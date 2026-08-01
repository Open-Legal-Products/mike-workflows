---
name: "med-quellen-livecheck"
description: "When Rechtsquellen-Livecheck in Medical Law is required: checks deadline, form, jurisdiction, legal remedy, and immediate measures; produces a deadline and risk indicator with immediate action steps."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Med Quellen Livecheck"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Medical Law"
  jurisdictions: "Germany"
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Fachanwalt Medizinrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `aerzte-quellenkarte` — Aerzte Quellenkarte
- `aerztewerbung-innovative-therapie` — Aerztewerbung Innovative Amnog Millionen
- `anaesthesie-hochrisiko-aufklaerung` — Anaesthesie Hochrisiko Approbation Digitales
- `apothekenrecht-arzneimittel-paragraf-78-amg` — Apothekenrecht Arzneimittel Paragraf 78 AMG
- `apothekenrecht-mehrparteien-konflikt-und-interessen` — Apothekenrecht Interessen Aufklaerung
- `arzthaftung-aufklaerung-bgb` — Arzthaftung Aufklaerung BGB
- `atmp-chain-of-identity` — Atmp Chain Classification
- `atmp-pharmakovigilanz-rmp` — Atmp Pharmakovigilanz Aufklaerungsfehler
- `aufklaerungsfehler` — Aufklaerungsfehler Behandlungsfehler
- `aufklaerungspflicht-paragraf-630e-bgb` — Aufklaerungspflicht Paragraf 630e BGB
- `behandlungsfehler-paragraf-630h-bgb` — Behandlungsfehler Paragraf 630h BGB
- `berufsrecht-verhandlung-vergleich-und-eskalation` — Berufsrecht BGB Einwilligung Sonderfall
- `beweislast-hightech-medizin` — Beweislast Hightech Biobank Consent
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (BGB, MPDG, SGB V, §§ 630a ff) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Fachanwalt Medizinrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
