# Name-Patterns-Denmark

# Dänemark: historisch erklärte und mittelalterliche Namensmuster

## Berichtsregel für Christian–Friedrich

Die Christian–Friedrich-Abfolge ab 1513 wird künftig als **statistisch auffällige, aber historisch erklärte Regelmäßigkeit** geführt, nicht als unerklärte Anomalie. Die oldenburgischen und später glücksburgischen Königsnamen alternierten über Jahrhunderte; überwiegend entstand die Folge durch Vater-Sohn-Nachfolge und Benennung nach dem Großvater. Dynastische Seitenwechsel zeigen, dass die Konvention bewusst fortgeführt wurde.

## Mittelalterlicher Suchbefund

Für die mittelalterliche Teilanalyse wurde die Folge von Gorm dem Alten bis Johann I. (34 individuelle Herrscher) untersucht. In der vollständigen Zwei-Phasen-Analyse bleibt der Christian–Friedrich-Abschnitt im Datensatz und wird als eigener historischer Mechanismus modelliert. Ordnungszahlen und Beinamen wurden entfernt; Hardiknut wurde als Knut normalisiert.

Gefundene Maximalstruktur:

1. Sven I. Gabelbart → Harald II. Svendsen → Knut II. der Große
2. Zwischenkönige: Hardiknut → Magnus I.
3. Sven II. Estridsson → Harald III. Hen → Knut IV. der Heilige

Die maximale identische Blocklänge beträgt 3. Der zweite Block endet 1086.

## Signifikanz

Konditionaler Permutationstest mit 200.000 Neuanordnungen, Seed 20261029; in jeder Permutation wurde die vollständige Block- und Lückensuche wiederholt:

- beobachtete maximale Blocklänge: 3
- Permutationen mit mindestens ebenso langem Treffer: 7.876 von 200.000
- suchkorrigierter Roh-p-Wert: 0,0393848

Der Befund ist damit innerhalb dieser dänischen Mittelaltersuche auf dem 5%-Niveau signifikant. Er ist noch nicht über Länder und Musterklassen global korrigiert.

## Fünf Achterfenster mit gleichem Randnamen

Die vollständige Enumeration aller Fenster von exakt acht Königen ergibt **fünf** Treffer, bei denen Anfang und Ende denselben normalisierten Regnalnamen tragen:

1. Harald I. → … → Harald III. (Positionen 2–9; Ende 1080)
2. Knut IV. → … → Knut V. (Positionen 10–17; Ende 1157)
3. Erik II. → … → Erik IV. (Positionen 14–21; Ende 1250)
4. Waldemar II. → … → Waldemar III. (Positionen 20–27; Ende 1329)
5. Erik V. → … → Erik VII. (Positionen 24–31; Ende 1439)

Der dritte Treffer ist ein überlappendes Fenster und darf nicht durch eine starre Zerlegung der Liste in disjunkte Achtergruppen ersetzt werden. Dasselbe gilt für die Treffer 4 und 5.

Bei 200.000 konditionalen Permutationen der 34 mittelalterlichen Namen traten in 12.347 Permutationen mindestens fünf solche Achtfenster auf; der längenspezifische Wert ist p = 0,061740.

Die Fensterlänge wurde jedoch nicht vorausgesetzt. Eine automatische Suche über sämtliche Längen 2–34 findet als nominal stärksten Befund Länge 10, ebenfalls mit fünf gleichnamig gerahmten Fenstern (längenspezifisch p = 0,045790). Nach empirischer Min-p-Korrektur über alle geprüften Fensterlängen beträgt der p-Wert der gesamten automatischen Längensuche 0,569722. Weder die Achter- noch die Zehnerfenster sind damit ein bestätigender statistischer Befund; beide werden vollständig deskriptiv berichtet.

Die fünf Zehnerfenster sind: Knut IV.–Knut VI., Erik I.–Erik IV., Erik III.–Erik V., Waldemar I.–Waldemar III. und Christoph I.–Christoph III.

## Gleiche Startabstände und kalendarische Spannweiten

Unter allen gleichnamig gerahmten Fenstern ist die folgende Kombination einzigartig: Drei Fenster derselben Länge 8 beginnen bei Verwendung des jeweils frühesten Wikipedia-Jahres im Abstand von genau 122 Jahren:

