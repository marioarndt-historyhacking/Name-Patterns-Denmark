#!/usr/bin/env python3
import csv,json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent.parent
rows=list(csv.DictReader((ROOT/'outputs'/'daenemark_dewiki.csv').open()))[:34]
def norm(s):
    x=s.split()[0]
    return {'Hardiknut':'Knut','Frederik':'Friedrich'}.get(x,x)
names=[norm(r['name_wikipedia']) for r in rows]
vals=sorted(set(names)); base=np.array([vals.index(x) for x in names],dtype=np.int16)
n=len(base); lengths=np.arange(2,n+1); B=200000; seed=20261029

def counts(a):
    # Anzahl aller Fenster der Länge L mit gleichem Namen an beiden Rändern.
    return np.column_stack([(a[:,:n-L+1]==a[:,L-1:]).sum(axis=1) for L in lengths]).astype(np.int16)

rng=np.random.default_rng(seed); null=np.empty((B,len(lengths)),dtype=np.int16)
for start in range(0,B,5000):
    m=min(5000,B-start); order=np.argsort(rng.random((m,n)),axis=1)
    null[start:start+m]=counts(base[order])
obs=counts(base.reshape(1,-1))[0]
allc=np.vstack([obs,null])
# Empirische obere Randwahrscheinlichkeit je Länge für jede Zeile.
tail=np.empty(allc.shape,dtype=float)
for j in range(allc.shape[1]):
    col=allc[:,j]; unique,cnt=np.unique(col,return_counts=True)
    surv=np.cumsum(cnt[::-1])[::-1]/len(col); mp=dict(zip(unique,surv))
    tail[:,j]=np.array([mp[x] for x in col])
minp=tail.min(axis=1); obs_min=float(minp[0]); p_adj=float(np.mean(minp<=obs_min))
details=[]
for j,L in enumerate(lengths):
    if obs[j]: details.append({'length':int(L),'count':int(obs[j]),'p_length_raw':float(tail[0,j])})
best=[d for d in details if abs(d['p_length_raw']-obs_min)<1e-15]
out={'n':n,'B':B,'seed':seed,'searched_lengths':[2,n],
     'definition':'Alle Fensterlängen automatisch; Statistik je Länge = Zahl der Fenster mit gleichem normalisiertem Randnamen; Min-p-Korrektur über sämtliche Längen',
     'best_raw_p':obs_min,'best_lengths':best,'p_adjusted_over_lengths':p_adj,'all_observed_lengths':details}
(ROOT/'outputs'/'daenemark_automatische_fenstersuche.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
