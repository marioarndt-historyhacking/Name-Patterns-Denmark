# Hypothesenprotokoll Dänemark v2

**Status:** explorative, nach Sichtung der dänischen Daten formulierte Hypothese. P-Werte für Dänemark sind selektionskorrigierte Evidenz innerhalb dieses Datensatzes, aber keine unabhängige Bestätigung. Eine Bestätigung erfordert Anwendung der unveränderten Regeln auf andere Herrscherlisten oder neue Daten.

## Datenfolge

- Beginn: Harald I. Blauzahn, Amtsantritt fest auf 958 gesetzt.
- Ein Eintrag je individuellem Herrscher, geordnet nach erster Königserhebung.
- Ko-Herrscher einzeln; spätere Amtszeiten derselben Person erzeugen keinen zweiten Eintrag.
- Regnalname ohne Ordnungszahl und Beiname; Hardiknut wird der Namensfamilie Knut zugeordnet.
- Amtsantrittsjahre sind die primären Kalenderkoordinaten. Für Knut II. wird 1018 als primärer Wert verwendet: Harald II. starb 1018, und 1018 gilt hier als die plausibelste bzw. vorherrschende Datierung. 1019 wird ausschließlich als Sensitivitätsvariante gerechnet. Sonstige unsichere Angaben werden primär mit dem festgelegten Hauptjahr und sensitiv mit einer Toleranz von ±1 bzw. den alternativen Jahren gerechnet.

## Hypothese H1: strukturierte Frühphase

Ab Harald I. existiert eine mehrere Jahrhunderte lange Phase, in der die Reihenfolge und die Kalenderpositionen wiederkehrender Regnalnamen stärker strukturiert sind als unter einer konditionalen Zufallspermutation derselben Namen.

Zwei primäre, allgemein formulierte Motivklassen werden automatisch gesucht:

1. **Periodische Rahmenkette:** mindestens drei nicht überlappende Fenster gleicher Herrscherzahl; jedes Fenster beginnt und endet mit demselben Regnalnamen; zwischen aufeinanderfolgenden Fenstern liegen höchstens zwei andere Herrscher; die Startjahre bilden mit ±1 Jahr Toleranz eine arithmetische Folge. Fensterlänge, Namen, Startpositionen und Kalenderabstand werden nicht vorgegeben.
2. **Zeitverschobenes Blockecho:** zwei identische Namensfolgen der Länge mindestens zwei, getrennt durch höchstens zwei Herrscher; die Amtsantrittsjahre korrespondierender Positionen unterscheiden sich um denselben Betrag mit ±1 Jahr Toleranz. Blocklänge, Namen, Positionen und Zeitverschiebung werden nicht vorgegeben.

Die beobachteten Ausprägungen (Achterfenster/122 Jahre und Sven–Harald–Knut/62 Jahre) sind Ergebnisse dieser allgemeinen Suchregeln, keine Eingabeparameter.

## Hypothese H2: Phasenwechsel und Nichtwiederkehr

Es existiert eine Grenze T im historisch plausiblen Suchbereich 1200–1450, nach der keine neue Instanz der beiden mittelalterlichen Motivklassen beginnt. T wird nicht am letzten Treffer festgesetzt, sondern durch eine über alle zulässigen Grenzen korrigierte Changepoint-Suche geschätzt.

- Ein Motiv wird zeitlich nach dem Amtsantritt seines ersten Herrschers zugeordnet.
- Vor T begonnene, aber nach T endende Fenster werden als **grenzüberschreitend** separat berichtet; sie gelten nicht als post-T neu entstanden.
- „Nie wieder“ bedeutet: keine neue Instanz bis zum Stichtag 2026-10-29, nicht eine Aussage über die Zukunft.
- Die dokumentierte Christian–Friedrich-Alternation ab 1513 ist ein bekannter dynastischer Namensmechanismus. Sie bleibt im Datensatz, wird aber separat modelliert und nicht als zufällige Anomalie derselben mittelalterlichen Motivklasse interpretiert.

## Nullmodell und Fehlerkontrolle

- Namen werden innerhalb der vollständigen Herrscherfolge permutiert; Namenshäufigkeiten, Herrscherzahl und Amtsantrittsjahre bleiben erhalten.
- Mindestens 200.000 Permutationen, Seed 20261029.
- In jeder Permutation werden Fensterlängen, Positionen, Kalenderabstände und mögliche Phasengrenzen erneut vollständig durchsucht.
- Berichtet werden motivspezifische, gemeinsame und changepoint-korrigierte p-Werte.

## Historische Grenzjahre

1329 ist das Ende der Herrschaft Waldemars III. und die Restauration Christophs II.; das eigentliche Interregnum beginnt nach Christophs Tod 1332. Beide Jahre werden historisch unterschieden. Die statistische Grenze wird nicht durch eine falsche Gleichsetzung von 1329 mit dem Beginn des Interregnums festgelegt.

## Vorab bekannte Prüfprobleme

1. Haralds Taufe wird häufig später als sein Amtsantritt datiert; „erster christlicher Herrscher“ bezeichnet hier die konventionelle historische Einordnung, nicht einen exakt 958 vollzogenen Glaubenswechsel.
2. Das Fenster Erik V.–Erik VII. beginnt vor 1329, endet aber danach. Seine Behandlung folgt der oben festgelegten Startregel und wird zusätzlich als grenzüberschreitend ausgewiesen.
3. Die zweite Phase enthält die historisch erklärte Christian–Friedrich-Konvention. Eine wörtliche Hypothese „überhaupt keine spätere Namensstruktur“ wäre deshalb falsch; geprüft wird die Nichtwiederkehr der definierten mittelalterlichen Motivklassen.
