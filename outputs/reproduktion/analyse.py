#!/usr/bin/env python3
import io, json, random, re, unicodedata, urllib.request
from collections import Counter
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent
UA = {"User-Agent": "Mozilla/5.0 (name-pattern-study/1.0; reproducible research)"}
PAGES = {
    "England/GB": "List_of_English_monarchs",
    "Britain": "List_of_British_monarchs",
    "France": "List_of_French_monarchs",
    "Spain": "List_of_Spanish_monarchs",
    "Portugal": "List_of_Portuguese_monarchs",
    "Denmark": "https://de.wikipedia.org/wiki/Liste_der_K%C3%B6nige_D%C3%A4nemarks",
    "Norway": "List_of_Norwegian_monarchs",
    "Sweden": "List_of_Swedish_monarchs",
    "Poland": "List_of_Polish_monarchs",
    "Hungary": "List_of_Hungarian_monarchs",
    "Bohemia": "List_of_Bohemian_monarchs",
    "Scotland": "List_of_Scottish_monarchs",
    "Russia": "List_of_Russian_monarchs",
    "HRR": "List_of_Holy_Roman_emperors",
}

TABLES = {
    "England/GB": list(range(3, 27)), "Britain": [0], "France": list(range(17)),
    "Spain": [1,2,3,4,5,6,7,9,13], "Portugal": [1,2,3,4],
    "Denmark": list(range(3,12)), "Norway": list(range(1,23)),
    "Sweden": list(range(1,12)), "Poland": list(range(3,11)),
    "Hungary": list(range(2,18)), "Bohemia": [3], "Scotland": list(range(1,11)),
    "Russia": list(range(1,14)), "HRR": list(range(1,19)),
}

def fetch_tables(label):
    url = PAGES[label] if PAGES[label].startswith("https://") else "https://en.wikipedia.org/wiki/" + PAGES[label]
    req = urllib.request.Request(url, headers=UA)
    raw = urllib.request.urlopen(req, timeout=60).read()
    (ROOT / "raw").mkdir(exist_ok=True)
    safe = "Liste_der_Koenige_Daenemarks" if label == "Denmark" else PAGES[label]
    (ROOT / "raw" / (safe + ".html")).write_bytes(raw)
    return pd.read_html(io.BytesIO(raw)), url

def flat_col(c):
    if isinstance(c, tuple): return " ".join(str(x) for x in c)
    return str(c)

def choose_col(df, kind):
    cols = list(df.columns)
    names = [flat_col(c).lower() for c in cols]
    if kind == "name":
        for i,s in enumerate(names):
            if "name" in s or "ruler" in s: return cols[i]
        return cols[0]
    for i,s in enumerate(names):
        if kind in s or (kind == "reign" and "regierungszeit" in s): return cols[i]
    return None

def clean_text(x):
    s = str(x).replace("\xa0", " ").replace("\u2009", " ")
    s = re.sub(r"\[[^]]*\]", "", s)
    return re.sub(r"\s+", " ", s).strip()

def first_year(s, default=None):
    ys = [int(x) for x in re.findall(r"(?<!\d)([789]\d\d|1\d{3}|20\d{2})(?!\d)", clean_text(s))]
    return ys[0] if ys else default

def last_year(s, default=None):
    ys = [int(x) for x in re.findall(r"(?<!\d)([789]\d\d|1\d{3}|20\d{2})(?!\d)", clean_text(s))]
    return ys[-1] if ys else default

ROMAN = r"[IVXLCDM]+"
PREFIX = re.compile(r"^(?:\([^)]*\)\s*)?(?:(?:King|Queen|Emperor|Empress|Tsar|Tsarina|Grand Duke|High Duke|Duke|Saint|Uncrowned)\s+)+", re.I)

def regnal_name(raw):
    s = clean_text(raw)
    s = PREFIX.sub("", s)
    s = re.sub(r"^(?:First|Second|Third) reign\s+", "", s, flags=re.I)
    s = re.sub(r"^(?:False)\s+", "", s, flags=re.I)
    # Stop at script/language duplicate, parenthesis, regnal number, epithet, or date.
    s = re.split(r"[А-Яа-я]|\(|\b(?:Spanish|Portuguese|Polish|Hungarian|English|Latin|Lithuanian):|\b"+ROMAN+r"\b|\bc?\.?\s*\d{3,4}\b|\d", s)[0]
    s = re.sub(r"\b(?:the|of|also|born|named|Saint)\b.*$", "", s, flags=re.I)
    s = re.sub(r"[^A-Za-zÀ-žÆæØøÐðÞþŁłŒœ' -]", "", s).strip(" -")
    # The first regnal forename is primary; preserve conventional hyphenated/double first names.
    return s.split()[0] if s else ""