- Harald I.–Harald III.: Beginn 958
- Knut IV.–Knut V.: Beginn 1080
- Waldemar II.–Waldemar III.: Beginn 1202

Es gibt keine weitere Dreiergruppe gleich langer Fenster mit arithmetisch gleichen Startabständen. Die Exaktheit ist jedoch quellenempfindlich, weil Haralds Regierungsbeginn als 958/64 angegeben wird. Bei Ansatz 964 wäre der erste Abstand 116 statt 122 Jahre.

Eine zweite Dreierübereinstimmung betrifft die kalendarische Spannweite. Drei Fenster der Länge 6 umfassen bei Verwendung der frühesten Jahresangaben jeweils 62 Jahre vom Amtsantritt des ersten bis zum Amtsantritt des letzten Randkönigs:

- Sven I.–Sven II.: 985–1047
- Harald II.–Harald III.: 1014–1076
- Knut II.–Knut IV.: 1018–1080

Auch diese Exaktheit ist wegen des als 1018/19 angegebenen Beginns Knuts II. nicht vollständig robust; bei Ansatz 1019 beträgt die dritte Spanne 61 Jahre.

Weitere identische kalendarische Spannweiten kommen nur paarweise vor: zweimal 45 Jahre und zweimal 164 Jahre. Weitere Dreiergruppen gleicher Spannweite gibt es nicht.

## Historische Erklärung

Die parallele Struktur ist genealogisch real:

- Nach Sven I. übernahm dessen Sohn Harald die dänische Krone. Der andere Sohn Knut führte zunächst das Heer in England und folgte nach Haralds Tod auch als König von Dänemark.
- Sven II. Estridsson war über seine Mutter Estrid ein Enkel Sven I. Gabelbarts und ein Neffe Knuts des Großen. Nach Sven II. wurde zunächst sein älterer Sohn Harald gewählt. Dessen Bruder Knut wurde nach Haralds Tod zum Nachfolger gewählt.

In beiden Fällen lautet die Struktur daher: **Vater Sven → Sohn Harald → Sohn Knut**. Die Wiederholung ist plausibel durch dynastische Wiederverwendung prestigeträchtiger Namen und die damalige Königswahl innerhalb des Königshauses bedingt. Dass Sven II. die Dreierfolge bewusst als vollständiges Schema kopieren wollte, ist durch die verwendeten Quellen nicht unmittelbar belegt und wird deshalb nicht behauptet.

## Kombinierter Namens- und Zeitbefund

Die Dreierblock-Wiederholung und die drei 62-Jahres-Fenster sind nicht getrennte Muster, sondern dieselbe Struktur in zwei Darstellungen:

| erster Block | Amtsantritt | zweiter Block | Amtsantritt | Verschiebung |
|---|---:|---|---:|---:|
| Sven I. | 985 | Sven II. | 1047 | +62 |
| Harald II. | 1014 | Harald III. | 1076 | +62 |
| Knut II. | 1018 | Knut IV. | 1080 | +62 |

Zwischen den beiden identischen Namensblöcken stehen Hardiknut und Magnus I. Die zweite Folge ist somit eine kalendarisch um 62 Jahre verschobene Wiederholung der ersten Folge.

Ein Permutationstest suchte automatisch über alle Blocklängen und 0–2 Zwischenkönige nach identischen Namensfolgen, bei denen die korrespondierenden Amtsantritte denselben Zeitversatz besitzen. Bei 200.000 Permutationen erreichten 95 mindestens die beobachtete Blocklänge 3; der vollständig suchkorrigierte p-Wert beträgt 0,000480. Mit einer Toleranz von einem Jahr für unsichere Datierungen erreichten 184 Permutationen den Befund; p = 0,000925.

Der kombinierte Befund ist damit wesentlich stärker als der reine Namenstest (p = 0,039385). Die exakte 62-Jahres-Angabe verwendet für Knut II. das früheste überlieferte Anfangsjahr 1018; bei 1019 lautet die dritte Verschiebung 61 Jahre, bleibt aber innerhalb der Einjahres-Sensitivitätsanalyse signifikant.

Für die Primäranalyse wird Knuts II. Amtsantritt verbindlich auf 1018 gesetzt. Harald II. starb 1018; die abweichende Angabe 1019 wird nur in der Sensitivitätsanalyse berücksichtigt und ändert die inhaltliche Schlussfolgerung nicht.

