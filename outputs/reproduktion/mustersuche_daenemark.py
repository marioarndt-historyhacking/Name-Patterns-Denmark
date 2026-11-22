#!/usr/bin/env python3
"""Exakte Wiederholungsblöcke in der bereinigten dänischen Herrscherfolge."""
import csv, json, re
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CSV=ROOT/'outputs'/'daenemark_dewiki.csv'

def name_id(name):
    first=re.split(r'\s+',name.strip())[0]
    return {'Frederik':'Friedrich'}.get(first,first)

def suchen(rows,max_luecke=2):
    seq=[name_id(r['name_wikipedia']) for r in rows]
    treffer=[]; n=len(seq)
    for i in range(n):
        for j in range(i+1,n):
            for L in range(1,min(j-i,n-j)+1):
                gap=j-(i+L)
                if 0 <= gap <= max_luecke and seq[i:i+L]==seq[j:j+L]:
                    treffer.append({'start1':i,'end1':i+L-1,'start2':j,'end2':j+L-1,
                                    'laenge':L,'luecke':gap,'muster':seq[i:i+L]})
    # Nur Treffer behalten, die bei denselben beiden Starts nicht kürzer sind,
    # und zusätzlich die globale Maximalgruppe ausweisen.
    maximal=[]
    for t in treffer:
        if not any(u['start1']==t['start1'] and u['start2']==t['start2'] and u['laenge']>t['laenge'] for u in treffer):
            maximal.append(t)
    return seq,sorted(maximal,key=lambda x:(-x['laenge'],x['luecke'],x['start1'],x['start2']))

def main():
    rows=list(csv.DictReader(CSV.open()))
    seq,hits=suchen(rows)
    best=max(h['laenge'] for h in hits) if hits else 0
    out={'definition':{'max_luecke':2,'normalisierung':'Ordnungszahlen/Beinamen entfernt; Frederik=Friedrich'},
         'n':len(rows),'sequenz':seq,'maximale_blocklaenge':best,'treffer':hits}
    p=ROOT/'outputs'/'daenemark_mustersuche.json'; p.write_text(json.dumps(out,ensure_ascii=False,indent=2))
    print('n=',len(rows),'maximale Blocklänge=',best)
    for h in hits:
        if h['laenge']<best: break
        a=rows[h['start1']]; b=rows[h['end1']]; c=rows[h['start2']]; d=rows[h['end2']]
        print(h['muster'],'L=',h['laenge'],'Lücke=',h['luecke'])
        print(' ',a['name_wikipedia'],'bis',b['name_wikipedia'],'|',c['name_wikipedia'],'bis',d['name_wikipedia'])

if __name__=='__main__': main()
