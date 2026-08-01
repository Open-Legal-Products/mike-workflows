---
name: "erb-einstieg-routing"
description: "Wenn es um Anwalts-Dashboard Fachanwalt Erbrecht in Fachanwalt Erbrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Erb Einstieg Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Inheritance Law"
  jurisdictions: "Germany"
---

# Anwalts-Dashboard Fachanwalt Erbrecht

> Erbfall, Pflichtteil, Erbschein, Erbengemeinschaft, Testament — Ausschlagungsfrist tickt ab Kenntnis. Wer beerbt wen, wann?
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 1944 BGB: 6 Wochen** Ausschlagung ab Kenntnis von Anfall und Berufungsgrund (6 Monate bei Auslandsbezug). § 1954 BGB: Anfechtung der Annahme/Ausschlagung 6 Wochen. § 2306 BGB: Ausschlagungsrecht bei Beschwerung 6 Wochen. § 2082 BGB: Anfechtung Testament 1 Jahr ab Kenntnis. § 2332 BGB: Pflichtteils-Verjährung 3 Jahre. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Erbe §§ 1922, 1942 BGB · Pflichtteil §§ 2303 ff. BGB · Pflichtteilsergänzung §§ 2325 ff. BGB · Auskunft § 2314 BGB · Auseinandersetzung §§ 2042 ff. BGB · Erbschein §§ 2353 ff. BGB · Vermächtnis §§ 2147 ff. BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Nachlassgericht am letzten gewöhnlichen Aufenthalt (§ 343 FamFG). Streitige Erbsachen: LG/AG nach Streitwert (§ 27 ZPO). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Ausschlagungsfrist 6 Wochen läuft ab Kenntnis; Akten dokumentieren. 🟠 Pflichtteilsergänzung (10-Jahresfrist § 2325 III BGB) und Pflichtteils-Verjährung (3 Jahre) gegen Schenkungen verfolgen.
- **Beweislage:** 🟠 Pflichtteils-Auskunft § 2314 BGB lückenhaft → notarielles Verzeichnis erzwingen. 🔴 Testament: Testierfähigkeit Beweis (medizinische Akten, Zeugen, ggf. Sachverständige).
- **Wirtschaftlich:** 🔴 Nachlassinsolvenz droht → § 1980 BGB Antrag (binnen 3 Monaten), Erbenhaftungsbeschränkung. 🟠 Hoher Nachlasswert: Pflichtteilsanspruch parallel zu Auseinandersetzung.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Pflichtteil berechnen / geltend machen** | `pflichtteil-berechnen` | Pflichtteilsquote, Wertermittlung, Auskunftsverfahren § 2314 BGB |
| Ausschlagung der Erbschaft | `erbschaftsausschlagung` | 6-Wochen-Frist § 1944 BGB, notarielle/gerichtliche Erklärung |
| Testament auslegen | `testament-auslegung-und-andeutung` | Andeutungstheorie, Auslegungsregeln, ergänzende Auslegung |
| Erbschein beantragen | `erbschein-antrag` | Antrag, Glaubhaftmachung, eidesstattliche Versicherung |
| Erbengemeinschaft blockiert | `erbengemeinschaft-blockade-auseinandersetzung` | Teilungsklage, Vermittlungsverfahren §§ 363 ff. FamFG |

## Norm-Radar (live verifizieren)

- **§ 1944 BGB** — Ausschlagungsfrist 6 Wochen
- **§ 2303 BGB** — Pflichtteilsanspruch
- **§ 2314 BGB** — Auskunftsanspruch des Pflichtteilsberechtigten
- **§ 2325 BGB** — Pflichtteilsergänzung; 10-Jahres-Abschmelzung
- **§ 2353 BGB** — Erbschein
- **§ 1980 BGB** — Antrag Nachlassinsolvenz

## Genau eine Rückfrage (nur wenn nötig)

> Vertreten Sie **Erbe(n), Pflichtteilsberechtigte oder Vermächtnisnehmer** — und steht eine **Frist** (Ausschlagung, Anfechtung) oder eine **Verteilungsfrage** im Vordergrund?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Pflichtteilsergänzung § 2325 BGB; 10-Jahres-Abschmelzung** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Pflichtteilsstrafklausel (Berliner Testament); Auslegung** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Erbschaftsteuer; Verschonungsregelungen** — BVerfG 1. Senat (Urteil v. 17.12.2014, 1 BvL 21/12) — *live verifizieren auf* `bundesverfassungsgericht.de`
- **Digitaler Nachlass (Facebook-Konto)** — BGH III. Zivilsenat (Urteil v. 12.07.2018, III ZR 183/17) — *live verifizieren auf* `bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.
