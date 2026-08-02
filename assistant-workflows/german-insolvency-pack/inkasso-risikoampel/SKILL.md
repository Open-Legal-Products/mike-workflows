---
name: "inkasso-risikoampel"
description: "When Inkasso-Risikoampel in Insolvency and Restructuring is required: drafts the appropriate document from facts, norm, evidence, and motion; produces a deadline and risk indicator with immediate action steps."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Inkasso Risikoampel"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Insolvency and Restructuring"
  jurisdictions: "Germany"
  source-plugin: "forderungsmanagement-klagewerkstatt"
---

# Inkasso-Risikoampel

Vor Beauftragung von Klage und Vollstreckung lohnt ein Realitaetscheck.

## Faktorenmatrix

| Faktor | Indikator | Punkte |
|---|---|---|
| Schuldnertyp | Gewerbetreibender im Handelsregister | 0 |
| | Verbraucher mit festem Wohnsitz | 1 |
| | Verbraucher mit unbekannter Anschrift | 3 |
| Solvenz | Geschäftsbetrieb laeuft | 0 |
| | Schuldnerverzeichnis Eintrag | 2 |
| | Insolvenzantrag bekannt | 4 |
| Belegstand | vollstaendig | 0 |
| | luckenhaft | 2 |
| | nur Mandantenaussage | 4 |
| Verjährung | mehr als ein Jahr Rest | 0 |
| | unter drei Monaten | 2 |
| | eingetreten | 5 |
| Streitlage | unbestritten | 0 |
| | Bestreiten erwartet | 2 |
| | Gegenforderung bekannt | 3 |

## Auswertung

| Summe | Ampel | Empfehlung |
|---|---|---|
| 0 bis 2 | gruen | Klage oder Mahnbescheid |
| 3 bis 6 | gelb | erst Aussichtspruefung Belege Schuldnerauskunft |
| ab 7 | rot | Klage nur mit Mandanten-Risikohinweis oder Verzicht |

## Schuldnerverzeichnis ZPO 882b

Gläubigerin kann beim Vollstreckungsgericht eine Auskunft aus dem Schuldnerverzeichnis verlangen. Eintragungen entstehen u a nach Vermögensauskunft ZPO 802c oder Haftbefehl ZPO 802g.

## Insolvenzantrag durch Gläubiger InsO 14

Voraussetzung sind glaubhafte Forderung und Insolvenzgrund. Gebraucht in Druckverhaeltnissen aber Vorsicht wegen Anfechtbarkeit der Zahlung im Vorfeld.

## Norm-Pinpoints

- ZPO 802c 802g 882b
- InsO 14 17 19

## Quellen

- [ZPO 802c](https://www.gesetze-im-internet.de/zpo/__802c.html)
- [ZPO 882b](https://www.gesetze-im-internet.de/zpo/__882b.html)
- [InsO 14](https://www.gesetze-im-internet.de/inso/__14.html)
