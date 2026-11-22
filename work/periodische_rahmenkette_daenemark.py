#!/usr/bin/env python3
import csv,json,random
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
rows=list(csv.DictReader((ROOT/'outputs'/'daenemark_dewiki.csv').open()))
def norm(s):
    x=s.split()[0]
    return {'Hardiknut':'Knut','Frederik':'Friedrich'}.get(x,x)
names=[norm(r['name_wikipedia']) for r in rows]; years=[int(r['beginn']) for r in rows]; n=len(rows)

# Geometrisch-kalendarische Kandidaten sind unabhängig von den Namen.
C=[]
for L in range(2,n//3+1):
    for i in range(n):
        for g1 in range(3):
            j=i+L+g1
            for g2 in range(3):
                k=j+L+g2
                if k+L>n: continue
                if abs((years[j]-years[i])-(years[k]-years[j]))<=1:
                    C.append((L,i,j,k,g1,g2,years[j]-years[i]))
def hits(seq):
    return [(L,i,j,k,g1,g2,d) for L,i,j,k,g1,g2,d in C
            if seq[i]==seq[i+L-1] and seq[j]==seq[j+L-1] and seq[k]==seq[k+L-1]]
H=hits(names); obs=max((x[0] for x in H),default=0)
B=200000;rng=random.Random(20261029);exc=0;hist={};w=names[:]
for _ in range(B):
    rng.shuffle(w); z=max((x[0] for x in hits(w)),default=0);exc+=z>=obs;hist[z]=hist.get(z,0)+1
p=(exc+1)/(B+1)
out={'n':n,'candidate_geometries':len(C),'definition':'Drei nichtüberlappende gleich lange Rahmenfenster; 0–2 Zwischenherrscher; Startjahre arithmetisch ±1; alle Längen/Positionen automatisch',
     'observed_max_length':obs,'observed_hits':[{'length':L,'starts_1based':[i+1,j+1,k+1],'gaps':[g1,g2],'year_step':d,
       'frames':[names[i],names[j],names[k]],'start_years':[years[i],years[j],years[k]]} for L,i,j,k,g1,g2,d in H if L==obs],
     'B':B,'seed':20261029,'exceed':exc,'p_search_corrected':p,'null_distribution':hist}
(ROOT/'outputs'/'daenemark_periodische_rahmenkette.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
