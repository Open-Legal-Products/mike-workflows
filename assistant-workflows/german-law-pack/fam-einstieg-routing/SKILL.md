---
name: "fam-einstieg-routing"
description: "When Anwalts-Dashboard Fachanwalt Familienrecht in Family Law is required: clarifies role, objective, deadline, documents, and the appropriate next specialist workflow; produces a deadline and risk indicator with immediate action steps."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Fam Einstieg Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Family Law"
  jurisdictions: "Germany"
---

# Anwalts-Dashboard Fachanwalt Familienrecht

> Trennung, Unterhalt, Versorgungsausgleich, Sorge- und Umgangsrecht — meist Verbundverfahren, meist im Hintergrund das Kindeswohl.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | Keine 3-Wochen-Frist wie im ArbR, aber: Paragraf 1565 II BGB (Härtefall-Scheidung vor Trennungsjahr), Paragrafen 1666, 1666a BGB i. V. m. Paragraf 49 FamFG (Kindeswohlgefährdung — sofort), Paragraf 36 GewSchG (Gewaltschutz — sofortige Wirksamkeit). | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Scheidung Paragrafen 1564 ff. BGB · Trennungsunterhalt Paragraf 1361 BGB · Nachehelicher Unterhalt Paragrafen 1569 ff. BGB · Kindesunterhalt Paragrafen 1601 ff. BGB · Zugewinn Paragrafen 1372 ff. BGB · Versorgungsausgleich Paragrafen 1, 9 VersAusglG · Sorge Paragrafen 1671, 1684 BGB · Umgang Paragraf 1684 BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Familiengericht (Abt. AG) am Aufenthalt des Kindes oder gemeinsamen Wohnsitzes (Paragrafen 122, 152, 232 FamFG). Anwaltszwang in Ehesachen (Paragraf 114 FamFG). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Kindeswohlgefährdung: sofort Eilantrag (Paragraf 49 FamFG). 🔴 Häusliche Gewalt: Schutzanordnung Paragraf 1 GewSchG. 🟠 Trennungsjahr: Datum dokumentieren (Beweis!).
- **Beweislage:** 🟠 Trennungszeitpunkt — Indizien (Kontotrennung, Schlafzimmer, schriftliche Erklärung). 🔴 Sorgekonflikt: Beweismittel sorgsam (kein Aufschaukeln, Verfahrensbeistand respektieren).
- **Wirtschaftlich:** 🟠 Hohes Vermögen: Zugewinn parallel zur Scheidung (Verbund). 🔴 Drohende Verschiebung von Vermögen: Paragraf 1379 BGB Auskunft + Paragraf 1390 BGB Anfechtung.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Trennung — Trennungsjahr / Folgen** | `famr-trennungsjahr-praxis` | Trennungszeitpunkt dokumentieren, Trennungsunterhalt vorbereiten |
| Kindesunterhalt zu prüfen | `kindesunterhalt-mindestsatz-paragraf-1612a-bgb` | Mindestunterhalt, Düsseldorfer Tabelle, Mangelfall-Berechnung |
| Versorgungsausgleich offen | `famr-versorgungsausgleich-spezial` | Auskunftsverfahren VAB-Fragebogen, Halbteilung, Ausschluss |
| Gewaltschutz / Umgang in Konflikt | `gewaltschutz-und-umgang-schnittstelle` | GewSchG-Anordnung, Schnittstelle Umgang Paragraf 1684 BGB |
| Kindeswohlgefährdung — Eilantrag | `famr-kindeswohlgefaehrdung-eilantrag-spezial` | Eilantrag Paragraf 1666 BGB, Verfahrensbeistand, Jugendamt |

## Norm-Radar (live verifizieren)

- **Paragraf 1565 BGB** — Scheidungsvoraussetzung, Trennungsjahr
- **Paragraf 1361 BGB** — Trennungsunterhalt
- **Paragraf 1612a BGB** — Mindestkindesunterhalt
- **Paragraf 1666 BGB** — Maßnahmen bei Kindeswohlgefährdung
- **Paragraf 1684 BGB** — Umgangsrecht / Umgangspflicht
- **Paragraf 1 VersAusglG** — Halbteilungsgrundsatz

## Genau eine Rückfrage (nur wenn nötig)

> Geht es vorrangig um **Trennungs-/Scheidungsfolgen (Unterhalt, Zugewinn, VA)** oder um eine **akute Kindes- bzw. Gewaltschutz-Sache** (dann sofortiger Eilantrag)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Ehevertrag; Kernbereichslehre, Wirksamkeitskontrolle** — BGH XII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Wechselmodell; Anordnungsfähigkeit durch Familiengericht** — BGH XII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Kindeswohlgefährdung Paragraf 1666 BGB; Eingriffsschwelle** — BVerfG 1. Senat — *live verifizieren auf* `bundesverfassungsgericht.de`
- **Düsseldorfer Tabelle (Unterhalt; jährliche Aktualisierung)** — OLG Düsseldorf — *live verifizieren auf* `olg-duesseldorf.nrw.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.
