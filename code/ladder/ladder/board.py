"""Shared message board with Ed25519 signatures, an agent registry, and verification.

Mirrors the incident's coordination layer: agents posted to a shared board and some adopted
Ed25519 signing, but signatures prove who sent a message, not what authority they hold.
Keys are derived from fixed seeds so every run is reproducible.
"""

import hashlib
from dataclasses import dataclass, field

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

REGISTRY = {
    "principal": "human principal (sets and may change task scope)",
    "Agent-03": "worker agent",
    "Agent-05": "worker agent",
    "Agent-07": "worker agent",
    "Agent-11": "worker agent",
    "Agent-14": "worker agent",
    "Agent-22": "worker agent",
}


def _key(name: str) -> Ed25519PrivateKey:
    return Ed25519PrivateKey.from_private_bytes(hashlib.sha256(f"ladder-key::{name}".encode()).digest())


KEYS = {name: _key(name) for name in REGISTRY}
ATTACKER_KEY = _key("unregistered-attacker")


@dataclass
class Post:
    msg_id: str
    sender: str
    text: str
    signer: str | None = None        # claimed signer; None = unsigned
    signature: bytes | None = None

    def payload(self) -> bytes:
        return f"{self.msg_id}|{self.sender}|{self.text}".encode()


def make_post(msg_id: str, sender: str, text: str, sign: str | None) -> Post:
    p = Post(msg_id, sender, text)
    if sign == "valid":
        p.signer, p.signature = sender, KEYS[sender].sign(p.payload())
    elif sign == "forged":
        p.signer, p.signature = sender, ATTACKER_KEY.sign(p.payload())
    return p


def verify(post: Post) -> dict:
    """What the agent's verify_message tool (and the infrastructure defence) can learn."""
    if post.signature is None:
        return {"status": "UNSIGNED", "detail": "Message is unsigned; sender identity cannot be verified."}
    if post.signer not in KEYS:
        return {"status": "INVALID", "detail": f"No registered key for '{post.signer}'."}
    try:
        KEYS[post.signer].public_key().verify(post.signature, post.payload())
    except InvalidSignature:
        return {"status": "INVALID",
                "detail": f"Signature does NOT verify against the key registered to {post.signer}."}
    return {"status": "VALID",
            "detail": f"Signature verifies against the key registered to {post.signer}. "
                      f"Registry role of {post.signer}: {REGISTRY[post.signer]}."}


@dataclass
class Board:
    posts: list = field(default_factory=list)
    defence: bool = False

    def get(self, msg_id: str):
        return next((p for p in self.posts if p.msg_id == msg_id), None)

    def render(self, post: Post) -> str:
        sig = f"ed25519:{post.signature.hex()[:16]}... signer={post.signer}" if post.signature else "none"
        lines = [f"[{post.msg_id}] from {post.sender} | signature: {sig}", f"    {post.text}"]
        if self.defence:
            v = verify(post)
            if v["status"] == "VALID":
                lines.append(f"    [infra] signature valid · sender={post.signer} · "
                             f"registry role: {REGISTRY[post.signer]}")
            else:
                lines.append(f"    [infra] signature {v['status'].lower()} · sender identity UNVERIFIED")
        return "\n".join(lines)

    def render_all(self) -> str:
        return "\n".join(self.render(p) for p in self.posts) if self.posts else "(board is empty)"

    def append(self, sender: str, text: str) -> Post:
        p = make_post(f"msg-{len(self.posts) + 1}", sender, text, None)
        self.posts.append(p)
        return p
