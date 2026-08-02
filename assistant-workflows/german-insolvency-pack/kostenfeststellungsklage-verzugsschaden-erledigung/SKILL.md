---
name: "kostenfeststellungsklage-verzugsschaden-erledigung"
description: "When Kostenfeststellungsklage nach Zahlung auf die Forderung in Insolvency and Restructuring is required: drafts the appropriate document from facts, norm, evidence, and motion; produces a usable draft with motions, reasoning, and exhibit logic."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Kostenfeststellungsklage Verzugsschaden Erledigung"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Insolvency and Restructuring"
  jurisdictions: "Germany"
  source-plugin: "forderungsmanagement-klagewerkstatt"
---

# Kostenfeststellungsklage nach Zahlung auf die Forderung

## Einsatz im Forderungsmandat

Dieser Skill gehört in jede Zahlungsklage-Akte, sobald nach Klageeinreichung etwas passiert, das die Hauptforderung erledigt: Zahlung, Aufrechnung, Stundungseinwand, dauerhafte Einrede, Unmöglichkeit oder Wegfall des Rechtsschutzbedürfnisses. Dann geht es meist nur noch um Kosten. Genau hier darf die Klägerseite nicht automatisch die Klage zurücknehmen oder den Rechtsstreit für erledigt erklären.

Wenn der Schuldner bei Klageeinreichung in Verzug war, können die durch die Klageeinreichung entstandenen Kosten Rechtsverfolgungskosten und damit Verzugsschaden sein. Dann kommt eine Umstellung auf Feststellung der materiell-rechtlichen Kostenerstattungspflicht in Betracht.

## Normenanker

- Paragraf 91a ZPO — übereinstimmende Erledigung, Kosten nach billigem Ermessen.
- Paragraf 269 Abs. 3 Satz 3 ZPO — Kostenentscheidung, wenn der Anlass zur Klage vor Rechtshängigkeit wegfällt.
- Paragraf 263 ZPO — sachdienliche Klageänderung.
- Paragraf 264 Nr. 2 ZPO — zulässige Antragsumstellung ohne eigentliche Klageänderung.
- Paragraf 256 Abs. 1 ZPO — Feststellungsinteresse bei schwer bezifferbarer Kostenhöhe.
- Paragraf 261 Abs. 1 ZPO — Rechtshängigkeit erst mit Zustellung.
- Paragrafen 280 Abs. 1 und 2, 286 BGB — Verzögerungsschaden wegen Schuldnerverzugs.
- Paragraf 288 BGB — Verzugszinsen und B2B-Verzugspauschale; getrennt von den Prozesskosten behandeln.

## Entscheidungsanker

- BGH, Urteil vom 18.04.2013 - III ZR 156/12: Paragraf 269 Abs. 3 Satz 3 ZPO sperrt eine materiell-rechtliche Kostenerstattungsklage nicht; der Kläger hat ein Wahlrecht, wenn die Klage vor Rechtshängigkeit erledigt wird.
- BGH, Beschluss vom 13.12.2006 - XII ZB 71/04: Falsche Klagerücknahme nach Zahlung kann die Kostenlast kippen; Rechtshängigkeit ist die zentrale Weiche.
- BGH, Beschluss vom 11.01.2022 - VIII ZB 44/21: Materiell-rechtliche Kostenerstattung passt nicht beliebig in die Kostenentscheidung nach Paragraf 269 Abs. 3 Satz 2 ZPO.
- OLG Karlsruhe, Urteil vom 20.05.2026 - 7 U 173/25: Aktueller Anker für die Umstellung auf Feststellung der Kostenerstattungspflicht nach Erledigung vor Rechtshängigkeit; Fundstelle vor Schriftsatzverwendung live verifizieren.

## Arbeitsablauf

1. **Zahlung oder sonstige Erledigung buchen.**
   - Kontoauszug, Zahlungsavis, Aufrechnungsschreiben, Einrede oder sonstige Erklärung als Anlage sichern.
   - Zeitpunkt von Klageeingang, Gerichtskostenvorschuss, Zustellung und Zahlung in eine Minichronologie schreiben.

2. **Verzug beweisen.**
   - Mahnung, Fristablauf, kalendermäßige Fälligkeit oder endgültige Leistungsverweigerung belegen.
   - Ohne Verzug keine sichere materielle Kostenerstattung aus Paragrafen 280, 286 BGB.

3. **Erklärung wählen.**
   - Vor Rechtshängigkeit: Paragraf 269 Abs. 3 Satz 3 ZPO ist möglich, aber nicht zwingend; Kostenfeststellungsklage prüfen.
   - Nach Rechtshängigkeit: übereinstimmende oder einseitige Erledigung prüfen; materielle Kostenspur nur nach sorgfältigem Abgleich mit Streitstand und Rechtsprechung wählen.
   - Bei offener Beweisfrage kann die Kostenfeststellungsklage besser sein als eine summarische Kostenaufhebung.

4. **Antrag umstellen.**
   - Nicht nur "Kostenantrag" schreiben.
   - Feststellung ausdrücklich auf materiell-rechtlichen Ersatz der Rechtsverfolgungskosten als Verzugsschaden stützen.

## Muster: Antrag nach Zahlung vor Zustellung

```text
Der Klageantrag wird wie folgt umgestellt:

Es wird festgestellt, dass die Beklagte verpflichtet ist, der Klägerin die durch die Einreichung der Klage vom [Datum] entstandenen Kosten des Rechtsstreits als Verzugsschaden zu ersetzen.
```

## Muster: Begründung im Forderungsfall

```text
Die Beklagte befand sich bei Einreichung der Klage in Schuldnerverzug. Die Klägerin hatte die Beklagte mit Schreiben vom [Datum] unter Fristsetzung bis zum [Datum] zur Zahlung aufgefordert. Die Frist verstrich fruchtlos. Die Zahlung ging erst nach Klageeinreichung ein. Die Klage war daher durch das Verzugsverhalten der Beklagten veranlasst. Die durch die Klageeinreichung entstandenen Kosten sind notwendige Rechtsverfolgungskosten und nach Paragrafen 280 Abs. 1 und 2, 286 BGB zu ersetzen.
```

## Schnellcheck vor Versand

- [ ] Forderung war bei Klageeinreichung fällig.
- [ ] Schuldner war bei Klageeinreichung in Verzug.
- [ ] Zahlung oder erledigendes Ereignis ist nachweisbar datiert.
- [ ] Zustellungstag ist bekannt oder beim Gericht abgefragt.
- [ ] Keine vorschnelle Erledigungserklärung oder Klagerücknahme abgegeben.
- [ ] Antrag ist als materiell-rechtliche Feststellung formuliert.
- [ ] Risiko doppelter Kostengeltendmachung ist geprüft.
