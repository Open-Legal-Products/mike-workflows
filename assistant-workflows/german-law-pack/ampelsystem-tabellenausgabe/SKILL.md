---
name: "ampelsystem-tabellenausgabe"
description: "When Ampelsystem-Tabellenausgabe in Arbeitszeugnis-Analyse is required: checks deadline, form, jurisdiction, legal remedy, and immediate measures; produces a deadline and risk indicator with immediate action steps."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Ampelsystem Tabellenausgabe"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Employment Law"
  jurisdictions: "Germany"
---

# Ampelsystem-Tabellenausgabe

## Fachlicher Anker

- **Normen:** Paragrafen 611a, Paragrafen 1, Paragrafen 14.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Geheimcode-Regeln

| Element | Ampel-Zuordnung |
|---|---|
| Note 1-Formel vorhanden | Grün |
| Note 2-Formel vorhanden | Grün |
| Note 3-Formel vorhanden | Orange |
| Note 4-Formel vorhanden | Rot |
| Note 5-Formel vorhanden | Rot |
| Gemischter Satz (grün + orange) | Orange gesamt |
| Gemischter Satz (grün + rot) | Rot gesamt |
| Fehlende Pflichtaussage | Rot |

## Beispiele

**Beispiel 1 – Ausgabe für Note-1-Zeugnis:**

| Satz | Ampel | Bewertung | Notentendenz | Begründung |
|---|---|---|---|---|
| "stets zur vollsten Zufriedenheit" | Grün | Note 1 | Stabil | Vollständige Maximalformel |
| "stets einwandfrei" (Verhalten) | Grün | Note 1 | Stabil | Maximale Verhaltensformel |
| Vollständige Schlussformel | Grün | Note 1-2 | Stabil | Alle drei Elemente vorhanden |

**Beispiel 2 – Ausgabe für gemischtes Zeugnis:**

| Satz | Ampel | Bewertung | Notentendenz | Begründung |
|---|---|---|---|---|
| "zur vollen Zufriedenheit" | Orange | Note 3 | Abschwächend | Fehlendes "stets" |
| "bemüht" (Leistungsaussage) | Rot | Note 4 | Abwärts | Rotes Signal durch "bemüht" |
| Schlussformel ohne Bedauern | Orange | Note 3 | Abschwächend | Fehlendes Bedauern |

**Beispiel 3 – Gesamtzusammenfassung:** Grüne Sätze: 4 / Orange Sätze: 2 / Rote Sätze: 1 → Gewichtete Gesamtnote: Note 2 bis 3. Empfehlung: Nachverhandlung des roten Satzes und eines orangen Satzes sinnvoll.

## Rechtliche Einordnung und Normen

- **Paragraf 109 GewO** — Anspruch auf qualifiziertes Zeugnis; Wohlwollensgebot und Wahrheitspflicht
- **Paragraf 109 Abs. 2 GewO** — Zeugnis muss klar und verständlich formuliert sein; Codierungen, die Fortkommen erschweren, verstoßen gegen Wohlwollensgebot

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — vor der Tabellenausgabe klären

1. Welche Analyse-Skills wurden bereits ausgeführt? (Leistungsbeurteilung, Verhaltensbeurteilung, Schlussformel)
2. Liegt ein vollständiges Zeugnisdokument vor oder nur Auszüge?
3. Ist das Ziel: Mandantenbericht, Klageantrag-Vorbereitung oder interne Einschätzung?

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Paragraf 16 BBiG
- Paragraf 46 ArbGG
- Paragraf 1 KSchG
- Paragraf 7 KSchG
- Paragraf 102 BetrVG
- Paragraf 2 NachwG
- Paragraf 42 GKG
- Paragraf 29 VwVfG
- Paragraf 11 ArbGG
- Paragraf 13 BBiG

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)


## Ampel-Symbol-Disziplin

**Die Ampel wird grafisch gesetzt, nicht als Farbwort geschrieben.** In jeder Ausgabe gilt:

- 🔴 = Rot (Note 4-6, Negativcode, dringender Berichtigungspunkt)
- 🟠 = Orange (Note 3, Abschwaechung, Verhandlungspunkt) - bei Darstellungsproblemen: 🟡
- 🟢 = Gruen (Note 1-2, unbedenklich)

Regeln:

1. In Matrizen, Tabellen und Fliesstext immer das **farbige Ampelsymbol** setzen ("🔴"), nicht "Rot". Die Farbwoerter in internen Katalogtabellen sind Kodierung - in der Nutzerausgabe erscheinen Symbole.
2. In reiner ASCII-Umgebung ersatzweise `[ROT]`, `[ORANGE]`, `[GRUEN]` in Grossbuchstaben.
3. Im **Hauptbefund** zusaetzlich eine Ampel-Bilanz-Zeile ausgeben: `Ampel-Bilanz: 🔴 4 · 🟠 3 · 🟢 5`.
4. Mischbefunde als Doppelsymbol: 🟢🟠.
