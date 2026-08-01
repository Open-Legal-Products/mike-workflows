---
name: "liq-anschluss-routing"
description: "When Anschluss-Routing in Liquiditätsplanung — Power is required: clarifies role, objective, deadline, documents, and the appropriate next specialist workflow; produces a directly usable work product with check points, risks, and next step."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Liq Anschluss Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Insolvency and Restructuring"
  jurisdictions: "Germany"
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Liquiditaetsplanung** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `ampel-zahlen-schwellenwerte-berechnung` — Ampel Zahlen Schwellenwerte Berechnung
- `ausgabengruppen-fristennotiz-naechster` — Ausgabengruppen Fristennotiz Naechster
- `ausgabengruppen-systematik` — Ausgabengruppen Systematik
- `bei-drohender-zahlungsunfaehigkeit` — bei Drohender Zahlungsunfaehigkeit
- `bei-eingetretener-zahlungsunfaehigkeit` — bei Eingetretener Zahlungsunfaehigkeit
- `cash-pooling-konzern` — Cash Pooling Konzern
- `chronologie-und-belegmatrix` — Chronologie und Belegmatrix
- `deutschem-dokumentationspaket-excel` — Deutschem Dokumentationspaket Excel
- `deutschem-tatbestandsmerkmale-beweisfragen` — Deutschem Tatbestandsmerkmale Beweisfragen
- `dokumentationspaket-bank` — Dokumentationspaket Bank
- `drohender-zahlungsunfaehigkeit` — Drohender Zahlungsunfaehigkeit
- `eingangsdaten-checkliste` — Eingangsdaten Checkliste
- `eingangsdaten-idw-s6-liqp` — Eingangsdaten IDW S6 Liqp
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Liquiditätsplanung und Insolvenzrecht-Schnittstelle-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (§ 15a InsO 3 Wochen (ZU) / 6 Wochen (Überschuldung), IDW S 11 12-Monats-Prognose, Drei-Wochen-Liquiditätsstockungs-Test (BGH II ZR 296/05)), notwendige Dokumente (Liquiditätsstatus, Finanzplan, Liquiditätsvorschau 3 Wochen / 3–6–12 Monate, Fortbestehensprognose, Sanierungsgutachten IDW S 6), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Geschäftsführer, Steuerberater, Wirtschaftsprüfer, Bank, IV/Restrukturierungsbeauftragter oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 266a StGB
- § 102 StaRUG
- § 1 StaRUG
- § 64 GmbHG
- § 8b KStG
- § 30 GmbHG
- § 31 StaRUG
- § 49 StaRUG
- § 43 GmbHG
- § 29 StaRUG
- § 29 VwVfG

### Leitentscheidungen

- BGH II ZR 296/05
- BGH IX ZR 129/22
- BGH II ZR 78/06
- BGH IX ZR 122/23
- BGH II ZR 206/22
