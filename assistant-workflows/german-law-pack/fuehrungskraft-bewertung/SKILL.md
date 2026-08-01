---
name: "fuehrungskraft-bewertung"
description: "Wenn es um Führungskraft-Bewertung in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Fuehrungskraft Bewertung"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Employment Law"
  jurisdictions: "Germany"
---

# Führungskraft-Bewertung

## Ziel

Den Führungsabschnitt vollständig und mit der richtigen Notenstufe generieren. Ein Führungszeugnis ohne Führungsabschnitt ist unvollständig.

## Fünf Pflichtbausteine im Führungszeugnis

| Baustein | Fehlen bedeutet | Notenrelevanz |
|---|---|---|
| Mitarbeiterführung und -entwicklung | Führungsversagen | rot |
| Strategische Verantwortung | keine Strategiebeteiligung | orange bis rot |
| Budget- und P&L-Verantwortung | keine wirtschaftliche Führungsrolle | orange |
| Repräsentation nach außen | keine externe Wirkung | orange |
| Loyalitätsaussage gegenüber Gesellschaftern oder Vorstand | Loyalitätsproblem | rot |

## Formeln nach Note

### Note 1 — Führung
> Frau/Herr [Name] führte ihre/seine [Zahl] direkt unterstellten Mitarbeiterinnen und Mitarbeiter mit klarer Zielorientierung, hoher Wertschätzung und nachhaltigem Erfolg.

> Unter ihrer/seiner Leitung verzeichnete der Bereich eine Steigerung der Mitarbeiterzufriedenheit und eine signifikante Verbesserung der Ergebnisse.

> Frau/Herr [Name] genoss das vollste Vertrauen der Geschäftsführung.

### Note 2 — Führung
> Frau/Herr [Name] führte ihr/sein Team mit klarer Linie und hoher Anerkennung.

> Ihre/Seine Mitarbeiterinnen und Mitarbeiter schätzten ihren/seinen kooperativen und zielorientierten Führungsstil.

> Sie/Er hatte das Vertrauen der Unternehmensleitung.

### Note 3 — Führung
> Frau/Herr [Name] pflegte einen kooperativen Führungsstil und wurde von ihren/seinen Mitarbeitenden geschätzt.

> Sie/Er erzielte mit ihrem/seinem Team gute Ergebnisse.

„Erzielte mit seinem Team gute Ergebnisse" ohne Erfolgszahlen ist Note 3 — passiv, kein Erfolgsnachweis.

### Rote Formulierungen im Führungsabschnitt (vermeiden)

| Formulierung | Riskante Lesart | Note |
|---|---|---|
| „verstand es, sein Team zu motivieren" | allein nicht aussagekräftig | 3 |
| „setzte sich für die Belange seiner Mitarbeiter ein" | Loyalität ohne Fachkompetenz | 3 |
| „arbeitete eng mit seinem Team zusammen" | kein Führungsnachweis | 4 |

## Loyalitätsaussage

Führungskräfte auf Ebene Abteilungsleitung und höher brauchen eine explizite Loyalitätsaussage. Ohne sie entsteht ein Negativsignal.

**Note 1:**
> Frau/Herr [Name] genoss das vollste Vertrauen der Geschäftsführung und handelte stets im besten Interesse des Unternehmens.

**Note 2:**
> Sie/Er handelte stets loyal und im Einklang mit den Unternehmenszielen.

## Strategische Verantwortung

**Note 1:**
> Sie/Er war maßgeblich an der Entwicklung und Umsetzung der [Bereichs-/Unternehmens-]Strategie beteiligt.

**Note 2:**
> Frau/Herr [Name] brachte sich aktiv in strategische Entscheidungsprozesse ein.

## Stolpersteine

- Führungsabschnitt weglassen, weil der Nutzer die Funktion nicht als „Führungskraft" bezeichnet — ab zwei unterstellten Mitarbeitern ist ein Führungsabschnitt sinnvoll.
- Mitarbeiterzahl weglassen: „führte ein Team" ohne Zahl ist schwächer als „führte acht Mitarbeiterinnen und Mitarbeiter".
- Loyalitätsaussage weglassen bei Geschäftsführung oder Vorstand — das ist ein rotes Signal.

## Anti-Muster

- Führungsabschnitt komplett weglassen bei Leitungsfunktion.
- „verstand es zu motivieren" als Note-1-Führungsaussage verwenden.
- Erfolgsnachweis ohne Zahl oder Referenzpunkt (z.B. „steigerte die Effizienz" ohne messbare Bezugsgröße).

## Ausgabeformat

Das Endprodukt wird in vollständigen, ausformulierten und grammatikalisch sauberen Sätzen geliefert; Stichworte, Halbsätze, leere Klauselrümpfe und reine Aufzählungs-Skelette sind als Endprodukt unzulässig (Ausformulierungspflicht). Die hier katalogisierten Formeln und Bausteine sind Zwischenergebnisse und werden im fertigen Zeugnis zu vollständigem Fließtext verbunden. Soweit technisch möglich, verwendet das formatierte Enddokument Times New Roman in 11 pt und ausschließlich dezimale Gliederung (1, 1.1, 1.1.1); bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch ausdrücklich als Exporthinweis vermerkt.
