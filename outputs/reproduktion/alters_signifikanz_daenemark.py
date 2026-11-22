#!/usr/bin/env python3
import csv,json,random,itertools
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
rows=[]
for r in csv.DictReader((ROOT/'outputs'/'daenemark_biografische_daten_bis_1329.csv').open()):
    if not r['birth_min']: continue
    fam={'Hardiknut':'Knut'}.get(r['name'].split()[0],r['name'].split()[0])
    b0,b1,d0,d1=map(int,[r['birth_min'],r['birth_max'],r['death_min'],r['death_max']])
    rows.append({'family':fam,'lo':d0-b1,'hi':d1-b0,'mid':((d0+d1)-(b0+b1))/2})
def stats(labels):
    overlap=close=0
    for i,j in itertools.combinations(range(len(rows)),2):
        if labels[i]!=labels[j]: continue
        overlap += max(rows[i]['lo'],rows[j]['lo'])<=min(rows[i]['hi'],rows[j]['hi'])
        close += abs(rows[i]['mid']-rows[j]['mid'])<=1
    return overlap,close
labels=[r['family'] for r in rows]; obs=stats(labels);B=200000;rng=random.Random(20261029);eo=ec=0;hist={};w=labels[:]
for _ in range(B):
    rng.shuffle(w);s=stats(w);eo+=s[0]>=obs[0];ec+=s[1]>=obs[1];hist[str(s)]=hist.get(str(s),0)+1
out={'n_with_usable_age':len(rows),'observed_overlap_pairs':obs[0],'observed_close_midpoint_pairs':obs[1],
     'B':B,'seed':20261029,'p_overlap':(eo+1)/(B+1),'p_close_midpoint':(ec+1)/(B+1),
     'warning':'Explorativ; ausschließlich Todesjahr minus Geburtsjahr, ohne Tage oder Monate; Intervalle beruhen teilweise auf circa-Angaben.'}
(ROOT/'outputs'/'daenemark_alters_signifikanz.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
