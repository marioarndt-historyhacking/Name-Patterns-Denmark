#!/usr/bin/env python3
import csv,json,random
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
rows=list(csv.DictReader((ROOT/'outputs'/'daenemark_dewiki.csv').open()))[:34]
def norm(s):
    x=s.split()[0]
    return {'Hardiknut':'Knut','Frederik':'Friedrich'}.get(x,x)
names=[norm(r['name_wikipedia']) for r in rows]
years=[int(r['beginn']) for r in rows]
n=len(rows)

def candidates():
    c=[]
    for L in range(2,n//2+1):
        for gap in range(3):
            for i in range(n-(2*L+gap)+1):
                j=i+L+gap
                delta=years[j]-years[i]
                if all(years[j+k]-years[i+k]==delta for k in range(L)):
                    c.append((L,gap,i,j,delta))
    return c
C=candidates()
def stat(seq):
    best=0
    for L,g,i,j,d in C:
        if L>best and seq[i:i+L]==seq[j:j+L]: best=L
    return best
obs=stat(names); hits=[{'length':L,'gap':g,'start1':i,'start2':j,'year_shift':d} for L,g,i,j,d in C if L==obs and names[i:i+L]==names[j:j+L]]
B=200000; rng=random.Random(20261029); exc=0; hist={}; w=names[:]
for _ in range(B):
    rng.shuffle(w); s=stat(w); exc+=s>=obs; hist[s]=hist.get(s,0)+1
p=(exc+1)/(B+1)
out={'n':n,'definition':'Automatische Suche über Blocklänge und 0–2 Zwischenkönige; identische Namensfolge und konstanter Amtsantritts-Zeitversatz für alle korrespondierenden Positionen',
     'observed_max_length':obs,'hits':hits,'B':B,'seed':20261029,'exceed':exc,'p_search_corrected':p,'null_distribution':hist,
     'date_note':'Primärwert Knut II = 1018; 1019 wird nur als Einjahres-Sensitivitätsvariante behandelt. Harald I ist für die Gesamthypothese auf 958 festgelegt.'}
(ROOT/'outputs'/'daenemark_zeitverschobene_bloecke.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