Auch die Amtsdauern wiederholen sich teilweise exakt auf Jahresniveau:

| erster Block | Amtsdauer | zweiter Block | Amtsdauer |
|---|---:|---|---:|
| Sven I. (985–1014) | 29 Jahre | Sven II. (1047–1076) | 29 Jahre |
| Harald II. (1014–1018) | 4 Jahre | Harald III. (1076–1080) | 4 Jahre |
| Knut II. (1018–1035) | 17 Jahre | Knut IV. (1080–1086) | 6 Jahre |

Damit stimmen bei den ersten beiden korrespondierenden Positionen nicht nur Namen, Reihenfolge und der 62-Jahres-Versatz, sondern auch die Amtsdauern überein. Die Knut-Amtszeiten unterscheiden sich. Die Dauern sind aus Jahresgrenzen berechnet und nicht als taggenaue Angaben zu verstehen.

## Vollständiger Vergleich namensgleicher Regierungsdauern

Die systematische Prüfung aller wiederkehrenden Königsnamen ergibt bis zur Arbeitsgrenze 1329 folgende Dauern. Berechnet wird jeweils `Endjahr − Anfangsjahr`; bei Christoph II. werden seine beiden getrennten Amtszeiten addiert. Es handelt sich somit um eine jahresgenaue, nicht taggenaue Prüfung.

| Name | Regierungsdauern in der Reihenfolge der Königserhebung | Exakte Wiederholung |
|---|---|---|
| Harald | Harald I. 27; Harald II. 4; Harald III. 4 | Harald II. = Harald III.: **4 Jahre** |
| Sven | Sven I. 29; Sven II. 29; Sven III. 11 | Sven I. = Sven II.: **29 Jahre** |
| Knut | Knut II. 17; Hardiknut/Knut III. 7; Knut IV. 6; Knut V. 11; Knut VI. 20 | keine |
| Erik | Erik I. 8; Erik II. 3; Erik III. 9; Erik IV. 9; Erik V. 27; Erik VI. 33 | Erik III. = Erik IV.: **9 Jahre** |
| Christoph | Christoph I. 7; Christoph II. 9 insgesamt | keine |
| Waldemar | Waldemar I. 28; Waldemar II. 39; Waldemar III. 3 | keine |

Damit existieren bis 1329 genau drei Paare namensgleicher Könige mit identischer, aus den Jahresgrenzen berechneter Regierungsdauer:

1. Sven I. und Sven II.: 29 Jahre.
2. Harald II. und Harald III.: 4 Jahre.
3. Erik III. und Erik IV.: 9 Jahre.

Nahe, aber nicht identische Werte sind Hardiknut/Knut III. mit 7 gegenüber Knut IV. mit 6 Jahren sowie Erik I. mit 8 gegenüber Erik III. und Erik IV. mit jeweils 9 Jahren.

In der späteren Periode gibt es nur eine weitere exakte Wiederholung innerhalb desselben Regnalnamens: Friedrich IV. (1699–1730) und Friedrich VI. (1808–1839) regierten nach dieser Jahresrechnung jeweils 31 Jahre. Unter den Christians gibt es keine identische Regierungsdauer. Die laufende Herrschaft Frederiks X. wird nicht verglichen.

Die Erik-Übereinstimmung ist von der Sven–Harald–Knut-Struktur zu trennen: Erik III. und Erik IV. stehen weder unmittelbar als korrespondierende Positionen in den beiden um 62 Jahre versetzten Blöcken noch besitzen ihre Amtsantritte denselben dort beobachteten Zeitversatz. Sie ist zunächst ein zusätzlicher deskriptiver Gleichstand, nicht automatisch ein weiterer Beleg für denselben Mechanismus.

## Kombinierte Gruppenregel: Regierungsdauer oder Jahresalter

Für den Zeitraum Harald I. bis Waldemar III. gibt es genau fünf Regnalnamen mit mindestens drei Königen. Tatsächlich erfüllt jede dieser fünf Gruppen dieselbe kombinierte Regel: Innerhalb der Gruppe existiert mindestens ein Paar mit entweder identischer Regierungsdauer oder höchstens einem Jahr Abweichung des Jahresalters. Regierungsdauer und Jahresalter werden ausschließlich aus Jahreszahlen berechnet; Tage und Monate bleiben unberücksichtigt.

