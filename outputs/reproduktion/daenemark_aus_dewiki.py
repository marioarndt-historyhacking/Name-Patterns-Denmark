#!/usr/bin/env python3
"""Liest die historisch belegte dänische Königsfolge aus der deutschen Wikipedia."""
import csv, re
from pathlib import Path

from analyse import TABLES, choose_col, clean_text, fetch_tables, first_year, last_year

OUT=Path(__file__).resolve().parent.parent/'outputs'

def einzelne_namen(name):
    """Zerlegt nur Zellen, die erkennbar mehrere nummerierte Monarchen nennen."""
    if len(re.findall(r'\b[IVXLCDM]+\.',name)) < 2:
        return [name]
    return [x.strip() for x in re.split(r'\s*,\s*|\s+und\s+',name) if x.strip()]

def identitaet(name):
    """Personenschlüssel aus Regnalname und -nummer, ohne Beinamen."""
    m=re.match(r'^(.+?\b[IVXLCDM]+)\.',name)
    return re.sub(r'\s+',' ',m.group(1) if m else name).strip().casefold()

def lesen():
    tabellen,url=fetch_tables('Denmark')
    roh=[]
    for ti in TABLES['Denmark']:
        df=tabellen[ti]; nc=choose_col(df,'name'); rc=choose_col(df,'reign')
        for _,row in df.iterrows():
            name=clean_text(row[nc]); zeit=clean_text(row[rc])
            if not name or name.lower()=='nan' or name.lower()=='interregnum':
                continue
            # Lebensdaten stehen auf der deutschen Seite in derselben Zelle.
            anzeige=re.sub(r'\s*\([^()]*\)\s*$','',name).strip()
            beginn=first_year(zeit)
            ende=None if re.search(r'\bseit\b',zeit,re.I) else last_year(zeit)
            for einzelname in einzelne_namen(anzeige):
                roh.append({'name_wikipedia':einzelname,'regierungszeit':zeit,'beginn':beginn,'ende':ende,'quelltabelle':ti})
    # Nur ein Eintrag je Person, positioniert bei der ersten Königserhebung.
    # Spätere/fortgesetzte Amtszeiten erweitern lediglich die Zeitangabe.
    eintraege=[]; position={}
    for r in roh:
        key=identitaet(r['name_wikipedia'])
        if key not in position:
            position[key]=len(eintraege); eintraege.append(r)
        else:
            alt=eintraege[position[key]]
            alt['beginn']=min(x for x in [alt['beginn'],r['beginn']] if x is not None)
            if alt['ende'] is None or r['ende'] is None: alt['ende']=None
            else: alt['ende']=max(alt['ende'],r['ende'])
            alt['regierungszeit']=f"{alt['beginn']}–{alt['ende']}" if alt['ende'] is not None else f"seit {alt['beginn']}"
            alt['quelltabelle']=f"{alt['quelltabelle']},{r['quelltabelle']}"
    return url,eintraege

def main():
    url,e=lesen(); OUT.mkdir(exist_ok=True)
    with (OUT/'daenemark_dewiki.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=e[0].keys()); w.writeheader(); w.writerows(e)
    print(url)
    for i,r in enumerate(e,1): print(f"{i:02d}. {r['name_wikipedia']} — {r['regierungszeit']}")
    print(f"ANZAHL={len(e)}")

if __name__=='__main__': main()
