# Reproduktion

Benötigt Python 3 sowie pandas, lxml und beautifulsoup4. Aus dem Projektstamm:

```sh
PYTHONPATH=/path/to/dependencies python3 outputs/reproduktion/analyse.py
```

Der Lauf lädt die dokumentierten Referenzseiten erneut, verwendet Seed 20261029 und 200.000 Permutationen pro Liste. Für eine bitgenaue Prüfung des berichteten Stands dienen `data.json` und `results.json`; ein erneuter Webabruf kann sich durch spätere Seitenänderungen unterscheiden.
