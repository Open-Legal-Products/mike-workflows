---
name: "it-anschluss-routing"
description: "Wenn es um Anschluss-Routing in Fachanwalt It Recht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "It Anschluss Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "IT Law"
  jurisdictions: "Germany"
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt It Recht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `ai-act-art-6-hochrisiko-ki` — AI ACT ART 6 Hochrisiko KI
- `cloud-act-vs-dsgvo-art-48-dsgvo` — Cloud ACT VS DSGVO ART 48 DSGVO
- `vertragsstrafe-pruefen` — Cloud Vertrag Datenschutz ITR
- `cyber-vorfall-sofortmassnahmen` — Cyber Datenschutz
- `datenschutzrecht-fehlerkatalog` — Datenschutzrecht Fehlerkatalog
- `dma-compliance-dokumentation-und-akte` — DMA DSA DSGVO Fachanwalt Governance
- `dsv-dsfa-update-nach-vorfall` — Dsfa Update Erstgespraech Vorfallmeldung
- `dsgvo-bussgeld-art-83-eugh-c-807-21` — DSGVO Bussgeld ART 83 Eugh C 807 21
- `hacking-haftung-paragraf-823-bgb-it-sicherheit` — Hacking Haftung Paragraf 823 BGB IT Sicherheit
- `informationstechnologierecht-tatbestand-beweis` — Informationstechnologierecht Kanzlei
- `dsv-aufnahme-statusinformation` — IT Recht Aufnahme Statusinformation Benachrichtigung ART
- `dsv-massenbenachrichtigung` — IT Recht Massenbenachrichtigung Meldekette Auftragsverarbeiter
- `dsv-stakeholder-mapping` — IT Recht Stakeholder Mapping Tonfall Krisenkommunikation
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt It Recht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 33 DSGVO
- Art. 34 DSGVO
- Art. 9 DSGVO
- Art. 56 DSGVO
- Art. 32 DSGVO
- § 32 BSIG
- Art. 28 DSGVO
- Art. 82 DSGVO
- § 203 StGB
- Art. 55 DSGVO
- Art. 36 DSGVO
- § 8b BSIG

### Leitentscheidungen

- EuGH C-311/18
- EuGH C-300/21
- EuGH C-589/22
