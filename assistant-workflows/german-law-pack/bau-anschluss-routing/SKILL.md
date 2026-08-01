---
name: "bau-anschluss-routing"
description: "When Anschluss-Routing in Construction and Architects Law is required: clarifies role, objective, deadline, documents, and the appropriate next specialist workflow; produces a directly usable work product with check points, risks, and next step."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Bau Anschluss Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Construction and Architects Law"
  jurisdictions: "Germany"
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Bau Architektenrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abnahme-fiktion-paragraf-640-bgb-bgh-vii-zr-301-13` — Abnahme Fiktion Paragraf 640 BGB BGH VII ZR 301 13
- `abnahme-quellenkarte` — Abnahme Quellenkarte
- `architektenhonorar-hoai-mindestsatz-eugh-c-377-17` — Architektenhonorar HOAI Mindestsatz Eugh C 377 17
- `einstieg-schnelltriage-fallrouting` — BAU Abnahme Nachtrag
- `abnahme-verweigerung` — Bauablauf VBG
- `baugenehmigung-nachbarklage-paragraf-58-vwgo-bverwg-4-c-1-19` — Baugenehmigung Nachbarklage Paragraf 58 Vwgo Bverwg 4 C 1 19
- `bauordnungsrecht-behoerden-gericht-und-registerweg` — Bauordnungsrecht Einfuehrung Fachanwalt HOAI
- `bautraeger-abnahme-formgerecht-640-bgb` — Bautraeger Abnahme Formgerecht Abnahmefiktion
- `bautraeger-belehrungspflicht-17-beurkg` — Bautraeger Belehrungspflicht
- `bautraeger-gemeinschaftliche-maengelverfolgung-weg` — Bautraeger Gemeinschaftliche
- `bautraeger-leistungsbeschreibung-baubeschreibung` — Bautraeger Leistungsbeschreibung
- `bautraeger-mabv-grundlagen-1-2` — Bautraeger MABV Grundlagen Ratenplan
- `bautraeger-mabv-vollstaendigkeitserklaerung-7` — Bautraeger MABV Vollstaendigkeitserklaerung
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Bau Architektenrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
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

- § 4 BBodSchG
- § 24 BBodSchG
- § 17 BeurkG
- § 9 BBodSchG
- § 13 BBodSchG
- § 18 BBodSchG
- § 2 BBodSchG
- § 26 BBodSchG
- Art. 14 GG
- § 29 VwVfG
- § 22 RVG
- § 19 WEG

### Leitentscheidungen

- EuGH C-377/17
- BGH VII ZR 174/19
- BGH VII ZR 46/17
- BGH VII ZR 301/13
- BGH VII ZR 49/15
