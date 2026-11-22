#!/usr/bin/env python3
import csv,json,random
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
rows=list(csv.DictReader((ROOT/'outputs'/'daenemark_dewiki.csv').open()))
def norm(s):
    x=s.split()[0]
    return {'Hardiknut':'Knut','Frederik':'Friedrich'}.get(x,x)
names=[norm(r['name_wikipedia']) for r in rows]; years=[int(r['beginn']) for r in rows]; n=len(rows)

chains=[]
for L in range(2,n//3+1):
  for i in range(n):
    for g1 in range(3):
      j=i+L+g1
      for g2 in range(3):
        k=j+L+g2
        if k+L<=n and abs((years[j]-years[i])-(years[k]-years[j]))<=1:
          chains.append((L,i,j,k))
echoes=[]
for L in range(2,n//2+1):
  for gap in range(3):
    for i in range(n-(2*L+gap)+1):
      j=i+L+gap; ds=[years[j+q]-years[i+q] for q in range(L)]
      if max(ds)-min(ds)<=1: echoes.append((L,i,j))

def measures(s):
  ch=[x for x in chains if s[x[1]]==s[x[1]+x[0]-1] and s[x[2]]==s[x[2]+x[0]-1] and s[x[3]]==s[x[3]+x[0]-1]]
  ec=[x for x in echoes if s[x[1]:x[1]+x[0]]==s[x[2]:x[2]+x[0]]]
  return max((x[0] for x in ch),default=0),max((x[0] for x in ec),default=0),ch,ec

oc,oe,och,oec=measures(names); boundary_index=27 # nach Waldemar III.; 0-basiert nächste Position
B=200000;rng=random.Random(20261029);joint=0;joint_early=0;w=names[:]
for _ in range(B):
  rng.shuffle(w); c,e,ch,ec=measures(w)
  if c>=oc and e>=oe:
    joint+=1
    strong_ch=[x for x in ch if x[0]>=oc]; strong_ec=[x for x in ec if x[0]>=oe]
    # Keine starke Instanz beginnt in der zweiten Phase.
    if not any(x[1]>=boundary_index for x in strong_ch+strong_ec): joint_early+=1
out={'n':n,'boundary_after_unique_ruler_position':27,'boundary_description':'nach Waldemar III. (Herrschaftsende 1329; Interregnum ab 1332)',
     'observed_chain_length':oc,'observed_echo_length':oe,'B':B,'seed':20261029,
     'joint_exceed':joint,'p_joint_motifs':(joint+1)/(B+1),
     'joint_and_no_post_start_exceed':joint_early,'p_joint_and_no_post_start':(joint_early+1)/(B+1),
     'conditional_no_post_given_joint':joint_early/joint if joint else None,
     'warning':'Grenze 1329 ist historisch motiviert, aber nach Sichtung der Muster gewählt; H2 bleibt explorativ und benötigt externe Replikation.'}
(ROOT/'outputs'/'daenemark_gemeinsamer_phasentest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
