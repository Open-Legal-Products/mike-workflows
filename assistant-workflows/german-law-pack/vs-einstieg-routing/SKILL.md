---
name: "vs-einstieg-routing"
description: "When Anwalts-Dashboard Fachanwalt Versicherungsrecht in Insurance Law is required: clarifies role, objective, deadline, documents, and the appropriate next specialist workflow; produces a deadline and risk indicator with immediate action steps."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Vs Einstieg Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Insurance Law"
  jurisdictions: "Germany"
---

# Anwalts-Dashboard Fachanwalt Versicherungsrecht

> Leistungsablehnung, BU, D&O, Rechtsschutz, Obliegenheiten — Bedingungen prüfen, Obliegenheit prüfen, Beweislast verteilen.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 12 VVG: 1 Monat** (a. F.) ist überholt; Klagefrist gibt es nicht mehr. Aber: § 195 BGB Verjährung 3 Jahre. § 28 IV VVG: Obliegenheitsverletzung — Belehrungspflicht des Versicherers. § 19 VVG: Anzeigepflicht vorvertraglich; Rücktritt 1 Monat ab Kenntnis. § 14 VVG: Fälligkeit nach Erhebung der nötigen Erhebungen. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Versicherungsleistung aus jeweiligem Vertrag (BU, D&O, RS, Kasko, Haftpflicht, KH); §§ 1, 100, 115 VVG; § 86 VVG Regress; § 28 VVG Obliegenheitsverletzung; § 19 VVG Anzeigepflicht; § 215 VVG Gerichtsstand. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | § 215 VVG: Wohnsitz Versicherungsnehmer (zwingend für Verbraucher). Sonst §§ 12, 17 ZPO. Bei BU/PKV häufig LG (Streitwert). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🟠 Verjährung 3 Jahre ab Kenntnis (§ 199 BGB). 🔴 D&O Claims-made: Eintrittsdatum innerhalb Versicherungsperiode — Melde-Obliegenheit!
- **Beweislage:** 🔴 Obliegenheit § 28 VVG: Belehrungserfordernis und Kausalitätsgegenbeweis. 🟠 Anzeigepflicht § 19 VVG: Vorvertragliche Fragen Wortlaut konkret abgleichen.
- **Wirtschaftlich:** 🔴 BU-Anerkennung: Rückwirkung der Leistungspflicht bei verspäteter Anerkenntnis. 🟠 RS: Stichentscheid-/Schiedsgutachten.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **BU-Leistung verweigert** | `versr-bu-leistungspruefung-spezial` | Definition Beruf, Prognose 6 Monate, Verweisung, Anerkenntnisstrategie |
| D&O-Anspruch / Claims-made | `versr-d-und-o-spezialfall` | Versicherungsfall-Definition, Anzeigepflicht, Verteidigungskosten |
| Rechtsschutzdeckung verweigert | `versr-rechtsschutz-deckungsklage-spezial` | Deckungsklage § 3 ARB, Stichentscheid, vorvertraglich |
| Obliegenheitsverletzung Vorwurf | `versr-obliegenheitsverletzung-praxis` | Belehrungserfordernis § 28 IV VVG, Kausalitätsgegenbeweis |
| Anzeigepflicht § 19 VVG / Rücktritt | `versr-vvg-anzeigepflicht-19-arglist` | Frage-/Fragebogenklarheit, Arglist, Rücktritt 1 Monat |

## Norm-Radar (live verifizieren)

- **§ 1 VVG** — Hauptleistung des Versicherers
- **§ 19 VVG** — vorvertragliche Anzeigepflicht; Rücktritt
- **§ 28 VVG** — Obliegenheitsverletzung; Belehrungserfordernis
- **§ 100 VVG** — Haftpflichtversicherung: Versicherungsschutz
- **§ 115 VVG** — Direktanspruch gegen KH-Versicherer
- **§ 215 VVG** — Gerichtsstand am Wohnsitz VN

## Genau eine Rückfrage (nur wenn nötig)

> Welche **Sparte** (BU · D&O · KH/Haftpflicht · RS · Sachversicherung) — und welcher **Streitpunkt**: Deckung, Obliegenheit, Anzeigepflicht oder Höhe?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **BU-Anerkenntnis / Nachprüfung** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Anzeigepflicht § 19 VVG; Arglistanfechtung** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Obliegenheitsverletzung § 28 VVG; Belehrungserfordernis Abs. 4** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **D&O; Versicherungsfall (Claims-made)** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.
