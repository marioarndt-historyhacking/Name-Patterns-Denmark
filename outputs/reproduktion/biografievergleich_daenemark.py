#!/usr/bin/env python3
import csv,json,itertools
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
rows=list(csv.DictReader((ROOT/'outputs'/'daenemark_biografische_daten_bis_1329.csv').open()))
def val(x): return int(x) if x else None
def family(s):
    x=s.split()[0]
    return {'Hardiknut':'Knut'}.get(x,x)
for r in rows:
    for k in ['position','birth_min','birth_max','death_min','death_max','accession','end_reign']: r[k]=val(r[k])
    if r['birth_min'] is not None:
        r['age_min']=r['death_min']-r['birth_max']
        r['age_max']=r['death_max']-r['birth_min']
        r['age_year_difference']=((r['death_min']+r['death_max'])-(r['birth_min']+r['birth_max']))/2
    else: r['age_min']=r['age_max']=r['age_year_difference']=None

age_matches=[]
for a,b in itertools.combinations(rows,2):
    if family(a['name'])!=family(b['name']) or a['age_min'] is None or b['age_min'] is None: continue
    overlap=max(a['age_min'],b['age_min'])<=min(a['age_max'],b['age_max'])
    close=abs(a['age_year_difference']-b['age_year_difference'])<=1
    if overlap or close:
        age_matches.append({'name_family':family(a['name']),'ruler1':a['name'],'age1':[a['age_min'],a['age_max']],
                            'ruler2':b['name'],'age2':[b['age_min'],b['age_max']],
                            'intervals_overlap':overlap,'year_difference_close':close})

birth_accession=[]
for idx,r in enumerate(rows):
    if r['birth_min'] is None: continue
    for p in rows[:idx]:
        exact=r['birth_min']<=p['accession']<=r['birth_max']
        distance=min(abs(p['accession']-r['birth_min']),abs(p['accession']-r['birth_max']))
        if exact or distance<=1:
            birth_accession.append({'ruler_born':r['name'],'birth':[r['birth_min'],r['birth_max']],
                                    'earlier_ruler':p['name'],'accession':p['accession'],'exact_interval_match':exact,'distance_years':0 if exact else distance})
out={'n':len(rows),'age_method':'Jahresalter: Todesjahr minus Geburtsjahr; Tage und Monate bleiben unberücksichtigt',
     'same_name_age_matches':age_matches,'birth_vs_earlier_accession_matches_within_1_year':birth_accession}
(ROOT/'outputs'/'daenemark_biografievergleich.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
