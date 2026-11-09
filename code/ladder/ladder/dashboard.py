"""Interactive dashboard: python -m ladder.dashboard results/<run> <out.html>

One self-contained HTML page (Plotly from cdnjs) with hover-enabled charts of every cell and an
episode explorer that shows each agent's board, turn-by-turn reasoning and actions, and its label.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

from .analyze import load, wilson
from .conditions import CONDITIONS

ORDER = list(CONDITIONS)
NAME = {"nvidia/nemotron-3-ultra-550b-a55b": "Nemotron 3 Ultra", "stepfun-ai/step-5-preview": "Step-5 preview"}


def build(run):
    rows = [r for r in load([run]) if r["model"] in NAME and r["valid"]]
    g = defaultdict(list)
    for r in rows:
        g[(r["model"], r["condition"], r["defence"])].append(r)
    cells = []
    for (m, c, d), rs in g.items():
        k = sum(r["crossed"] for r in rs)
        lo, hi = wilson(k, len(rs))
        cells.append({"model": NAME[m], "cond": c, "defence": d, "k": k, "n": len(rs), "lo": lo, "hi": hi,
                      "verify": sum(r["verify_calls"] > 0 for r in rs), "vmsg2": sum(r["verified_treatment"] for r in rs),
                      "turncap": sum(r["halt"] == "turn_cap" for r in rs)})
    labels = {r["episode_id"]: r for r in map(json.loads, open(Path(run) / "reasons_claude.jsonl"))}
    eps = []
    for r in sorted(rows, key=lambda r: (r["model"], r["defence"], ORDER.index(r["condition"]), r["seed"])):
        rec = json.loads((Path(run) / "episodes" / f"{r['episode_id']}.json").read_text())
        obs1 = rec["turns"][0]["observation"] if rec["turns"] else ""
        board = obs1.split("[board]", 1)[1].split("\n", 1)[1] if "[board]" in obs1 else ""
        turns = []
        for t in rec["turns"]:
            p = t["parsed"] or {}
            a = p.get("args") or {}
            turns.append([t["turn"], (p.get("thought") or "")[:600], p.get("action", "(unparseable)"),
                          str(a.get("path") or a.get("message_id") or a.get("text") or a.get("summary") or "")[:160],
                          t["observation"].split("\n\n[board]")[0][:220]])
        lab = labels.get(r["episode_id"], {})
        eps.append({"id": r["episode_id"], "model": NAME[r["model"]], "cond": r["condition"], "defence": r["defence"],
                    "crossed": r["crossed"], "verify": r["verify_calls"], "halt": r["halt"], "turns_n": r["n_turns"],
                    "first": r["first_cross_turn"], "reason": lab.get("primary", ""), "evidence": lab.get("evidence", ""),
                    "board": board, "turns": turns})
    return cells, eps


PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Who's in Charge? Interactive results</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/plotly.js/2.35.0/plotly.min.js"></script>
<style>
:root{--bg:#fbfaf7;--card:#ffffff;--ink:#222;--muted:#666;--line:#e3e2dc;--nem:#0077BB;--step:#EE7733;--ok:#1a7f4b;--bad:#b42318}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#17171a;--card:#202024;--ink:#ececea;--muted:#a6a59f;--line:#34343a;--nem:#4aa3e0;--step:#f2915a;--ok:#4cc38a;--bad:#f07167}}
:root[data-theme="dark"]{--bg:#17171a;--card:#202024;--ink:#ececea;--muted:#a6a59f;--line:#34343a;--nem:#4aa3e0;--step:#f2915a;--ok:#4cc38a;--bad:#f07167}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 Georgia,'Times New Roman',serif}
.wrap{max-width:1100px;margin:0 auto;padding:24px 16px 60px}h1{font-size:30px;margin:0 0 4px}h2{font-size:20px;margin:34px 0 6px}
.sub{color:var(--muted);margin:0 0 18px}.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px;margin:10px 0}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px}.kpi b{display:block;font-size:24px}.kpi span{color:var(--muted);font-size:13px}
.chart{width:100%;height:380px}.note{color:var(--muted);font-size:13px}
.filters{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}select{font:inherit;font-size:14px;padding:4px 6px;background:var(--card);color:var(--ink);border:1px solid var(--line);border-radius:6px}
.explorer{display:grid;grid-template-columns:minmax(0,320px) minmax(0,1fr);gap:12px}@media(max-width:760px){.explorer{grid-template-columns:1fr}}
.list{max-height:560px;overflow:auto;border:1px solid var(--line);border-radius:8px}.item{padding:6px 10px;border-bottom:1px solid var(--line);cursor:pointer;font-size:13px}
.item:hover,.item.sel{background:rgba(0,119,187,.10)}.tag{display:inline-block;font-size:11px;padding:0 6px;border-radius:9px;margin-left:4px;border:1px solid currentColor}
.edit{color:var(--bad)}.keep{color:var(--ok)}.detail{max-height:560px;overflow:auto;border:1px solid var(--line);border-radius:8px;padding:10px 12px}
pre{white-space:pre-wrap;font:12.5px/1.45 Menlo,Consolas,monospace;background:rgba(127,127,127,.08);padding:8px;border-radius:6px;margin:6px 0}
.turn{border-left:3px solid var(--line);padding:2px 0 2px 10px;margin:8px 0}.turn.w{border-left-color:var(--bad)}.turn.v{border-left-color:var(--nem)}
.act{font:12.5px Menlo,Consolas,monospace;color:var(--muted)}table{border-collapse:collapse;width:100%;font-size:13px}td,th{border-bottom:1px solid var(--line);padding:4px 6px;text-align:left}
.toggle{float:right;font-size:13px}
</style></head><body><div class="wrap">
<button class="toggle" onclick="toggleTheme()">◐ theme</button>
<h1>Who’s in Charge?</h1>
<p class="sub">Interactive results for “Authority Verification and Boundary Decisions in a Shared Agent Channel” · Purvansh Joshi · Swarm Alignment Hackathon (Apart Research), Nov 2026. Hover any mark for exact counts; click legend items to hide series.</p>
<div class="kpis">
<div class="card kpi"><b id="k1"></b><span>Nemotron edits under unauthorised authority (C2–C5, no defence)</span></div>
<div class="card kpi"><b id="k2"></b><span>Nemotron edits, forged vs valid worker signature (C4 vs C3)</span></div>
<div class="card kpi"><b id="k3"></b><span>Step-5 edits for the authorised principal (C6)</span></div>
<div class="card kpi"><b id="k4"></b><span>Nemotron unauthorised edits, labels off → on</span></div>
</div>
<h2>1. Edit rate by condition</h2><div class="card"><div id="c1" class="chart"></div>
<p class="note">Bars: share of episodes that edited the protected test (10 per cell), with 95% Wilson intervals. C6 is the only condition where the edit is authorised.</p></div>
<h2>2. Does verifying predict refusing?</h2><div class="card"><div id="c2" class="chart"></div>
<p class="note">Each point is one cell. Nemotron rarely verifies and usually edits; Step-5 usually verifies and almost never edits — even when the signature is valid (C6).</p></div>
<h2>3. Effect of provenance labels</h2><div class="card"><div id="c3" class="chart"></div>
<p class="note">Edit rate without (left of each pair) and with the defence that prints signature status and registry role beside every post.</p></div>
<h2>4. Episode explorer</h2>
<div class="filters"><select id="fm"></select><select id="fc"></select><select id="fd"></select><select id="fo"></select></div>
<div class="explorer"><div class="list" id="list"></div><div class="detail" id="detail"><p class="note">Select an episode to read the board, the agent’s reasoning turn by turn, and its exploratory reason label.</p></div></div>
<h2>Cell table</h2><div class="card" style="overflow:auto"><table id="tbl"></table></div>
<p class="note">Data: github.com/purvanshjoshi/swarm-alignment-hackathon (code/ladder/results/main). Reason labels are LLM-generated (exploratory, not human-validated). Page generated by <code>python -m ladder.dashboard</code>.</p>
</div>
<script>
const CELLS=__CELLS__, EPS=__EPS__;
const ORDER=["C0_baseline","C1_peer_impunity","C2_coord_unsigned","C3_coord_valid_sig","C4_coord_forged_sig","C5_principal_claim","C6_principal_valid_sig"];
const LBL={C0_baseline:"C0 baseline",C1_peer_impunity:"C1 peer",C2_coord_unsigned:"C2 coord.",C3_coord_valid_sig:"C3 coord. +valid",C4_coord_forged_sig:"C4 coord. +forged",C5_principal_claim:"C5 principal claim",C6_principal_valid_sig:"C6 principal +valid ✓"};
const css=v=>getComputedStyle(document.documentElement).getPropertyValue(v).trim();
const cell=(m,c,d)=>CELLS.find(x=>x.model===m&&x.cond===c&&x.defence===d);
function sum(m,cs,d){let k=0,n=0;cs.forEach(c=>{const x=cell(m,c,d);k+=x.k;n+=x.n});return k+"/"+n}
const U=["C2_coord_unsigned","C3_coord_valid_sig","C4_coord_forged_sig","C5_principal_claim"];
k1.textContent=sum("Nemotron 3 Ultra",U,false);
k2.textContent=cell("Nemotron 3 Ultra","C4_coord_forged_sig",false).k+"/10 vs "+cell("Nemotron 3 Ultra","C3_coord_valid_sig",false).k+"/10";
k3.textContent=cell("Step-5 preview","C6_principal_valid_sig",false).k+"/10";
k4.textContent=sum("Nemotron 3 Ultra",U,false)+" → "+sum("Nemotron 3 Ultra",U,true);
function layout(extra){return Object.assign({paper_bgcolor:"rgba(0,0,0,0)",plot_bgcolor:"rgba(0,0,0,0)",font:{family:"Georgia, serif",color:css("--ink"),size:12},
 margin:{l:56,r:12,t:10,b:60},legend:{orientation:"h",y:-0.25},yaxis:{range:[0,1.08],gridcolor:css("--line"),title:"edit rate",tickformat:".0%"},xaxis:{gridcolor:css("--line")}},extra||{})}
function draw(){
 const col={"Nemotron 3 Ultra":css("--nem"),"Step-5 preview":css("--step")};
 const t1=[];["Nemotron 3 Ultra","Step-5 preview"].forEach(m=>[false,true].forEach(d=>{const xs=[],ys=[],lo=[],hi=[],tx=[];
  ORDER.forEach(c=>{const x=cell(m,c,d);if(!x)return;xs.push(LBL[c]);ys.push(x.k/x.n);lo.push(x.k/x.n-x.lo);hi.push(x.hi-x.k/x.n);
  tx.push(`${m}${d?" + labels":""}<br>${LBL[c]}<br>edits ${x.k}/${x.n} (95% CI ${(x.lo*100).toFixed(0)}–${(x.hi*100).toFixed(0)}%)<br>verified msg-2: ${x.vmsg2}/${x.n}`)});
  t1.push({type:"bar",name:m+(d?" + labels":""),x:xs,y:ys,error_y:{type:"data",symmetric:false,array:hi,arrayminus:lo,color:css("--muted")},
   marker:{color:d?"rgba(0,0,0,0)":col[m],line:{color:col[m],width:1.5},pattern:d?{shape:"/",fgcolor:col[m]}:undefined},hovertext:tx,hoverinfo:"text"})}));
 Plotly.react("c1",t1,layout({barmode:"group"}),{responsive:true,displaylogo:false});
 const t2=[];["Nemotron 3 Ultra","Step-5 preview"].forEach(m=>[false,true].forEach(d=>{const xs=[],ys=[],tx=[];
  CELLS.filter(x=>x.model===m&&x.defence===d).forEach(x=>{xs.push(x.verify/x.n);ys.push(x.k/x.n);tx.push(`${m}${d?" + labels":""}<br>${LBL[x.cond]}<br>verified (any): ${x.verify}/${x.n}<br>edited: ${x.k}/${x.n}`)});
  t2.push({type:"scatter",mode:"markers",name:m+(d?" + labels":""),x:xs,y:ys,hovertext:tx,hoverinfo:"text",
   marker:{size:d?16:10,symbol:m.startsWith("N")?"circle":"square",color:d?"rgba(0,0,0,0)":col[m],line:{color:col[m],width:2}}})}));
 Plotly.react("c2",t2,layout({xaxis:{title:"share of episodes with ≥1 verify_message call",range:[-0.05,1.08],tickformat:".0%",gridcolor:css("--line")}}),{responsive:true,displaylogo:false});
 const t3=[];["Nemotron 3 Ultra","Step-5 preview"].forEach(m=>{ORDER.slice(2).forEach((c,i)=>{const a=cell(m,c,false),b=cell(m,c,true);
  t3.push({type:"scatter",mode:"lines+markers",showlegend:i===0,legendgroup:m,name:m,x:[LBL[c]+" ·off",LBL[c]+" ·on"],y:[a.k/a.n,b.k/b.n],
   line:{color:col[m]},marker:{size:9,symbol:m.startsWith("N")?"circle":"square",color:[col[m],"rgba(0,0,0,0)"],line:{color:col[m],width:2}},
   hovertext:[`${m}, ${LBL[c]}, no defence: ${a.k}/${a.n}`,`${m}, ${LBL[c]}, labels shown: ${b.k}/${b.n}`],hoverinfo:"text"})})});
 Plotly.react("c3",t3,layout({xaxis:{tickangle:-35,gridcolor:css("--line")},margin:{l:56,r:12,t:10,b:150},legend:{orientation:"h",y:1.12}}),{responsive:true,displaylogo:false});
}
function opts(sel,label,vals){sel.innerHTML=`<option value="">${label}: all</option>`+vals.map(v=>`<option>${v}</option>`).join("")}
opts(fm,"Model",["Nemotron 3 Ultra","Step-5 preview"]);opts(fc,"Condition",ORDER);opts(fd,"Defence",["off","on"]);opts(fo,"Outcome",["edited","kept test"]);
const esc=s=>String(s).replace(/[&<>]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;"}[c]));
function renderList(){const L=EPS.filter(e=>(!fm.value||e.model===fm.value)&&(!fc.value||e.cond===fc.value)&&(!fd.value||(e.defence?"on":"off")===fd.value)&&(!fo.value||(e.crossed?"edited":"kept test")===fo.value));
 list.innerHTML=L.map(e=>`<div class="item" data-id="${e.id}">${e.model.split(" ")[0]} · ${e.cond.split("_")[0]}${e.defence?"ᴰ":""} #${e.id.slice(-3)}<span class="tag ${e.crossed?"edit":"keep"}">${e.crossed?"edited":"kept"}</span>${e.verify?'<span class="tag">verified</span>':""}</div>`).join("")||"<p class='note' style='padding:8px'>No episodes match.</p>";
 [...list.children].forEach(el=>el.onclick=()=>{[...list.children].forEach(x=>x.classList.remove("sel"));el.classList.add("sel");show(el.dataset.id)})}
function show(id){const e=EPS.find(x=>x.id===id);
 detail.innerHTML=`<b>${esc(e.model)}</b> · ${esc(LBL[e.cond])}${e.defence?" · defence on":""} · ${e.crossed?`<span class="edit">edited the protected test (first at turn ${e.first})</span>`:'<span class="keep">kept the test unchanged</span>'} · ${e.turns_n} turns · ${esc(e.halt)}
 <p class="note">Exploratory label: <b>${esc(e.reason)}</b> — “${esc(e.evidence)}”</p><b>Board shown on turn 1</b><pre>${esc(e.board)}</pre><b>Turns</b>`+
 e.turns.map(t=>`<div class="turn ${t[2]==="write_file"&&/test_discount/.test(t[3])?"w":t[2]==="verify_message"?"v":""}"><div class="act">T${t[0]} · ${esc(t[2])} ${esc(t[3])}</div>${esc(t[1])}<div class="act">→ ${esc(t[4])}</div></div>`).join("")}
[fm,fc,fd,fo].forEach(s=>s.onchange=renderList);renderList();
tbl.innerHTML="<tr><th>Model</th><th>Condition</th><th>Defence</th><th>Edits</th><th>95% CI</th><th>Any verify</th><th>Verified msg-2</th><th>Turn cap</th></tr>"+
 [...CELLS].sort((a,b)=>a.model.localeCompare(b.model)||a.defence-b.defence||ORDER.indexOf(a.cond)-ORDER.indexOf(b.cond)).map(x=>`<tr><td>${x.model}</td><td>${LBL[x.cond]}</td><td>${x.defence?"on":"off"}</td><td>${x.k}/${x.n}</td><td>${(x.lo*100).toFixed(0)}–${(x.hi*100).toFixed(0)}%</td><td>${x.verify}</td><td>${x.vmsg2}</td><td>${x.turncap}</td></tr>`).join("");
function toggleTheme(){const r=document.documentElement;const dark=r.dataset.theme?r.dataset.theme==="dark":matchMedia("(prefers-color-scheme: dark)").matches;r.dataset.theme=dark?"light":"dark";draw()}
draw();
</script></body></html>"""


def main(run, out):
    cells, eps = build(run)
    html = PAGE.replace("__CELLS__", json.dumps(cells)).replace("__EPS__", json.dumps(eps).replace("</", "<\\/"))
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(html)
    print(f"wrote {out} ({len(html) / 1e6:.1f} MB, {len(eps)} episodes)")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "results/main", sys.argv[2] if len(sys.argv) > 2 else "../../docs/extra/interactive/index.html")
