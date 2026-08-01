---
name: "mig-quellen-livecheck"
description: "When Rechtsquellen-Livecheck in Migration Law is required: organises facts, norm, burden of proof, counter-arguments, and next step; produces an interface map with conflict, jurisdiction, and evidence questions."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Mig Quellen Livecheck"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Migration Law"
  jurisdictions: "Germany"
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Fachanwalt Migrationsrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `abschiebehaft-paragraf-62-aufenthg` — Abschiebehaft Paragraf 62 Aufenthg
- `einstieg-schnelltriage-fallrouting` — Abschiebungsabwehr Sofort Arbeitgeber
- `arbeitgeberwechsel` — Arbeitgeberwechsel Asyl Anhoerung Asylg
- `asylantrag-folgeverfahren-paragraf-71-asylg` — Asylantrag Folgeverfahren Paragraf 71 Asylg
- `aufenthalt-paragraf-25a-aufenthg` — Aufenthalt Paragraf 25A Aufenthg
- `aufenthaltstitel-antrag` — Aufenthaltstitel
- `workflow-aufenthaltstitel-router` — Aufenthaltstitel Ausweisung Start
- `aufenthaltstitel-pruefung` — Aufenthaltstitel Erstgespraech Mandatsannahme
- `ausweisung-paragrafe-53-55-aufenthg` — Ausweisung Paragrafe 53 55 Aufenthg
- `ba-zustimmung-beschaeftigung` — BA Zustimmung Beschäftigungsduldung
- `blaue-karte-eu-mobilitaet` — Blaue Karte Bleiberecht 25A Chancenaufenthalt
- `workflow-botschaft-visumtermin` — Botschaft Visumtermin Dokumentenstapel
- `datenschutz-sicherheit-migration` — Datenschutz Sicherheit Daueraufenthalt EU
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Fachanwalt Migrationsrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