| Namensgruppe | Zahl der Könige | qualifizierendes Paar | Übereinstimmung |
|---|---:|---|---|
| Harald | 3 | Harald II. / Harald III. | Regierungsdauer 4 / 4 Jahre |
| Sven | 3 | Sven I. / Sven II. | Regierungsdauer 29 / 29 Jahre |
| Knut | 5 | Knut II. / Knut VI. | Jahresalter 40 / 39–40 Jahre |
| Erik | 6 | Erik III. / Erik IV. | Regierungsdauer 9 / 9 Jahre |
| Erik | 6 | Erik II. / Erik V. | Jahresalter 37 / 37 Jahre |
| Waldemar | 3 | Waldemar I. / Waldemar III. | Jahresalter 51 / 50 Jahre |

Die beobachtete Aussage ist für den definierten Zeitraum somit vollständig erfüllt: **5 von 5** geeigneten Namensgruppen besitzen wenigstens ein solches Paar. Bei Knut VI. beruht das Intervall 39–40 auf dem Geburtsjahr 1162/63; die Regel bleibt bei beiden möglichen Jahren erfüllt.

Ein explorativer Permutationstest verteilte die vorhandenen Namensetiketten bei unveränderten Gruppengrößen 200.000-mal neu. In 2.355 Permutationen erfüllten ebenfalls alle fünf Gruppen die kombinierte Regel; dies entspricht p = 0,011780. Dieser Wert ist nicht bestätigend: Mindestgruppengröße, Einjahresschwelle und die ODER-Verknüpfung von Regierungsdauer und Lebensalter wurden erst nach Betrachtung der dänischen Daten formuliert. Außerdem bildet die einfache Permutation dynastische und zeitliche Abhängigkeiten nicht vollständig ab. Die Regel muss deshalb unverändert an weiteren Ländern geprüft werden.

### Paartrennung und nicht zugeordnete Könige

Verwendet man jeweils die belastbaren Hauptpaare — exakte Regierungsdauern sowie Jahresalter mit höchstens einem Jahr Abstand —, überschneiden sich die beiden Merkmale tatsächlich nicht: Kein Hauptpaar besitzt zugleich dieselbe Regierungsdauer und dasselbe beziehungsweise um höchstens ein Jahr abweichende Jahresalter.

| Namensgruppe | Paar über Regierungsdauer | Paar über Jahresalter | nicht durch diese Hauptpaare erfasst |
|---|---|---|---|
| Harald | Harald II. / Harald III. | – | **Harald I.** |
| Sven | Sven I. / Sven II. | – | **Sven III.** |
| Knut | Hardiknut/Knut III. / Knut IV. (7/6 Jahre; nur bei ±1-Regel) | Knut II. / Knut VI. | **Knut V.** |
| Erik | Erik III. / Erik IV. | Erik II. / Erik V. | **Erik I. und Erik VI.** |
| Waldemar | – | Waldemar I. / Waldemar III. | **Waldemar II.** |

Damit bleibt bei den Dreiergruppen Harald, Sven und Waldemar jeweils genau ein König außerhalb des Paares. Bei den fünf Knuts bilden sich zwei getrennte Paare und Knut V. bleibt übrig. Bei den sechs Eriks bleiben nach Auswahl der beiden belastbaren Hauptpaare dagegen **zwei**, nicht einer, übrig: Erik I. und Erik VI. Die allgemeinere Formulierung muss daher lauten: Es gibt keine Dreifachidentität desselben Zahlenwertes; nicht aber, dass in jeder Namensgruppe insgesamt genau ein König übrig bleibt.

Bei Erik III. ist die Geburtsangabe 1100–1105 zu ungenau für eine strikte Trennung aller denkbaren Paare. Sein mögliches Jahresalter 41–46 liegt höchstens ein Jahr von Erik I. mit 47 entfernt und umfasst Erik VI. mit 45. Zugleich liegen die Regierungsdauern Eriks I. mit 8 sowie Eriks III. und IV. mit je 9 Jahren höchstens ein Jahr auseinander. Werden alle bloß möglichen Intervalltreffer und eine ±1-Regel auch für Regierungsdauern zugelassen, entstehen daher bei Erik Überschneidungen. Die Aussage „in keinem Fall Überschneidung“ gilt nur für die robusten Hauptpaare, nicht für jede mathematisch mögliche Paarung.

