---
name: "fa-ins-einstieg-routing"
description: "When Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht in Insolvency and Restructuring is required: clarifies role, objective, deadline, documents, and the appropriate next specialist workflow; produces a deadline and risk indicator with immediate action steps."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Fa Ins Einstieg Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Insolvency and Restructuring"
  jurisdictions: "Germany"
  source-plugin: "fachanwalt-insolvenz-sanierungsrecht"
---

# Anwalts-Dashboard Fachanwalt Insolvenz- und Sanierungsrecht

> Antragspflicht, Eigenverwaltung, Anfechtung, Restrukturierung — die 3-Wochen-Frist § 15a InsO ist der Taktgeber.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 15a I InsO: 3 Wochen** Insolvenzantragspflicht bei Zahlungsunfähigkeit / 6 Wochen bei Überschuldung (nach SanInsKG befristet). § 270b InsO: Schutzschirmverfahren — Antrag im Vorfeld der Insolvenz. § 174 InsO: Anmeldefrist Gläubiger nach öffentlicher Bekanntmachung. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Antragspflicht §§ 15a, 17 ff. InsO · Anfechtung §§ 129 ff. InsO · GF-Haftung § 64 GmbHG a. F. / § 15b InsO n. F. · Gläubigeranfechtung AnfG außerhalb Insolvenz · Schutzschirm § 270b InsO · Eigenverwaltung § 270 InsO · StaRUG (Stabilisierungs- und Restrukturierungsrahmen). | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Insolvenzgericht (AG am Sitz, § 3 InsO). Restrukturierungsgericht nach StaRUG = LG (§§ 30 ff. StaRUG). Anfechtungsklage gegen Gläubiger: LG/AG nach Streitwert. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 § 15a InsO: 3 Wochen ab Zahlungsunfähigkeit. Frist tickt taggenau — Kalender. 🟠 § 270b InsO: Vorbereitung vor Antrag in 4-8 Wochen.
- **Beweislage:** 🔴 Zahlungsunfähigkeit § 17 II InsO: 3-Wochen-Liquiditätsstatus. Buchhaltungs- und Bankkontodaten sichern. 🟠 Überschuldung § 19 II InsO: Fortbestehensprognose dokumentieren.
- **Wirtschaftlich:** 🔴 Geschäftsführerhaftung § 15b InsO (Zahlungen nach Insolvenzreife) — sofort einstellen. 🟠 Anfechtungsangriff in 4 Jahren (§ 133 InsO 10 Jahre Vorsatzanfechtung).

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| Fortbestehensprognose anwerfen | `insanw-fortbestehensprognose-workflow` | Liquiditätsplan 12 Monate, IDW S 11, Beweisdokument |
| Eigenverwaltung / Schutzschirm § 270b | `insanw-eigenverwaltung-schutzschirm-spezial` | Antragsfähigkeit, Bescheinigung, Sachwalter |
| **Antragspflicht § 15a InsO** | `inso-p015a-antragspflicht-bei-juristischen-personen-und-rechtsfa` | 3-Wochen-Frist, GF-Haftung, Strafrecht § 15a IV InsO |
| Anfechtungsmandat (Gläubiger / Verwalter) | `insanw-anfechtungsmandat-leitfaden` | Tatbestände §§ 129 ff. InsO, Verteidigungsstrategie |
| Konzerninsolvenz / Gruppenkoordination | `insanw-konzerninsolvenz-koordination-spezial` | Gruppen-Gerichtsstand § 3a InsO, Koordinationsverfahren |

## Norm-Radar (live verifizieren)

- **§ 15a InsO** — Insolvenzantragspflicht — 3 Wochen / 6 Wochen
- **§ 17 InsO** — Zahlungsunfähigkeit
- **§ 19 InsO** — Überschuldung
- **§ 270 InsO** — Eigenverwaltung; § 270b Schutzschirm
- **§ 133 InsO** — Vorsatzanfechtung; 10-Jahres-Zeitraum
- **§ 15b InsO** — Zahlungsverbot nach Insolvenzreife

## Genau eine Rückfrage (nur wenn nötig)

> Stehen wir **vor** der Antragstellung (Beratung GF / Sanierung) oder **nach** Verfahrenseröffnung (Verwalter, Gläubiger, Anfechtung)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Verwerterpflichten; höchstmögliche Erlöserzielung** — BGH IX. Zivilsenat (Linie IX ZR 169/04 v. 13.04.2006, fortgeführt) — *live verifizieren auf* `bundesgerichtshof.de`
- **Vorsatzanfechtung § 133 InsO; Bargeschäfts-Ausnahme** — BGH IX. Zivilsenat (Linienwandel ab 2021) — *live verifizieren auf* `bundesgerichtshof.de`
- **Insolvenzantragspflicht § 15a InsO; § 15b InsO Zahlungsverbot** — BGH II./IX. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Geschäftsveräußerung im Ganzen § 1 Ia UStG** — EuGH C-497/01 (Zita Modes); EuGH C-444/10 (Schriever); BFH — *live verifizieren auf* `curia.europa.eu + bfh.bund.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.
