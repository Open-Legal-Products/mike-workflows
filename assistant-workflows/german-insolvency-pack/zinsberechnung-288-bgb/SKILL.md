---
name: "zinsberechnung-288-bgb"
description: "When Zinsberechnung Paragraf 288 BGB in Insolvency and Restructuring is required: drafts the appropriate document from facts, norm, evidence, and motion; produces a usable draft with motions, reasoning, and exhibit logic."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Zinsberechnung 288 Bgb"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Insolvency and Restructuring"
  jurisdictions: "Germany"
  source-plugin: "forderungsmanagement-klagewerkstatt"
---

# Zinsberechnung Paragraf 288 BGB

Konkrete Berechnung von Verzugszinsen und der Pauschale nach Paragraf 288 BGB für den Klageantrag und die Forderungsaufstellung.

## Zinssaetze im Überblick

| Schuldner | Zinssatz | Norm |
|---|---|---|
| Verbraucher (B2C) | 5 Prozentpunkte über Basiszinssatz | Paragraf 288 Abs. 1 Satz 2 BGB |
| Unternehmer (B2B) | 9 Prozentpunkte über Basiszinssatz | Paragraf 288 Abs. 2 BGB |
| Entgeltforderungen B2B Pauschale | 40 EUR | Paragraf 288 Abs. 5 BGB |
| Prozesszinsen bei Klagezustellung | 5 / 9 Prozentpunkte | Paragraf 291 BGB i.V.m. Paragraf 288 BGB |
| Vertragliche Zinsen ab Faelligkeit (B2B) | Faelligkeitszinsen 5 % | Paragraf 353 HGB |

## Basiszinssatz Paragraf 247 BGB

Halbjaehrliche Anpassung durch Deutsche Bundesbank (jeweils zum 01.01. und 01.07.). Aktuelle und historische Werte:

| Periode | Basiszins |
|---|---|
| 01.01.2026 - 30.06.2026 | 1,27 % |
| 01.07.2025 - 31.12.2025 | 1,77 % |
| 01.01.2025 - 30.06.2025 | 2,27 % |
| 01.07.2024 - 31.12.2024 | 3,37 % |
| 01.01.2024 - 30.06.2024 | 3,62 % |
| 01.07.2023 - 31.12.2023 | 3,12 % |
| 01.01.2023 - 30.06.2023 | 1,62 % |
| 01.07.2016 - 30.06.2022 | -0,88 % |