Christoph passt als zusätzliche Zweiergruppe in die erweiterte ±1-Regel, wenn der Beobachtungszeitraum exakt mit dem Ende der Herrschaft Waldemars III. im Jahr 1329 abgeschnitten wird: Christoph I. regierte 1252–1259, also 7 Jahre; von Christoph II. zählt bis zu diesem Schnitt seine erste Herrschaft 1320–1326, also 6 Jahre. Seine Wiederherstellung 1329 trägt bei reiner Jahresdifferenz bis zum Schnittjahr noch null weitere Jahre bei. Christoph I. und II. bilden somit ein 7/6-Paar. Es handelt sich jedoch nur um zwei Christophs innerhalb des Zeitraums und daher nicht um einen Test der Regel für Namensgruppen mit mindestens drei Königen.

## Spätere Christian–Friedrich-Folge: auffällig, aber historisch erklärt

Die lange Alternation Christian–Friedrich ab 1513 ist statistisch hochgradig regelmäßig, gehört aber nicht zur unerklärten mittelalterlichen Motivklasse. Das dänische Standardlexikon und die Namensforschung der Universität Kopenhagen beschreiben ausdrücklich, dass die oldenburgischen und später glücksburgischen Königsnamen über Jahrhunderte zwischen Christian und Frederik wechselten.

Der Ausgangspunkt war zunächst keine einfache Vater-Sohn-Folge: Christian II. wurde 1523 abgesetzt und durch seinen Onkel Friedrich I. ersetzt. Danach stabilisierte sich die Alternation vor allem genealogisch. Von Friedrich I. bis Friedrich VI. verlief die Nachfolge weitgehend Vater–Sohn; die Benennung des Thronfolgers nach dem königlichen Großvater erzeugte automatisch Christian → Friedrich → Christian → Friedrich.

Dass es sich um eine bewusste dynastische Konvention und nicht nur um biologische Zufälligkeit handelt, zeigt ihre Fortführung über Seitenlinien und Dynastiewechsel hinweg. Christian VIII. war nicht der Sohn Friedrichs VI., sondern sein Cousin. Nach dem kinderlosen Tod Friedrichs VII. wechselte die Krone 1863 von der älteren Oldenburger Hauptlinie auf die Glücksburger Linie; dennoch folgten Christian IX., Friedrich VIII., Christian X. und Friedrich IX. Auf Friedrich IX. folgte durch die 1953 ermöglichte weibliche Thronfolge Margrethe II.; mit ihrem Sohn Frederik X. und dessen Sohn Kronprinz Christian ist die traditionelle Namensfolge wieder sichtbar.

Die Christian–Friedrich-Sequenz wird daher vollständig beschrieben und als statistisch auffällig ausgewiesen, aber kausal als dokumentierte dynastische Namensregel erklärt. Sie ist keine Evidenz für die hypothetische mittelalterliche Strukturierungsphase und wird nicht als spätere „Wiederkehr“ der dort definierten kalendergebundenen Rahmenketten oder Blockechos gewertet.

## Geburtsdaten, Todesdaten und Lebensalter bis 1329

Für die 26 Herrscher von Harald I. bis Waldemar III. wurden Geburts- und Todesjahre ergänzt. Bei 24 Herrschern ist daraus wenigstens ein Jahresalter ableitbar; bei Sven III. und Knut V. ist nur „vor 1120“ beziehungsweise „vor 1130“ bekannt, was für einen belastbaren Altersvergleich nicht genügt. Nach der festgelegten Konvention gilt ausschließlich `Todesjahr − Geburtsjahr`; Tage und Monate werden nicht berücksichtigt. Bei circa- und Doppeljahrangaben entsteht ein Intervall möglicher Jahreswerte.

Robuste oder nahezu robuste Altersübereinstimmungen innerhalb derselben Namensfamilie:

- Knut II.: 40 Jahre; Knut VI.: 39–40 Jahre.
- Erik II.: 37 Jahre; Erik V.: 37 Jahre.
- Waldemar I.: 51 Jahre; Waldemar III.: 50 Jahre.

Zwei weitere Nähebeziehungen betreffen Erik III., dessen Geburtsangabe 1100–1105 so breit ist, dass sie nur schwache Evidenz liefert: Erik I. liegt mit 47 Jahren ein Jahr über dem oberen möglichen Wert Eriks III. von 46 Jahren; das Intervall Eriks III. von 41–46 Jahren enthält außerdem die 45 Jahre Eriks VI.

