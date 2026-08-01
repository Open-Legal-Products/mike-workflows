---
name: "vs-quellen-livecheck"
description: "When Rechtsquellen-Livecheck in Insurance Law is required: organises facts, norm, burden of proof, counter-arguments, and next step; produces an element-of-offence or claim matrix with counter-arguments."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Vs Quellen Livecheck"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Insurance Law"
  jurisdictions: "Germany"
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Fachanwalt Versicherungsrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `berufsunfaehigkeit-paragraf-172-vvg` — Berufsunfaehigkeit Paragraf 172 VVG
- `versr-bu-anerkennt-was-spezial` — BU Anerkennt Leistungspruefung
- `cyber-loesegeld-sanktionsrecht` — Cyber Loesegeld Versr Deckungsanfrage
- `versr-d-o-claims-made-ausschluesse` — D O Spezialfall Deckungsklage Leitfaden
- `deckungsklage-mehrparteien-konflikt-und-interessen` — Deckungsklage Interessen Deckungspruefung
- `versr-deckungsprozess-215-vvg-beweislast` — Deckungsprozess VVG Einfuehrung Themen
- `do-deckungsabwehr` — DO Deckungsabwehr Lebensversicherung
- `erstgespraech-mandatsannahme` — Erstgespraech Mandatsannahme
- `einstieg-schnelltriage-fallrouting` — FA Versicherungsrecht Start Chronologie Fristen
- `erstpruefung-und-mandatsziel` — Fachanwalt Kanzlei Krankenversicherung
- `fehlerkatalog` — Fehlerkatalog
- `gebaeudeversicherung-paragraf-86-vvg` — Gebaeudeversicherung Paragraf 86 VVG
- `haftpflicht-paragraf-100-vvg` — Haftpflicht Paragraf 100 VVG
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (VAG, VVG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Fachanwalt Versicherungsrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
