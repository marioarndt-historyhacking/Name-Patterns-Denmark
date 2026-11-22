import csv, json, shutil
from pathlib import Path

W=Path(__file__).resolve().parent
O=W.parent/'outputs'; O.mkdir(exist_ok=True)
R=json.loads((W/'results.json').read_text()); D=json.loads((W/'data.json').read_text())
P=['FIXED','BOOKEND','PAIR_ECHO']

def f(x): return '—' if x is None else f'{x:.6f}'
def best(x,p):
    m=x['observed'][p]; hs=[h for h in x['hits'][p] if h['length']==m]
    if not hs: return 'kein Treffer', '—'
    h=hs[0]; ey=h['end']['end']; endpoint='offen (Stichtag 2026-10-29)' if ey is None else str(ey)
    return f"{h['start']['name']} → {h['end']['name']} (Länge {m})",endpoint

rows=[]
for land,x in R.items():
    if land=='HRR': continue
    for p in P:
        desc,end=best(x,p)
        rows.append([land,x['n'],p,x['observed'][p],desc,end,x['p_raw'][p],x['p_local'][p],x['p_global'][p],x['p_global'][p]<.05])
with (O/'vollstaendige_ergebnisse.csv').open('w',newline='') as z:
    w=csv.writer(z); w.writerow(['Liste','n','Muster','Maximallänge','Bestes_Fenster','Endzeitpunkt','p_roh','p_Holm_Land','p_Holm_global','global_signifikant']); w.writerows(rows)

lines=[]
lines += ['# Europäische Vergleichsstudie zu Namensmustern in Herrscherlisten','',
'**Stichtag:** 29. Oktober 2026  ','**Status:** methodisch eigenständige, reproduzierbare Vergleichsanalyse; Analyseprotokoll vor Ergebniseinsicht festgelegt.','',
'## Kurzbefund','',
'Unter elf unabhängigen europäischen Vergleichslisten war **kein Test nach globaler Holm-Korrektur signifikant**. Der stärkste Vergleichsbefund war die schottische FIXED-Folge James I–V (fünf aufeinanderfolgende Herrscher; roh p = 0,002725; landesintern Holm p = 0,008415; global Holm p = 0,089925). Sie ist damit ein auffälliger, aber europaweit nicht bestätigter Kandidat. Alle BOOKEND- und PAIR_ECHO-Tests blieben schon roh klar unsignifikant. Das HRR wurde planmäßig nur explorativ behandelt und liefert keine unabhängige Bestätigung. Russland zeigt den vorab erwarteten längeren Musterzeitraum deskriptiv (BOOKEND Ivan IV–Ivan VI, 1547–1741; 14 Herrscher), aber keinerlei statistische Evidenz (roh p = 0,988220).','',
'## Design','',
'Die Primäranalyse verwendet den ersten normalisierten Regnalnamen. Für jede Liste wurden automatisch alle zusammenhängenden Fenster enumeriert. FIXED verlangt mindestens drei identische Namen in Folge. BOOKEND verlangt denselben Namen nur an den beiden Rändern eines Fensters. PAIR_ECHO verlangt die Wiederholung desselben geordneten, aus zwei verschiedenen Namen bestehenden Paares am Anfang und Ende, ohne weitere Wiederholung dieses Paars dazwischen. Primäre Statistik ist jeweils die maximale Fensterlänge.','',
'Das Nullmodell permutiert die beobachteten Namen innerhalb jeder Liste und hält dadurch Listenlänge und Namenshäufigkeiten exakt konstant. Pro Liste wurden 200.000 Monte-Carlo-Permutationen mit Seed 20261029 gerechnet. Die drei p-Werte je Liste wurden mit Holm korrigiert; zusätzlich wurden alle 33 Primärtests der elf unabhängigen Vergleichslisten gemeinsam mit Holm korrigiert.','',
'## Vollständige Primärergebnisse','',
'| Liste | n | Muster | Maximum | bestes Fenster | Ende | p roh | p Holm Land | p Holm global |','|---|---:|---|---:|---|---|---:|---:|---:|']
for row in rows:
    land,n,p,m,desc,end,pr,pl,pg,sig=row
    lines.append(f'| {land} | {n} | {p} | {m} | {desc} | {end} | {f(pr)} | {f(pl)} | {f(pg)} |')

lines += ['','**Lesart der Nulltreffer:** Maximum 0 bedeutet, dass die definierte Musterklasse in der betreffenden Liste überhaupt nicht vorkam. Ein p-Wert von 1 ist dann definitionsgemäß gesetzt. Sämtliche nicht global signifikanten Zellen sind vollständige negative Ergebnisse, nicht ausgelassene Tests.','',
'## HRR: explorativer Ausgangsbefund, keine Replikation','',
'| Muster | Maximum | bestes Fenster | Ende | p roh | p Holm HRR |','|---|---:|---|---|---:|---:|']
x=R['HRR']
for p in P:
    desc,end=best(x,p); lines.append(f"| {p} | {x['observed'][p]} | {desc} | {end} | {f(x['p_raw'][p])} | {f(x['p_local'][p])} |")
