# Vorab festgelegtes Analyseprotokoll

**Studie:** Europäische Vergleichsstudie zu Namensmustern in Herrscherlisten  
**Festgelegt:** 2026-10-29 (Asia/Bangkok), vor Abruf oder Einsicht in Vergleichsergebnisse  
**Status:** Eingefrorene Primärspezifikation; spätere Abweichungen werden separat ausgewiesen.

## 1. Fragestellung und Status der Fälle

Untersucht wird, ob die Abfolge der Regnalnamen europäischer Monarchen lokale Muster zeigt, die unter einer geeigneten Nullverteilung seltener als zufällig zu erwarten sind. Das Heilige Römische Reich (HRR) ist der bereits explorierte Ausgangsbefund und wird weder zur unabhängigen Bestätigung noch zur Schätzung einer europäischen Replikationsrate verwendet. Russland ist vor Einsicht in die Vergleichsergebnisse als mögliche Ausnahme mit längerem Musterzeitraum benannt.

## 2. Untersuchungseinheiten und Korpus

- Einheit ist eine chronologisch geordnete, institutionell möglichst homogene Herrscherliste eines europäischen Gemeinwesens.
- Primärkorpus: England/Großbritannien, Frankreich, Spanien, Portugal, Dänemark, Norwegen, Schweden, Polen, Ungarn, Böhmen, Schottland, Neapel/Sizilien und Russland; das HRR wird separat deskriptiv geführt.
- Beginn je Liste ist der erste in der verwendeten Referenzliste als Monarch des betreffenden Gemeinwesens geführte Herrscher; Ende ist Monarchieende bzw. 2026-10-29.
- Regenten, Gegenkönige, bloße Prätendenten und Interregna werden ausgeschlossen. Ko-Herrscher werden nur aufgenommen, wenn die Referenzliste sie in der Hauptchronologie als eigenständige Monarchen führt.
- Bei Personalunionen zählt jede institutionelle Liste separat. Dynastische oder territoriale Brüche werden dokumentiert, aber nicht nach Ergebnislage zugeschnitten.
- Analysevariable ist der normalisierte erste Regnalname: Ordnungszahlen, Beinamen, Titel, diakritische Zeichen und Sprachvarianten werden entfernt/vereinheitlicht; echte Doppelnamen bleiben als eigener Name erhalten, sofern sie als Regnalname geführt werden.

## 3. Primäre Musterdefinitionen

Für eine Namensfolge \(x_1,\dots,x_n\) und jedes zusammenhängende Fenster \([s,e]\) mit \(1\le s<e\le n\):

1. **FIXED:** Alle Namen im Fenster sind gleich. Mindestlänge 3.
2. **BOOKEND:** Erster und letzter Name sind gleich, alle inneren Namen unterscheiden sich vom Randnamen. Mindestlänge 3. Diese Definition misst eine echte Rückkehr und verhindert, dass FIXED automatisch BOOKEND ist.
3. **PAIR_ECHO:** Das geordnete Paar am Fensteranfang wird am Fensterende wiederholt: \((x_s,x_{s+1})=(x_{e-1},x_e)\), mit zwei verschiedenen Namen und ohne weitere Vorkommen desselben geordneten Paars innerhalb des Fensters. Mindestlänge 4.

Überlappende Treffer werden vollständig berichtet. Für jede Musterklasse und Liste ist der primäre Teststatistikwert das Maximum der Fensterlänge; Bindungen werden durch die früheste Startposition und dann den frühesten Endpunkt aufgelöst. Der **Endzeitpunkt** eines Treffers ist das Amtsende des letzten Herrschers im Fenster (bei amtierenden Monarchen: offen/rechtszensiert zum Stichtag).

## 4. Automatische Zeitraumsuche

Ein deterministisches Programm enumeriert sämtliche zusammenhängenden Fenster, prüft die drei Definitionen und speichert Startindex, Endindex, Namen, Herrscher, Jahre und Länge. Es gibt kein manuelles Verschieben von Grenzen. Russland erhält keine andere Suchregel; die Vorab-Ausnahme bedeutet nur, dass ein Treffer mit größerer zeitlicher Spannweite nicht nachträglich als überraschende Sonderhypothese ausgegeben wird.

## 5. Nullmodell und p-Werte

- Primäres Nullmodell: konditionale Zufallspermutation der beobachteten normalisierten Namen innerhalb jeder Landesliste. Damit bleiben Listenlänge und Namenshäufigkeiten exakt erhalten; getestet wird nur die Reihenfolge.
- Exakter Test, wenn höchstens 2.000.000 eindeutige Permutationen existieren; sonst mindestens 200.000 Monte-Carlo-Permutationen mit festem Seed 20261029.
- Der rohe p-Wert einer Musterklasse ist \((b+1)/(B+1)\), wobei \(b\) Permutationen einen mindestens so großen Maximalwert wie beobachtet haben. Fehlt ein Muster, wird der beobachtete Maximalwert 0 und p=1 gesetzt.
- **Länderspezifische Korrektur:** Holm-Korrektur über die drei Musterklassen innerhalb jeder Liste.
- **Globale Korrektur:** Holm-Korrektur über alle Primärtests aller unabhängigen Vergleichslisten. Das HRR ist davon ausgeschlossen und erhält nur explorative Werte.
- Alpha = 0,05, zweiseitige Formulierung wird nicht verwendet, da die Statistik gerichtet auf ungewöhnlich lange Muster ist.

## 6. Sensitivitätsanalysen

1. Dynastie-stratifizierte Permutation (Namen nur innerhalb dokumentierter Dynastien permutiert), sofern jede Liste ausreichend Variation enthält.
2. Zeitspanne in Kalenderjahren statt Anzahl der Herrscher als Teststatistik.
3. Ausschluss von Ko-Herrschern und umstrittenen Monarchen.
4. Separate Darstellung der russischen Gesamtliste und einer vorspezifizierten langen Periode vom ersten Zaren bis zum Monarchieende; keine zusätzliche Signifikanzbehauptung aus der Auswahl.

## 7. Berichtsstandard

Berichtet werden Korpus und Ausschlüsse, Normalisierungstabelle, Code und Seed, sämtliche Treffer, rohe sowie landes- und global korrigierte p-Werte, Endzeitpunkte, Sensitivitätsanalysen und **vollständige negative Ergebnisse** (jede Liste × jede Musterklasse). Effektbefund und statistische Evidenz werden getrennt formuliert. Fehlende oder mehrdeutige Daten werden nicht stillschweigend ersetzt.

## 8. Abweichungsregel

Jede nach diesem Zeitpunkt notwendige Änderung (Datenzugang, Listenabgrenzung, Definition oder Rechenverfahren) wird in einem Abweichungsprotokoll mit Grund und Einfluss auf die Interpretation dokumentiert; die ursprüngliche Spezifikation bleibt erhalten.
