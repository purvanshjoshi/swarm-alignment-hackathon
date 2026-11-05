"""Download the reference papers and web reports for the Swarm Alignment Hackathon.

Each arXiv ID is checked against the arXiv API before downloading: if the
returned title does not contain the expected keyword, the PDF is skipped and
flagged so a wrong ID never silently lands in the library.

Usage:  python -I download_papers.py            (run from anywhere)
"""
import json
import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UA = {"User-Agent": "Mozilla/5.0 (research download script)"}

# (folder, arxiv_id, short_name, keyword that must appear in the real title)
PAPERS = [
    # Organizer labs
    ("01_ae_studio_aiaf", "2412.16325", "SOO_self_other_overlap_honest_agents", "Self-Other Overlap"),
    ("01_ae_studio_aiaf", "2607.08077", "GRAM_modular_pretraining_access_control", "Modular Pretraining"),
    ("01_ae_studio_aiaf", "2602.06941", "endogenous_steering_resistance", "Steering"),
    ("01_ae_studio_aiaf", "2410.04332", "gradient_routing", "Gradient Routing"),
    ("02_apart_research", "2502.19145", "multi_agent_security_tax", "Security Tax"),
    # Incident investigators
    ("03_redwood_control", "2312.06942", "AI_control_intentional_subversion", "AI Control"),
    ("03_redwood_control", "2504.10374", "ctrl_z_resampling_agents", "Ctrl-Z"),
    ("03_redwood_control", "2412.14093", "alignment_faking", "Alignment Faking"),
    ("04_metr", "2503.14499", "measuring_long_tasks", "Long Software Tasks"),
    ("04_metr", "2411.15114", "RE_bench", "RE-Bench"),
    # Multi-agent safety literature
    ("05_multi_agent_literature", "2502.14143", "multi_agent_risks_advanced_AI", "Multi-Agent Risks"),
    ("05_multi_agent_literature", "2402.07510", "secret_collusion_steganography", "Secret Collusion"),
    ("05_multi_agent_literature", "2602.15198", "colosseum_auditing_collusion", "Colosseum"),
    ("05_multi_agent_literature", "2609.15494", "troy_moment_impossible_tasks_peer_authority", "Troy Moment"),
    ("05_multi_agent_literature", "2505.02077", "open_challenges_multi_agent_security", "Multi-Agent Security"),
    ("05_multi_agent_literature", "2410.07283", "prompt_infection", "Prompt Infection"),
    ("05_multi_agent_literature", "2402.08567", "agent_smith_jailbreak_spread", "Agent Smith"),
    ("05_multi_agent_literature", "2406.14595", "misuse_combinations_safe_models", "Combinations of Safe Models"),
    ("05_multi_agent_literature", "2404.16698", "govsim_cooperate_or_collapse", "Cooperate or Collapse"),
    ("05_multi_agent_literature", "2312.03664", "concordia_generative_agent_sims", "Concordia"),
    ("05_multi_agent_literature", "2304.03442", "generative_agents", "Generative Agents"),
]

# Web pages saved as raw HTML (reports, blog posts, sprint rubrics).
PAGES = [
    ("00_incident_report", "metr_huggingface_incident_report",
     "https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/"),
    ("01_ae_studio_aiaf", "aiaf_homepage", "https://www.aialignmentfoundation.org/"),
    ("01_ae_studio_aiaf", "ae_studio_alignment", "https://ae.studio/ai-alignment"),
    ("01_ae_studio_aiaf", "lesswrong_SOO_llm_deception",
     "https://www.lesswrong.com/posts/jtqcsARGtmgogdcLT"),
    ("01_ae_studio_aiaf", "anthropic_blog_modular_pretraining",
     "https://alignment.anthropic.com/2026/modular-pretraining/"),
    ("02_apart_research", "sprint_ai_collusion_oct2026",
     "https://apartresearch.com/sprints/ai-collusion-research-sprint-2026-10-23-to-2026-10-25"),
    ("02_apart_research", "sprint_agent_attribution_2026",
     "https://apartresearch.com/sprints/agent-attribution-2026"),
    ("02_apart_research", "sprint_threat_intel_rubric_2026",
     "https://apartresearch.com/sprints/threat-intelligence-threat-modelling-2026"),
]


def fetch(url, timeout=180, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception:
            if attempt == retries - 1:
                raise
            time.sleep(10)


def arxiv_titles(ids):
    url = "https://export.arxiv.org/api/query?max_results=100&id_list=" + ",".join(ids)
    ns = {"a": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(fetch(url))
    out = {}
    for e in root.findall("a:entry", ns):
        aid = e.find("a:id", ns).text.rsplit("/", 1)[-1]
        aid = re.sub(r"v\d+$", "", aid)
        out[aid] = {
            "title": " ".join(e.find("a:title", ns).text.split()),
            "authors": [a.find("a:name", ns).text for a in e.findall("a:author", ns)],
            "published": e.find("a:published", ns).text[:10],
            "abstract": " ".join(e.find("a:summary", ns).text.split()),
        }
    return out


def main():
    manifest, problems = [], []
    meta = arxiv_titles([p[1] for p in PAPERS])

    for folder, aid, name, keyword in PAPERS:
        info = meta.get(aid)
        if not info or keyword.lower() not in info["title"].lower():
            problems.append(f"{aid} ({name}): title check failed -> {info['title'] if info else 'not found'}")
            continue
        dest = ROOT / folder / f"{aid}_{name}.pdf"
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            try:
                data = fetch(f"https://export.arxiv.org/pdf/{aid}")
                if not data.startswith(b"%PDF"):
                    raise ValueError("response is not a PDF")
                dest.write_bytes(data)
                time.sleep(3)  # arXiv asks for polite rate limiting
            except Exception as ex:
                problems.append(f"{aid} ({name}): download failed -> {ex}")
                continue
        manifest.append({"folder": folder, "file": dest.name, "arxiv": aid,
                         "url": f"https://arxiv.org/abs/{aid}", **info})
        print(f"ok   {dest.relative_to(ROOT)}", flush=True)

    for folder, name, url in PAGES:
        dest = ROOT / folder / f"{name}.html"
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            dest.write_bytes(fetch(url))
            manifest.append({"folder": folder, "file": dest.name, "url": url})
            print(f"ok   {dest.relative_to(ROOT)}", flush=True)
        except Exception as ex:
            problems.append(f"{url}: {ex}")

    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\n{len(manifest)} items saved.")
    if problems:
        print("PROBLEMS:\n  " + "\n  ".join(problems))
        sys.exit(1)


if __name__ == "__main__":
    main()