lines += ['','Keiner der HRR-Werte ist nach der internen Drei-Test-Korrektur signifikant. Unabhängig davon darf das HRR wegen seiner Rolle als bereits explorierter Ausgangsbefund nicht in die Bestätigungszählung eingehen.','',
'## Endzeitpunkte der auffälligsten Muster','',
'- Schottland FIXED: James I bis James V; Ende 1542.','- England/Großbritannien FIXED: George I bis George IV; Ende 1830.','- Frankreich FIXED: Louis XIII bis Louis XVI; Ende 1792.','- Spanien FIXED: Philip II bis Philip IV; Ende 1665.','- Portugal FIXED: Philip I bis Philip III; Ende 1621.','- Schweden FIXED: Charles X bis Charles XII; Ende 1718.','- Russland BOOKEND: Ivan IV bis Ivan VI; Ende 1741.','- HRR FIXED (explorativ): Otto I bis Otto III; Ende 1002.','',
'## Russland als vorab benannte Ausnahme','',
'Russland wurde nicht mit einer günstigeren Suchregel analysiert. Die längere BOOKEND-Spanne (Ivan IV–Ivan VI) und PAIR_ECHO-Spanne (Peter I–Catherine II, acht Herrscher, Ende 1796; roh p = 0,221314) sind deskriptiv bemerkenswert, aber unter der konditionalen Permutationsnull nicht selten. Die Vorabbenennung verhindert daher eine nachträgliche Sonderhypothese; sie erzeugt keinen positiven Befund.','',
'## Datenbasis und Abweichungen','',
'Die maschinenlesbaren Reihen stammen aus den englischsprachigen Wikipedia-Herrscherlisten sowie, für England/Großbritannien, Frankreich, Spanien, Dänemark, Schottland, Russland und das HRR, aus dem offen zugänglichen kuratierten `dataset.json` des Projekts *European monarchy timeline*. Laufende Folgen wurden bis zum Stichtag ergänzt. Normalisierte Daten, Ergebnisse, Quellen-URLs und Code liegen im Reproduktionspaket.','',
'**Protokollabweichung:** Böhmen wurde vor der inferenzstatistischen Auswertung ausgeschlossen, weil die verfügbare Referenztabelle Herrscher von Teilgebieten und Regenten in eine nicht eindeutig lineare Folge mischt. Es wird deshalb nicht als negatives Ergebnis gezählt. Die vorab vorgesehenen Sensitivitätsanalysen nach Dynastie und Kalenderzeit konnten nicht belastbar gerechnet werden, weil die zusammengeführte Datenbasis keine einheitlich codierten Dynastien und für mehrere mittelalterliche Listen mehrdeutige Amtsdaten enthält. Diese Einschränkung schwächt die Robustheitsprüfung, verändert aber nicht die vollständige Berichterstattung der spezifizierten Primärtests.','',
'## Grenzen der Aussage','',
'Die Analyse testet Reihenfolge unter festgehaltenen Namenshäufigkeiten; sie erklärt keine dynastischen Namenskonventionen und ist kein populationsstatistisches Modell aller denkbaren europäischen Monarchien. Mittelalterliche Ko-Herrschaften und umstrittene Herrscher sind quellenabhängig. Weil lange BOOKEND- und PAIR_ECHO-Fenster bei häufig wiederkehrenden Namen unter der Permutationsnull oft entstehen, sind große deskriptive Fenster nicht automatisch starke Evidenz.','',
'## Reproduzierbarkeit und Quellen','',
'- Eingefrorenes Protokoll: `analyseprotokoll.md`','- Vollständige Testmatrix: `vollstaendige_ergebnisse.csv`','- Reproduktionspaket: `reproduktion/` (Code, normalisierte Daten, Ergebnisse und Quellen-URLs)','- M. Zemel, *A timeline of European monarchy using d3.js*, GitHub: https://github.com/mzemel/monarchs','- Wikipedia-Index der Monarchenlisten: https://en.wikipedia.org/wiki/Lists_of_monarchs','',
'## Schlussfolgerung','',
'Die europäische Vergleichsanalyse bestätigt kein robustes FIXED-, BOOKEND- oder PAIR_ECHO-Muster nach globaler Fehlerkontrolle. Schottlands James-I–V-Serie ist der einzige landesintern korrigierte Kandidat, verfehlt aber die globale Schwelle. Russland entspricht der vorab erwarteten langen deskriptiven Spanne, nicht jedoch einer statistischen Ausnahme. Das HRR bleibt ein explorierter Ausgangsfall und darf nicht als unabhängige Bestätigung interpretiert werden.']

(O/'studie.md').write_text('\n'.join(lines)+'\n')
shutil.copy2(W/'analyseprotokoll.md',O/'analyseprotokoll.md')
rep=O/'reproduktion'; rep.mkdir(exist_ok=True)
for name in ['analyse.py','data.json','results.json']:
    shutil.copy2(W/name,rep/name)
(rep/'source-monarchs').mkdir(exist_ok=True)
shutil.copy2(W/'source-monarchs'/'dataset.json',rep/'source-monarchs'/'dataset.json')
(rep/'README.md').write_text('''# Reproduktion\n\nBenötigt Python 3 sowie pandas, lxml und beautifulsoup4. Aus dem Projektstamm:\n\n```sh\nPYTHONPATH=/path/to/dependencies python3 outputs/reproduktion/analyse.py\n```\n\nDer Lauf lädt die dokumentierten Referenzseiten erneut, verwendet Seed 20261029 und 200.000 Permutationen pro Liste. Für eine bitgenaue Prüfung des berichteten Stands dienen `data.json` und `results.json`; ein erneuter Webabruf kann sich durch spätere Seitenänderungen unterscheiden.\n''')
print(O/'studie.md')
