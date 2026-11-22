#!/usr/bin/env python3
import csv, json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent.parent
rows=list(csv.DictReader((ROOT/'outputs'/'daenemark_dewiki.csv').open()))[:34]

def ident(name):
    x=name.split()[0]
    return {'Frederik':'Friedrich','Hardiknut':'Knut'}.get(x,x)

labels=[ident(r['name_wikipedia']) for r in rows]
ids=np.array([sorted(set(labels)).index(x) for x in labels],dtype=np.int16)
n=len(ids); B=200_000; seed=20261029; rng=np.random.default_rng(seed)

def maxblock(a):
    # a: (batch,n); returns maximum repeated block length for each row.
    out=np.zeros(a.shape[0],dtype=np.int16)
    for L in range(1,n//2+1):
        possible=np.zeros(a.shape[0],dtype=bool)
        for gap in range(3):
            for i in range(0,n-(2*L+gap)+1):
                possible |= np.all(a[:,i:i+L]==a[:,i+L+gap:i+2*L+gap],axis=1)
        out[possible]=L
    return out

obs=maxblock(ids.reshape(1,-1))[0]
exceed=0; hist={}
for start in range(0,B,5000):
    m=min(5000,B-start)
    order=np.argsort(rng.random((m,n)),axis=1)
    st=maxblock(ids[order])
    exceed += int(np.sum(st>=obs))
    for v,c in zip(*np.unique(st,return_counts=True)): hist[int(v)]=hist.get(int(v),0)+int(c)
p=(exceed+1)/(B+1)
result={'n':n,'B':B,'seed':seed,'observed_max_block':int(obs),'exceed':exceed,'p_raw_search_corrected':p,
        'null_distribution':hist,'normalization':'Hardiknut=Knut; Frederik=Friedrich; Ordnungszahlen/Beinamen entfernt'}
(ROOT/'outputs'/'daenemark_mittelalter_signifikanz.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