Aktueller Basiszinssatz beim Gläubiger prüfen: [bundesbank.de/basiszinssatz](https://www.bundesbank.de/de/bundesbank/organisation/agb-und-regelungen/basiszinssatz-607820)

## Verzugseintritt Paragraf 286 BGB

Voraussetzungen Verzug:
1. **Faelligkeit** der Forderung (Paragraf 271 BGB, Paragraf 641 BGB, Paragraf 271a BGB).
2. **Moeglichkeit der Leistung** (kein Paragraf 275 BGB).
3. **Nichtleistung trotz Faelligkeit**.
4. **Mahnung** (Paragraf 286 Abs. 1 BGB) **oder** Entbehrlichkeit (Paragraf 286 Abs. 2 BGB) **oder** 30-Tage-Regel (Paragraf 286 Abs. 3 BGB).
5. **Vertretenmuessen** (Paragraf 286 Abs. 4 BGB) – Verschulden wird vermutet.

Entbehrlichkeit Paragraf 286 Abs. 2 BGB:
- Nr. 1: kalendermaessig bestimmte Leistungszeit (z.B. "Zahlung bis 15.04.2026").
- Nr. 2: kalendermaessig berechenbar nach Ereignis ("30 Tage nach Lieferung").
- Nr. 3: ernsthafte und endgueltige Leistungsverweigerung.
- Nr. 4: besondere Gruende unter Abwaegung beiderseitiger Interessen.

Paragraf 286 Abs. 3 BGB (B2B, Entgeltforderung): Verzug spaetestens 30 Tage nach Rechnungszugang ODER bei Verbraucher zusaetzlich Hinweis in Rechnung.

## Zinsberechnungsformel

```
Tage * Forderungsbetrag * (Basiszins + Aufschlag) / 36500
```

**Beispiel:** Hauptforderung 5.000 EUR, B2B, Verzug ab 15.04.2026, Klagezustellung 15.10.2026 (183 Tage).
- Basiszins ab 01.01.2026: 1,27 %
- Verzugszinssatz: 1,27 + 9 = 10,27 %
- Zinsen: 183 * 5000 * 0,1027 / 365 = 257,46 EUR

Bei Periodenwechsel (z.B. über den 01.07. hinaus): Aufteilen und separat rechnen.

## Verzugspauschale Paragraf 288 Abs. 5 BGB

- Gilt nur B2B-Entgeltforderungen.
- 40 EUR pro Forderung, **nicht** pro Mahnung.
- Auf Schadensersatz wegen Verzug (Mahnkosten, Rechtsverfolgungskosten) anzurechnen, soweit Schaden in Rechtsverfolgungskosten besteht (Paragraf 288 Abs. 5 Satz 3 BGB).
- BGH VIII ZR 232/16: Pauschale faellig auch ohne konkreten Schaden, nicht anrechenbar auf Anwaltskosten in einfach gelagerten Faellen.

## Hoehere Zinsen nach Paragraf 288 Abs. 3 BGB

Gläubiger kann hoehere Verzugszinsen nach anderem Rechtsgrund verlangen (z.B. vertraglich vereinbart, Paragraf 354 HGB, Paragraf 352 HGB), aber **kumulativ nur einmal**.

## Mahnkosten als Verzugsschaden Paragraf 280 Abs. 1, 2, Paragraf 286 BGB

- Erste Mahnung kostet **nichts** (selbst Verzug auslosend).
- Folgemahnungen: Schadensersatz für tatsaechliche Kosten (Porto, Material).
- Pauschale 2,50 EUR pro Mahnung in der Praxis akzeptiert (LG Berlin 32 O 188/95).
- Inkassokosten nur in Höhe einer 1,3 Geschäftsgebuehr eines Rechtsanwalts (Paragraf 4 Abs. 5 RDGEG).

## Klageantrag-Formulierung

```
Zinsen in Hoehe von 9 Prozentpunkten ueber dem jeweiligen
Basiszinssatz aus EUR 5.000,00 seit dem 15.04.2026
sowie eine Verzugspauschale in Hoehe von EUR 40,00.
```

Bei Verbraucher:
```
Zinsen in Hoehe von 5 Prozentpunkten ueber dem jeweiligen
Basiszinssatz aus EUR 1.250,00 seit dem 15.04.2026.
```

## Typische Fehler

- Verzugsbeginn ab Rechnungsdatum statt Faelligkeit + Mahnung.
- Bei Verbraucher Pauschale beantragt (falsch).
- "Zinsen aus" vergessen, dadurch unbestimmt.
- Periodenwechsel Basiszinssatz ignoriert.
- Vertragliche Faelligkeitszinsen Paragraf 353 HGB mit Verzugszinsen Paragraf 288 BGB doppelt.

## Quellen
- BGB Paragraf 247 Basiszinssatz [gesetze-im-internet.de/bgb/__247.html](https://www.gesetze-im-internet.de/bgb/__247.html)
- BGB Paragraf 286 Verzugseintritt [gesetze-im-internet.de/bgb/__286.html](https://www.gesetze-im-internet.de/bgb/__286.html)
- BGB Paragraf 288 Verzugszinsen [gesetze-im-internet.de/bgb/__288.html](https://www.gesetze-im-internet.de/bgb/__288.html)
- BGB Paragraf 291 Prozesszinsen [gesetze-im-internet.de/bgb/__291.html](https://www.gesetze-im-internet.de/bgb/__291.html)
- BGH VIII ZR 232/16 zur Pauschale [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
- Bundesbank Basiszinssatz [bundesbank.de](https://www.bundesbank.de/de/bundesbank/organisation/agb-und-regelungen/basiszinssatz-607820)
