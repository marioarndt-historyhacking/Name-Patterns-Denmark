#!/usr/bin/env python3
"""Explorative Prüfung der kombinierten Gruppenregel bis Waldemar III.

Eine Namensfamilie mit mindestens drei Königen gilt als getroffen, wenn es
innerhalb der Familie mindestens ein Paar mit exakt gleicher, aus Jahresgrenzen
berechneter Regierungsdauer ODER mit höchstens einem Jahr Unterschied des aus
Geburts- und Todesjahr berechneten Lebensalters gibt. Tage und Monate werden
nicht verwendet.
"""

from __future__ import annotations

import csv
import itertools
import json
import random
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIO = ROOT / "outputs" / "daenemark_biografische_daten_bis_1329.csv"
OUT = ROOT / "outputs" / "daenemark_kombinierte_gruppenregel.json"


def family(name: str) -> str:
    first = name.split()[0].rstrip(".")
    return {"Hardiknut": "Knut"}.get(first, first)


rows = []
for r in csv.DictReader(BIO.open(encoding="utf-8", newline="")):
    b0 = int(r["birth_min"]) if r["birth_min"] else None
    b1 = int(r["birth_max"]) if r["birth_max"] else None
    d0 = int(r["death_min"]) if r["death_min"] else None
    d1 = int(r["death_max"]) if r["death_max"] else None
    # Christoph II.: 1320–1326 + 1329–1332 = 9 Jahre. Alle anderen sind
    # innerhalb dieses Datensatzes durchgehend im Amt.
    if r["name"].startswith("Christoph II."):
        reign_duration = 9
    else:
        reign_duration = int(r["end_reign"]) - int(r["accession"])
    # Reine Jahresdifferenz gemäß Festlegung des Nutzers, ohne Korrektur danach,
    # ob Geburtstag oder Todestag im jeweiligen Jahr schon erreicht war.
    age_lo = None if b0 is None else d0 - b1
    age_hi = None if b0 is None else d1 - b0
    rows.append(
        {
            "name": r["name"],
            "family": family(r["name"]),
            "reign_duration": reign_duration,
            "age_lo": age_lo,
            "age_hi": age_hi,
        }
    )

counts = Counter(r["family"] for r in rows)
large_families = sorted(f for f, n in counts.items() if n >= 3)


def evidence_for(labels: list[str]):
    groups = defaultdict(list)
    for idx, label in enumerate(labels):
        groups[label].append(idx)
    evidence = {}
    for label in large_families:
        reign_pairs = []
        age_pairs = []
        for i, j in itertools.combinations(groups[label], 2):
            a, b = rows[i], rows[j]
            if a["reign_duration"] == b["reign_duration"]:
                reign_pairs.append((i, j))
            if a["age_lo"] is not None and b["age_lo"] is not None:
                interval_distance = max(
                    0,
                    a["age_lo"] - b["age_hi"],
                    b["age_lo"] - a["age_hi"],
                )
            else:
                interval_distance = None
            if interval_distance is not None and interval_distance <= 1:
                age_pairs.append((i, j))
        evidence[label] = {"reign_pairs": reign_pairs, "age_pairs": age_pairs}
    return evidence


labels = [r["family"] for r in rows]
observed = evidence_for(labels)


def named_pair(pair):
    i, j = pair
    a, b = rows[i], rows[j]
    return {
        "ruler1": a["name"],
        "ruler2": b["name"],
        "reign_duration1": a["reign_duration"],
        "reign_duration2": b["reign_duration"],
        "age_years1": [a["age_lo"], a["age_hi"]] if a["age_lo"] is not None else None,
        "age_years2": [b["age_lo"], b["age_hi"]] if b["age_lo"] is not None else None,
    }


observed_named = {
    label: {
        "n": counts[label],
        "equal_reign_pairs": [named_pair(p) for p in ev["reign_pairs"]],
        "age_pairs_within_1": [named_pair(p) for p in ev["age_pairs"]],
        "rule_satisfied": bool(ev["reign_pairs"] or ev["age_pairs"]),
    }
    for label, ev in observed.items()
}

B = 200_000
rng = random.Random(20261030)
work = labels[:]
at_least_observed = 0
observed_covered = sum(v["rule_satisfied"] for v in observed_named.values())
coverage_histogram = Counter()
for _ in range(B):
    rng.shuffle(work)
    ev = evidence_for(work)
    covered = sum(bool(v["reign_pairs"] or v["age_pairs"]) for v in ev.values())
    coverage_histogram[covered] += 1
    at_least_observed += covered >= observed_covered

result = {
    "scope": "Harald I. bis Waldemar III.; Namensfamilien mit mindestens drei Königen",
    "rule": (
        "Mindestens ein Paar je Namensfamilie mit exakt gleicher Regierungsdauer "
        "oder höchstens 1 Jahr Differenz des Jahresalters (Todesjahr minus Geburtsjahr)"
    ),
    "age_caveat": (
        "Nur Jahreszahlen; Tage und Monate werden nicht berücksichtigt. Bei circa- "
        "und Doppeljahrangaben werden die möglichen Jahresalter als Intervall geführt."
    ),
    "groups": observed_named,
    "covered_groups": observed_covered,
    "eligible_groups": len(large_families),
    "permutation_test": {
        "B": B,
        "seed": 20261030,
        "null": "Zufällige Neuverteilung der vorhandenen Namensetiketten bei festen Gruppengrößen",
        "hits_at_least_observed": at_least_observed,
        "p": (at_least_observed + 1) / (B + 1),
        "coverage_histogram": dict(sorted(coverage_histogram.items())),
        "warning": (
            "Post-hoc und explorativ: Schwelle, Mindestgruppengröße und ODER-Regel "
            "wurden nach Sichtung der dänischen Daten formuliert."
        ),
    },
}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
