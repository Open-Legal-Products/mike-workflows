---
name: "vk-anschluss-routing"
description: "When Anschluss-Routing in Traffic Law is required: clarifies role, objective, deadline, documents, and the appropriate next specialist workflow; produces a directly usable work product with check points, risks, and next step."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Vk Anschluss Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Traffic Law"
  jurisdictions: "Germany"
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Verkehrsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `autonom-abschlussprodukt-und-uebergabe` — Autonom Bezuege Fachanwalt
- `blitzer-messung-paragraf-3-stvo` — Blitzer Messung Paragraf 3 Stvo
- `bussgeld-zahlen-schwellen-und-berechnung` — Bussgeld Unfall Haftungsquote VKR
- `dieselskandal-paragraf-826-bgb` — Dieselskandal Paragraf 826 BGB
- `erstgespraech-mandatsannahme` — Erstgespraech Mandatsannahme Verkehr Autonom
- `workflow-fristen-und-risikoampel` — FA Verkehrsrecht Fristen Risiko Mandant
- `fahrerlaubnis-entzug-paragraf-3-stvg` — Fahrerlaubnis Entzug Paragraf 3 Stvg
- `fahrerlaubnis-compliance-dokumentation-und-akte` — Fahrerlaubnis Kanzlei Personen
- `haftpflicht-paragraf-115-vvg` — Haftpflicht Paragraf 115 VVG
- `kaskoversicherung-paragraf-81-vvg-bgh-iv-zr-25-21` — Kaskoversicherung Paragraf 81 VVG BGH IV ZR 25 21
- `kfz-handel-paragraf-434-bgb` — KFZ Handel Paragraf 434 BGB
- `mandat-triage-sportrecht` — Mandat Triage Schriftsatzkern Substantiierung
- `mpu-vorbereitung` — MPU Vorbereitung Orientierung
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Verkehrsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
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

- § 67 OWiG
- § 69a StGB
- § 7 StVG
- § 18 StVG
- § 115 VVG
- § 69 StGB
- § 4 StVG
- § 33 OWiG
- § 24a StVG
- § 17 StVG
- § 55 OWiG
- § 26 StVG

### Leitentscheidungen

- BGH VI ZR 12/24
- BGH VI ZR 280/22
- BGH VI ZR 253/22
- BGH VI ZR 239/22
- BGH VI ZR 24/25
