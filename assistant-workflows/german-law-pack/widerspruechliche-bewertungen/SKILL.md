---
name: "widerspruechliche-bewertungen"
description: "Wenn es um Widersprüchliche Bewertungen erkennen und kommentieren in Arbeitszeugnis-Analyse geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Widerspruechliche Bewertungen"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Employment Law"
  jurisdictions: "Germany"
---

# Widersprüchliche Bewertungen erkennen und kommentieren

## Fachlicher Anker

- **Normen:** Paragrafen 611a, Paragrafen 1, Paragrafen 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Widerspruchstyp | Signalwirkung | Ampel |
|---|---|---|
| Leistung grün, Schlussformel rot | Uneinvernehmliche Trennung | Orange-Rot |
| Verhalten grün, Leistung rot | Netter, aber leistungsschwacher Mitarbeiter | Rot |
| Eigeninitiative und "nach Anweisung" im selben Zeugnis | Inkonsistenz | Orange |
| Sehr warme Schlussformel bei schwacher Leistungsbeurteilung | Verdacht auf Gefälligkeitsformel | Orange |
| Positive Einzelsätze, negative Gesamtzufriedenheitsformel | Bewusste Irreführung | Rot |
| Spitzensatz und Durchschnittssatz im selben Themenbereich | Schaufenster-Pattern (siehe bereichs-drift-detektor) | Rot |

## Beispiele

**Beispiel 1 – Leistung grün, Schlussformel rot:** "Die Leistungen waren stets hervorragend" (Grün) + keine Schlussformel (Rot) → deutet auf Streit beim Ausscheiden oder feindseligen Abgang.

**Beispiel 2 – Innere Inkonsistenz:** "Herr Braun arbeitete stets eigenverantwortlich" (Satz 3) vs. "Er erledigte die ihm nach Anweisung zugewiesenen Aufgaben zuverlässig" (Satz 7) → direkte inhaltliche Contradiction.

**Beispiel 3 – Warme Schlussformel bei Note-4-Leistung:** Leistung mit "bemüht" (Rot, Note 4), Schlussformel vollständig und warm → vermutlich persönliches Gefälligkeitszeugnis, nicht authentisch.

**Beispiel 4 – Reihenfolge-Anomalie:** Abschnitt 1 (Leistung): hervorragend. Abschnitt 2 (Verhalten): Kollegen vor Vorgesetzten + "direkte Kommunikationsweise". Abschnitt 3 (Schlussformel): vollständig. → Einstellender wird Verhaltensteil isoliert bewerten.

**Beispiel 5 – Positiver Leistungsteil, fehlende Integrität:** Alle Leistungsaussagen grün, kein einziges Wort zu Zuverlässigkeit oder Vertrauen bei einem Buchhalter → der Widerspruch zwischen Lob und Schweigen ist das rote Signal.

## Rechtliche Einordnung und Normen

- **Paragraf 109 GewO** — Anspruch auf qualifiziertes wohlwollendes Zeugnis
- **Paragraf 109 Abs. 2 GewO** — Klarheits- und Wahrheitspflicht; kodierte Negativaussagen unzulässig

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


## Leitentscheidungs-Anker (Empfaengerhorizont, Grenzen der Decodierung)

> Diese Entscheidungen sind als Sucheinstieg gepflegt. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (`bundesarbeitsgericht.de`, `dejure.org`, Rechtsprechungsportal des Bundes) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung.

| Entscheidung | Tragende Aussage | Freie Quelle |
| --- | --- | --- |
| **BAG, Urt. v. 21.06.2005 - 9 AZR 352/04** | Gebot der Zeugnisklarheit ($ 109 II GewO): massgeblich ist der objektive Empfaengerhorizont, nicht die Absicht des Arbeitgebers. "Kennen gelernt" allein ist kein Geheimcode. | bundesarbeitsgericht.de / dejure.org |
| **BAG, Urt. v. 15.11.2011 - 9 AZR 386/10** | Bestaetigung: "kennen gelernt" ist allein und losgeloest vom uebrigen Zeugnisinhalt kein unzulaessiger Geheimcode; Werturteile-Spielraum mit Grenze Zeugniswahrheit/-klarheit. | bundesarbeitsgericht.de / dejure.org |

