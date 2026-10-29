#!/usr/bin/env python3
"""Merge per-operator research JSON files into data/tier1-reviews.json.

  python3 scripts/import_research.py <dir-with-slug.json-files>

Each file follows the schema in docs/research-brief.md. Only fields present in the file are
changed; ratings of null never overwrite an existing rating. Run
`python3 scripts/build_tier1.py apply` afterwards to rebuild the pages.
"""
from __future__ import annotations
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "tier1-reviews.json"
CRIT = ["terms", "payments", "safer", "complaints", "licence", "usability"]
ELIG = ["domain", "operator", "regulator", "market_permission", "terms_and_withdrawal_rules"]


def clip(s: str, n: int) -> str:
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def offer_from(f: dict) -> dict:
    w = f.get("welcome_offer") or {}
    parts = []
    for label, key in (("Min deposit", "min_deposit"), ("Wagering", "wagering"), ("Expiry", "expiry"), ("Max cashout", "max_cashout")):
        v = (w.get(key) or "").strip()
        if v:
            parts.append(f"{label}: {v}")
    return {
        "headline": clip(w.get("headline") or "Not verified yet", 120),
        "detail": " · ".join(parts) or "No offer conditions verified from the operator's own pages yet.",
        "verified": bool(w.get("verified")),
        "seen": w.get("seen") or "",
        "url": w.get("url") or "",
    }


def merge(entry: dict, d: dict) -> None:
    if d.get("checked"):
        entry["checked"] = d["checked"]
    if d.get("eligibility"):
        entry["eligibility"] = {k: d["eligibility"].get(k, {"status": "unverified", "note": "Not checked", "url": ""}) for k in ELIG}
    for k in CRIT:
        new = (d.get("criteria") or {}).get(k)
        if new and (new.get("rating") is not None or entry["criteria"][k]["rating"] is None):
            entry["criteria"][k] = {"rating": new.get("rating"), "note": new.get("note", ""), "url": new.get("url", "")}
    if d.get("facts"):
        entry["facts"] = d["facts"]
        entry["offer"] = offer_from(d["facts"])
        lic = (d["facts"].get("licence") or {}).get("value")
        if lic:
            entry["licence_line"] = clip(lic, 150)
    for k in ("red_flags", "pros", "cons", "unreachable"):
        if d.get(k) is not None:
            entry[k] = d[k]
    if d.get("notes"):
        entry["notes"] = [d["notes"]] if isinstance(d["notes"], str) else d["notes"]


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    data = json.loads(DATA.read_text(encoding="utf-8"))
    n = 0
    for f in sorted(Path(sys.argv[1]).glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        slug = d.get("slug") or f.stem
        if slug not in data["reviews"]:
            print("skip (unknown slug):", slug)
            continue
        merge(data["reviews"][slug], d)
        n += 1
    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Merged {n} research file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