def split_numbered_monarchs(raw):
    """Split a source row only when it visibly contains several regnal numbers."""
    if len(re.findall(r"\b[IVXLCDM]+\.",raw)) < 2: return [raw]
    return [x.strip() for x in re.split(r"\s*,\s*|\s+und\s+|\s+and\s+|\s*&\s*",raw) if x.strip()]

def monarch_identity(raw):
    m=re.match(r"^(.+?\b[IVXLCDM]+)\.",raw)
    return re.sub(r"\s+"," ",m.group(1) if m else raw).strip().casefold()

def extract():
    all_rows, sources = {}, {}
    cached = {}
    for label in PAGES:
        tables, url = fetch_tables(label); cached[label] = tables; sources[label] = url
        rows=[]
        for ti in TABLES[label]:
            df=tables[ti]; nc=choose_col(df,"name"); rc=choose_col(df,"reign")
            for _,r in df.iterrows():
                raw=clean_text(r[nc]); reign=clean_text(r[rc]) if rc is not None else raw
                whole=raw+" "+reign
                if raw.lower()=="nan" or not raw: continue
                if any(z in whole.lower() for z in ["anti-king","in opposition","title disputed","junior king","named his son","political affiliation"]): continue
                name=regnal_name(raw)
                if not name or name.lower() in {"name","ruler","nan"}: continue
                sy=first_year(reign); ey=None if re.search(r"\bseit\b",reign,re.I) else last_year(reign)
                rows.append({"raw":raw,"name":name,"start":sy,"end":ey,"table":ti})
        all_rows[label]=rows
    # Merge English sequence with the post-1707 British list, avoiding Anne duplication.
    eng=[r for r in all_rows["England/GB"] if r["name"]!="Anne"]
    brit=all_rows.pop("Britain")
    all_rows["England/GB"]=eng+brit
    sources["England/GB"] += "; " + sources.pop("Britain")
    # Denmark: one person per entry, ordered by first elevation. Repeated or
    # continued reigns enlarge the first entry instead of creating a duplicate.
    den=[]; denpos={}
    for r in all_rows["Denmark"]:
        for person in split_numbered_monarchs(r["raw"]):
            nr=dict(r); nr["raw"]=person; nr["name"]=regnal_name(person); key=monarch_identity(person)
            if key not in denpos:
                denpos[key]=len(den); den.append(nr)
            else:
                old=den[denpos[key]]
                starts=[x for x in (old["start"],nr["start"]) if x is not None]
                ends=[x for x in (old["end"],nr["end"]) if x is not None]
                old["start"]=min(starts) if starts else None
                old["end"]=max(ends) if ends and old["end"] is not None and nr["end"] is not None else None
    all_rows["Denmark"]=den
    # Rule-based removals of explicitly disputed/claimant rows not reliably encoded in columns.
    for label in list(all_rows):
        out=[]
        seen=set()
        for r in all_rows[label]:
            low=r["raw"].lower()
            if label=="England/GB" and any(x in low for x in ["edgar ætheling","louis the lion","empress matilda"]): continue
            if label=="Scotland" and "edward balliol" in low: continue
            if label=="Russia" and any(x in low for x in ["irina", "false dmitry", "michael aleksandrovich", "nicholas nikolaevich"]): continue
            if label=="Hungary" and "gabriel" in low: continue
            key=(r["raw"],r["start"],r["end"])
            if key in seen: continue
            seen.add(key); out.append(r)
        all_rows[label]=out
    # Use the separately curated, reign-level timeline where it covers a realm
    # comprehensively; this avoids parsing multi-row Wikipedia presentation tables.
    curated=json.loads((ROOT/"source-monarchs"/"dataset.json").read_text())
    cmap={"England/GB":"England","France":"France","Spain":"Spain",
          "Scotland":"Scotland","Russia":"Russia","HRR":"Holy Roman Empire"}
    for label,ckey in cmap.items():
        rr=[]
        for _,v in curated[ckey].items():
            rr.append({"raw":v["name"],"name":regnal_name(v["name"]),"start":v.get("start"),"end":v.get("end"),"table":"curated"})
        all_rows[label]=sorted(rr,key=lambda r:(r["start"] if r["start"] is not None else 99999,r["end"] or 99999))
        sources[label]="https://github.com/mzemel/monarchs (dataset.json; accessed 2026-10-29)"
    # Bring the two continuing curated sequences to the study cutoff.
    all_rows["England/GB"][-1]["end"]=2022
    all_rows["England/GB"].append({"raw":"Charles III","name":"Charles","start":2022,"end":None,"table":"current-update"})
    # Presentation-only rows and territorial subdivisions are not monarchs.
    bad={"Interregnum","Regency","Regencies","Earl","First","Second","Bohemia","Brno","Olomouc"}
    for label in list(all_rows): all_rows[label]=[r for r in all_rows[label] if r["name"] not in bad]
    # Within-list equivalence of translated/modernized spellings used by the source.
    maps={
      "Denmark":{},
      "Norway":{"Olav":"Olaf"},
      "Sweden":{"Gustaf":"Gustav","Carl":"Charles"},
      "Portugal":{"Luís":"Louis","BeatricePortuguese":"Beatrice","EdwardThe":"Edward"},
      "Russia":{"Olegthe":"Oleg","Vseslavthe":"Vseslav","Viacheslavof":"Viacheslav","Konstantinof":"Konstantin","MikhailKhorobrit":"Mikhail","AlexanderNevsky":"Alexander","Vasilyof":"Vasily","Dmitryof":"Dmitry","Dmitrythe":"Dmitry","DmitryDonskoyof":"Dmitry","Simeonthe":"Simeon","Vasilythe":"Vasily","Alexisthe":"Alexis"},
      "Spain":{"Joannathe":"Joanna"}
    }
    for label,mp in maps.items():
        for r in all_rows[label]: r["name"]=mp.get(r["name"],r["name"])
    # Bohemia's source table mixes rulers of territorial subdivisions and cannot
    # satisfy the pre-specified homogeneous-list criterion; retain raw evidence,
    # but exclude it from confirmatory testing and log the deviation.
    all_rows.pop("Bohemia")
    sources["Bohemia"] += " (excluded: table is not a single chronological crown sequence)"
    return all_rows,sources

