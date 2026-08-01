---
name: "zeugnisart-ausbildungszeugnis-16-bbig"
description: "Wenn es um Zeugnisart: Ausbildungszeugnis nach Paragraf 16 BBiG in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Zeugnisart Ausbildungszeugnis 16 Bbig"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Employment Law"
  jurisdictions: "Germany"
---

# Zeugnisart: Ausbildungszeugnis nach Paragraf 16 BBiG

## Ziel

Ein vollständiges Ausbildungszeugnis nach BBiG generieren, das die Besonderheiten des Ausbildungsverhältnisses berücksichtigt.

## Rechtsgrundlage

- Paragraf 16 Abs. 1 BBiG: Anspruch auf einfaches Zeugnis bei Beendigung des Berufsausbildungsverhältnisses.
- Paragraf 16 Abs. 2 BBiG: Qualifiziertes Zeugnis mit Angaben zu Verhalten und Leistung nur auf Verlangen.
- Elektronische Form nur mit Einwilligung der Auszubildenden und qualifizierter elektronischer Signatur (Paragraf 16 Abs. 1 BBiG seit 1.8.2024).

## Pflichtinhalt (einfaches Ausbildungszeugnis)

| Element | Pflicht |
|---|---|
| Name und Geburtsdatum | ja |
| Ausbildungsberuf | ja |
| Ausbildungszeitraum | ja |
| Wesentliche Ausbildungsinhalte/Fertigkeiten | ja |
| Beendigungssatz | ja |
| Unterschrift des Ausbildenden | ja |

## Zusätzlicher Inhalt (qualifiziertes Ausbildungszeugnis, auf Verlangen)

| Element |
|---|
| Lernfortschritt und fachliche Entwicklung |
| Berufsschulleistungen (bei dualer Ausbildung) |
| Verhalten gegenüber Ausbildern, Kollegen, Kunden |
| Engagement und Lernbereitschaft |

## Formulierungen für Lernfortschritt

### Sehr gut (Note 1)
> Herr/Frau [Name] hat die Ausbildungsinhalte stets schnell und sicher aufgenommen und zeigte großes Interesse an ihrem/seinem Ausbildungsberuf.

> Sie/Er zeichnete sich durch hervorragende Berufsschulleistungen aus.

### Gut (Note 2)
> Herr/Frau [Name] hat die Ausbildungsinhalte zuverlässig erworben und sicher angewendet.

> Ihre/Seine Leistungen in der Berufsschule waren gut.

### Befriedigend (Note 3)
> Herr/Frau [Name] hat sich die Ausbildungsinhalte erarbeitet und die Anforderungen erfüllt.

### Ausreichend/Mangelhaft (Note 4 bis 5)
> Herr/Frau [Name] war bereit, die Ausbildungsinhalte zu erlernen, und hat die Anforderungen im Wesentlichen erfüllt.

„War bereit zu erlernen" ist ein doppeltes Negativsignal — unterdurchschnittlicher Fortschritt.

## Azubi-Codes (Achtung beim Generieren)

| Formulierung | Bedeutung | Bewertung |
|---|---|---|
| „schnell und sicher aufgenommen" | hervorragender Lernfortschritt | gruen |
| „zuverlässig die Ausbildungsinhalte angeeignet" | guter Lernfortschritt | gruen |
| „hat sich die Inhalte erarbeitet" | befriedigender Fortschritt | orange |
| „war bereit zu erlernen" | unterdurchschnittlicher Fortschritt | rot |
| fehlender Berufsschulabschnitt (duale Ausbildung) | Schulprobleme möglich | orange |
| fehlende Pünktlichkeitsaussage | Fehlzeiten oder Verspätungen | orange |

## Triage-Checkliste

1. Abschlusszeugnis oder Zwischenzeugnis?
2. Duale Ausbildung — Berufsschulbewertung erforderlich?
3. Ausbildung abgebrochen — auch dann Anspruch auf Leistungs-/Verhaltensaussage auf Verlangen.
4. Beendigungsgrund: bestandene Prüfung oder Kündigung/Aufhebung?

## Besonderheit: Abgebrochene Ausbildung

Auch bei abgebrochener Ausbildung besteht Anspruch auf ein einfaches Zeugnis; qualifiziertes Zeugnis auf Verlangen. Beendigungsgrund (Kündigung, Aufhebung) neutral formulieren.

## Stolpersteine

- Berufsschulleistungen weglassen bei dualer Ausbildung — deren Fehlen ist ein Negativsignal.
- Azubi-Zeugnis mit demselben Template wie Führungskräfte-Zeugnis generieren — andere Terminologie, andere Maßstäbe.
- „positiv entwickelt" weglassen, obwohl es ein standardisierter Positivcode im Azubi-Bereich ist.

## Anti-Muster

- Qualifiziertes Ausbildungszeugnis erstellen, ohne dass der Auszubildende es verlangt hat.
- Berufsschulleistungen erfinden, wenn der Nutzer keine Angaben macht.
- Azubi-Zeugnis ohne Ausbildungsberuf und -zeitraum.

## Ausgabeformat

Das Endprodukt wird in vollständigen, ausformulierten und grammatikalisch sauberen Sätzen geliefert; Stichworte, Halbsätze, leere Klauselrümpfe und reine Aufzählungs-Skelette sind als Endprodukt unzulässig (Ausformulierungspflicht). Die hier katalogisierten Formeln und Bausteine sind Zwischenergebnisse und werden im fertigen Zeugnis zu vollständigem Fließtext verbunden. Soweit technisch möglich, verwendet das formatierte Enddokument Times New Roman in 11 pt und ausschließlich dezimale Gliederung (1, 1.1, 1.1.1); bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch ausdrücklich als Exporthinweis vermerkt.
