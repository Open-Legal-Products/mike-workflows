---
name: "gr-anschluss-routing"
description: "Wenn es um Anschluss-Routing in Fachanwalt Gewerblicher Rechtsschutz geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Gr Anschluss Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Intellectual Property"
  jurisdictions: "Germany"
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Gewerblicher Rechtsschutz** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `abmahnung-formular-portal-und-einreichung` — Abmahnung Bezuege Designg
- `workflow-chronologie-und-belegmatrix` — Chronologie Belegmatrix Fristen Risikoampel
- `designeintragung-neuheit-paragraf-3-designg-eugh` — Designeintragung Neuheit Paragraf 3 Designg Eugh
- `designschutz-eu-gemeinschaftsgeschmacksmuster-eugh-c-419-13` — Designschutz EU Gemeinschaftsgeschmacksmuster Eugh C 419 13
- `designverletzung-fehlerkatalog` — Designverletzung Fehlerkatalog
- `designverletzung` — Designverletzung Marken Widerspruch
- `domainrecht-loeschung-bgh-i-zr-138-19` — Domainrecht Loeschung BGH I ZR 138 19
- `dpma-mehrparteien-konflikt-und-interessen` — Dpma Interessen Einstweilige Euipo
- `erstgespraech-mandatsannahme` — Erstgespraech Mandatsannahme Abmahnung UWG
- `eu-warenmarke-loeschung-eugh-c-541-18` — EU Warenmarke Loeschung Eugh C 541 18
- `einstieg-schnelltriage-fallrouting` — FA Gewerblicher RS GR Abmahnung Portfolio
- `erstpruefung-und-mandatsziel` — Fachanwalt FAO Gebrmg
- `workflow-redteam-qualitygate` — Faevvollzug Abschlussschreiben Lizenzanaloger
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Gewerblicher Rechtsschutz-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
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

- § 8c UWG
- § 14 MarkenG
- § 8 UWG
- § 12 UWG
- § 13 UWG
- § 5a UWG
- § 139 PatG
- § 42 DesignG
- § 42 MarkenG
- § 26 MarkenG
- § 2 DesignG
- § 24 MarkenG

### Leitentscheidungen

- EuGH C-541/18
- BGH II ZR 189/12
- BGH I ZR 138/19
- BGH I ZB 117/19
- BGH I ZR 167/19
