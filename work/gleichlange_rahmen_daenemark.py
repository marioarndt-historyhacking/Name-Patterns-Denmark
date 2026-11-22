#!/usr/bin/env python3
import csv,json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent.parent
rows=list(csv.DictReader((ROOT/'outputs'/'daenemark_dewiki.csv').open()))[:34]
def nid(s):
    x=s.split()[0]
    return {'Hardiknut':'Knut','Frederik':'Friedrich'}.get(x,x)
names=[nid(r['name_wikipedia']) for r in rows]
vals=sorted(set(names)); ids=np.array([vals.index(x) for x in names],dtype=np.int16)

def stat(a):
    # Größte Länge L zweier Blöcke gleicher Länge. Jeder Block wird vom
    # gleichen Namen gerahmt; zwischen den Blöcken liegen höchstens 2 Könige.
    b,n=a.shape; out=np.zeros(b,dtype=np.int16)
    for L in range(2,n//2+1):
        ok=np.zeros(b,dtype=bool)
        for gap in range(3):
            for i in range(n-(2*L+gap)+1):
                j=i+L+gap
                ok |= (a[:,i]==a[:,i+L-1]) & (a[:,j]==a[:,j+L-1]) & (a[:,i]!=a[:,j])
        out[ok]=L
    return out

hits=[]; n=len(ids)
for L in range(2,n//2+1):
    for gap in range(3):
        for i in range(n-(2*L+gap)+1):
            j=i+L+gap
            if ids[i]==ids[i+L-1] and ids[j]==ids[j+L-1] and ids[i]!=ids[j]:
                hits.append({'laenge':L,'luecke':gap,'start1':i,'end1':i+L-1,'start2':j,'end2':j+L-1,
                             'rahmen1':names[i],'rahmen2':names[j]})
obs=int(stat(ids.reshape(1,-1))[0])
B=200000; rng=np.random.default_rng(20261029); exc=0; hist={}
for start in range(0,B,5000):
    m=min(5000,B-start); order=np.argsort(rng.random((m,n)),axis=1); s=stat(ids[order]); exc+=int((s>=obs).sum())
    for v,c in zip(*np.unique(s,return_counts=True)): hist[int(v)]=hist.get(int(v),0)+int(c)
p=(exc+1)/(B+1)
out={'definition':'Zwei verschieden benannte, gleich lange Namensrahmen; je Block gleicher Name am Anfang und Ende; 0–2 Zwischenkönige',
     'n':n,'observed_max_length':obs,'hits':[h for h in hits if h['laenge']==obs],
     'B':B,'seed':20261029,'exceed':exc,'p_search_corrected':p,'null_distribution':hist}
(ROOT/'outputs'/'daenemark_gleichlange_rahmen.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
