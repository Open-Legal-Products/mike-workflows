---
name: "belastbarkeit-formeln"
description: "Wenn es um Belastbarkeit-Formeln in Arbeitszeugnisgenerator geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Belastbarkeit Formeln"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Employment Law"
  jurisdictions: "Germany"
---

# Belastbarkeit-Formeln

## Ziel

Belastbarkeitsaussagen mit der richtigen Notenstufe generieren und riskante Formulierungen vermeiden, die auf Krankheit oder Fehlzeiten hindeuten.

## Wann ist Belastbarkeit Pflicht?

Belastbarkeit muss erwähnt werden bei:
- Führungskräften
- Positionen mit regelmäßigen Deadlines oder Hochphasen
- Außendienst und Reisebereitschaft
- Schichtarbeit oder unregelmäßigen Arbeitszeiten
- Krisenrelevanten Positionen (Notaufnahme, IT-Support, Produktion)

Fehlt die Belastbarkeitsaussage bei diesen Positionen, wird das als Belastbarkeitsdefizit gelesen.

## Formeln nach Note

### Note 1 — Belastbarkeit
> Frau/Herr [Name] bewies auch in Phasen hoher Arbeitsbelastung stets Überblick, Ruhe und Entschlossenheit.

> Auch unter schwierigen Bedingungen war sie/er stets belastbar und lieferte konstant hervorragende Ergebnisse.

> Zeitdruck und komplexe Anforderungen meisterte sie/er souverän und ohne Qualitätseinbußen.

### Note 2 — Belastbarkeit
> Frau/Herr [Name] behielt auch in belastenden Situationen den Überblick und arbeitete verlässlich.

> Sie/Er war auch unter Druck stets zuverlässig und ergebnisorientiert.

### Note 3 — Belastbarkeit
> Frau/Herr [Name] zeigte sich den üblichen Belastungen gewachsen.

> Sie/Er erledigte auch in Hochphasen ihre/seine Aufgaben ordnungsgemäß.

„Den üblichen Belastungen gewachsen" ist Note 3 — mittelmäßig, aber nicht abwertend.

### Note 4 — Belastbarkeit
> Frau/Herr [Name] war mit den üblichen Belastungen vertraut.

„Mit den üblichen Belastungen vertraut" bedeutet: konnte sie nicht wirklich bewältigen — deutliches Negativsignal.

## Riskante Formulierungen (generieren vermeiden)

| Formulierung | Riskante Lesart | Bewertung |
|---|---|---|
| „war im Rahmen ihrer Anwesenheit engagiert" | riskante Fehlzeiten-Lesart | rot |
| „zeigte trotz ihrer Beeinträchtigungen Einsatzbereitschaft" | riskante Krankheits-/Belastbarkeitslesart | rot |
| „nutzte die ihr gegebenen Möglichkeiten" | riskante Krankenstands-Lesart | rot |
| „erledigte die Aufgaben zuverlässig, wenn sie anwesend war" | riskante Ausfallzeiten-Lesart | rot |
| „mit den üblichen Belastungen vertraut" | konnte sie nicht bewältigen | rot |

## Fehlzeiten und Krankheit

Krankheitsbedingte Fehlzeiten dürfen im Zeugnis nicht erwähnt werden — weder direkt noch durch kodierte Formulierungen. Der Generator darf keine Formulierungen erzeugen, die auf Krankheit oder Fehlzeiten hindeuten, auch wenn der Nutzer das explizit verlangt.

## Qualitätscheck vor Ausgabe

1. Ist Belastbarkeit für diese Position Pflicht?
2. Passt die Belastbarkeitsformel zur Gesamtnote?
3. Keine riskanten Krankheits- oder Fehlzeiten-Formulierungen?

## Stolpersteine

- „belastbar" ohne Kontextangabe ist schwach — immer mit Situation verknüpfen.
- Belastbarkeit weglassen bei einer Führungskraft, die regelmäßig unter Druck arbeitete.
- „trotz" in der Belastbarkeitsaussage: jedes „trotz" deutet auf eine Einschränkung hin.

## Anti-Muster

- Belastbarkeit bei Bürojob mit Routineaufgaben übertrieben loben — wirkt unglaubwürdig.
- Formulierungen, die indirekt auf hohe Fehlzeiten hinweisen.
- „war im Rahmen seiner Möglichkeiten belastbar" — Note 5, kein vertrauenserweckendes Signal.

## Ausgabeformat

Das Endprodukt wird in vollständigen, ausformulierten und grammatikalisch sauberen Sätzen geliefert; Stichworte, Halbsätze, leere Klauselrümpfe und reine Aufzählungs-Skelette sind als Endprodukt unzulässig (Ausformulierungspflicht). Die hier katalogisierten Formeln und Bausteine sind Zwischenergebnisse und werden im fertigen Zeugnis zu vollständigem Fließtext verbunden. Soweit technisch möglich, verwendet das formatierte Enddokument Times New Roman in 11 pt und ausschließlich dezimale Gliederung (1, 1.1, 1.1.1); bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch ausdrücklich als Exporthinweis vermerkt.
