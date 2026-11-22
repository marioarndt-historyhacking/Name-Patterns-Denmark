#!/usr/bin/env python3
"""Vergleicht die Regierungsdauern namensgleicher dänischer Monarchen.

Konvention wie im Hauptbericht: Dauer = Endjahr minus Anfangsjahr. Bei
unterbrochenen Herrschaften werden die Teilzeiten addiert. Offene Herrschaften
werden nicht in den Gleichheitsvergleich einbezogen.
"""

from __future__ import annotations

import csv
import itertools
import json
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "outputs" / "daenemark_dewiki.csv"
OUT_CSV = ROOT / "outputs" / "daenemark_regierungsdauern_namensgleich.csv"
OUT_JSON = ROOT / "outputs" / "daenemark_regierungsdauervergleich.json"


def regnal_name(full_name: str) -> str:
    first = full_name.split()[0].rstrip(".")
    aliases = {
        "Hardiknut": "Knut",
        "Friedrich": "Frederik",
        "Margarethe": "Margrethe",
    }
    return aliases.get(first, first)


def intervals(text: str) -> list[tuple[int, int]]:
    # "1018/19–1035" soll gemäß Festlegung mit 1018 beginnen.
    # Alle expliziten Bereiche erfassen; "seit" bleibt offen.
    if text.startswith("seit"):
        return []
    found = re.findall(r"(\d{3,4})(?:/\d{2})?–(\d{3,4})", text)
    return [(int(a), int(b)) for a, b in found]


rows: list[dict] = []
with SOURCE.open(encoding="utf-8", newline="") as f:
    for position, row in enumerate(csv.DictReader(f), 1):
        spans = intervals(row["regierungszeit"])
        duration = sum(b - a for a, b in spans) if spans else None
        rows.append(
            {
                "position": position,
                "herrscher": row["name_wikipedia"],
                "regnalname": regnal_name(row["name_wikipedia"]),
                "regierungszeit": row["regierungszeit"],
                "teilzeiten": spans,
                "dauer_jahre": duration,
                "bis_1329": int(row["beginn"]) <= 1329,
            }
        )

groups = defaultdict(list)
for row in rows:
    groups[row["regnalname"]].append(row)

same_name_groups = {name: rs for name, rs in groups.items() if len(rs) >= 2}
pairwise = []
for name, rs in same_name_groups.items():
    completed = [r for r in rs if r["dauer_jahre"] is not None]
    for a, b in itertools.combinations(completed, 2):
        pairwise.append(
            {
                "regnalname": name,
                "herrscher_1": a["herrscher"],
                "dauer_1": a["dauer_jahre"],
                "herrscher_2": b["herrscher"],
                "dauer_2": b["dauer_jahre"],
                "differenz_jahre": abs(a["dauer_jahre"] - b["dauer_jahre"]),
                "beide_bis_1329": a["bis_1329"] and b["bis_1329"],
            }
        )

exact = [p for p in pairwise if p["differenz_jahre"] == 0]
near = [p for p in pairwise if p["differenz_jahre"] == 1]

with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
    fields = [
        "position",
        "herrscher",
        "regnalname",
        "regierungszeit",
        "dauer_jahre",
        "bis_1329",
    ]
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for r in rows:
        if r["regnalname"] in same_name_groups:
            writer.writerow({k: r[k] for k in fields})

payload = {
    "methode": (
        "Jahresgrenzen: Endjahr minus Anfangsjahr; bei mehreren Amtszeiten "
        "Summe der Teilzeiten. Knut II beginnt gemäß Festlegung 1018."
    ),
    "gruppen": {
        name: [
            {
                "herrscher": r["herrscher"],
                "regierungszeit": r["regierungszeit"],
                "dauer_jahre": r["dauer_jahre"],
                "bis_1329": r["bis_1329"],
            }
            for r in rs
        ]
        for name, rs in sorted(same_name_groups.items())
    },
    "exakt_gleiche_paare": exact,
    "bis_1329_exakt": [p for p in exact if p["beide_bis_1329"]],
    "bis_1329_differenz_ein_jahr": [p for p in near if p["beide_bis_1329"]],
}
OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

print(json.dumps({
    "exakt": exact,
    "bis_1329_nahe": [p for p in near if p["beide_bis_1329"]],
}, ensure_ascii=False, indent=2))