Eine Permutation der Namensetiketten über die 24 verwendbaren Altersprofile ergab für drei überlappende Jahresaltersintervalle p = 0,190679. Beschränkt man sich auf die drei Paare mit höchstens einem Jahr Unterschied der Intervallmittelpunkte, ergibt sich p = 0,275199. Die Altersübereinstimmungen allein sind damit deskriptiv interessant, aber nicht statistisch signifikant.

Geburtsjahre, die mit früheren Thronbesteigungen zusammenfallen oder höchstens ein Jahr abweichen:

- Hardiknut, geboren 1018/19; Knut II. bestieg 1018 den Thron — exakte Intervallübereinstimmung.
- Harald III., geboren 1041; Magnus I. bestieg 1042 den Thron — ein Jahr Abstand.
- Knut IV., geboren ca. 1043; Magnus I. bestieg 1042 den Thron — ein Jahr Abstand.
- Erik III., geboren etwa 1100–1105; Niels bestieg 1104 den Thron — innerhalb des breiten Geburtsintervalls.
- Erik V., geboren ca. 1249; Abel bestieg 1250 den Thron — ein Jahr Abstand.

Für diese Geburtsjahr–Amtsantritt-Koinzidenzen wird noch kein p-Wert angegeben. Eine Permutation über Jahrhunderte würde Alters-, Generations- und Dynastiestrukturen zerstören; ein belastbarer Test benötigt ein eigenes demografisches Nullmodell für königliche Geburtsjahre.

## Quellen

- Deutsche Wikipedia: Liste der Könige Dänemarks
- Lex/Danmarkshistorien: *Vikingetiden, ca. 800–1050*
- Dansk Biografisk Leksikon/Lex: *Knud 2. den Store*
- Lex/Danmarkshistorien: *Knud den Hellige, ca. 1042–1086*
- Lex/Danmarkshistorien: *Svend Estridsen, ca. 1020–1074/76*
- Lex: *Danmarks kongehus*

## Zwei-Phasen-Hypothese: vorläufige Bewertung

Die präzisierte H1 wird durch zwei allgemein definierte, automatisch gesuchte Motive getragen:

1. Periodische Rahmenkette: Die Suche gab weder Länge 8 noch 122 Jahre vor. Der maximale Treffer ist die Kette Harald/Knut/Waldemar mit Fensterlänge 8 und Startschritt 122 Jahre; über Längen, Positionen, Lücken und Kalenderabstände korrigiert p = 0,013225.
2. Zeitverschobenes Blockecho: Die Suche gab weder Länge 3 noch 62 Jahre vor. Der maximale Treffer ist Sven–Harald–Knut mit zwei Zwischenkönigen und einer Zeitverschiebung von 62 Jahren; mit Einjahres-Toleranz und vollständiger Suchkorrektur p = 0,000925.

Ein gemeinsamer Permutationstest verlangte mindestens beide beobachteten Stärken. Drei von 200.000 Permutationen erfüllten dies; p = 0,000020. Dieser kombinierte Wert ist wegen der nach Sichtung Dänemarks ausgewählten Motivklassen explorativ und keine unabhängige Bestätigung.

Für H2 wurde als historisch motivierte Arbeitsgrenze das Ende der Herrschaft Waldemars III. 1329 verwendet; das eigentliche Interregnum begann 1332. Keine neue Instanz der beiden primären Motivklassen beginnt nach dieser Grenze. Das überlappende Achterfenster Erik V.–Erik VII. beginnt 1259, endet jedoch erst später und wird als grenzüberschreitend ausgewiesen.

Die Bedingung „keine neue starke Instanz nach 1329“ reduzierte die Zahl der gemeinsamen Nulltreffer nicht: alle drei Permutationen, die beide H1-Schwellen erreichten, hatten ebenfalls keinen post-1329 begonnenen starken Treffer. Die Nichtwiederkehr liefert damit in diesem Test keine von H1 unabhängige Signifikanz. Der genaue Changepoint ist aus den wenigen Motiven statistisch nicht eindeutig identifizierbar; 1329/1332 bleibt eine historisch plausible, aber nach Sichtung gewählte Grenze. H2 bedarf einer unverändert spezifizierten Prüfung in weiteren Herrscherlisten.