def stats(seq):
    n=len(seq); fixed=1 if n else 0; run=1
    for i in range(1,n):
        run=run+1 if seq[i]==seq[i-1] else 1; fixed=max(fixed,run)
    fixed=fixed if fixed>=3 else 0
    last={}; book=0
    for i,x in enumerate(seq):
        if x in last: book=max(book,i-last[x]+1)
        last[x]=i
    book=book if book>=3 else 0
    lastp={}; pair=0
    for i in range(n-1):
        p=(seq[i],seq[i+1])
        if p[0]!=p[1] and p in lastp: pair=max(pair,i-lastp[p]+2)
        lastp[p]=i
    pair=pair if pair>=4 else 0
    return (fixed,book,pair)

def hits(rows):
    seq=[r["name"] for r in rows]; out={"FIXED":[],"BOOKEND":[],"PAIR_ECHO":[]}; n=len(seq)
    for s in range(n):
        for e in range(s+1,n):
            w=seq[s:e+1]
            if len(w)>=3 and len(set(w))==1: out["FIXED"].append((s,e))
            if len(w)>=3 and w[0]==w[-1] and w[0] not in w[1:-1]: out["BOOKEND"].append((s,e))
            if len(w)>=4 and w[0]!=w[1] and w[:2]==w[-2:] and all(w[i:i+2]!=w[:2] for i in range(1,len(w)-2)): out["PAIR_ECHO"].append((s,e))
    return out

def holm(ps):
    m=len(ps); order=sorted(range(m),key=lambda i:ps[i]); adj=[0.0]*m; prev=0
    for rank,i in enumerate(order):
        v=min(1.0,(m-rank)*ps[i]); prev=max(prev,v); adj[i]=prev
    return adj

def analyze(rows_by, B=200000):
    rng=random.Random(20261029); patterns=["FIXED","BOOKEND","PAIR_ECHO"]
    result={}
    for label,rows in rows_by.items():
        seq=[r["name"] for r in rows]; obs=stats(seq); exceed=[0,0,0]
        work=seq[:]
        for _ in range(B):
            rng.shuffle(work); st=stats(work)
            for j in range(3): exceed[j]+=st[j]>=obs[j]
        raw=[(x+1)/(B+1) if obs[j]>0 else 1.0 for j,x in enumerate(exceed)]
        local=holm(raw); hs=hits(rows)
        result[label]={"n":len(rows),"observed":dict(zip(patterns,obs)),"p_raw":dict(zip(patterns,raw)),"p_local":dict(zip(patterns,local)),"hits":{}}
        for p in patterns:
            result[label]["hits"][p]=[{"start_index":s,"end_index":e,"length":e-s+1,"start":rows[s],"end":rows[e],"names":seq[s:e+1]} for s,e in hs[p]]
    keys=[(l,p) for l in result if l!="HRR" for p in patterns]
    ga=holm([result[l]["p_raw"][p] for l,p in keys])
    for (l,p),v in zip(keys,ga): result[l].setdefault("p_global",{})[p]=v
    result["HRR"]["p_global"]={p:None for p in patterns}
    return result

def main():
    rows,sources=extract()
    (ROOT/"data.json").write_text(json.dumps({"sources":sources,"lists":rows},ensure_ascii=False,indent=2))
    res=analyze(rows)
    (ROOT/"results.json").write_text(json.dumps(res,ensure_ascii=False,indent=2))
    for l,x in res.items(): print(l,x["n"],x["observed"],x["p_raw"])

if __name__=="__main__": main()
