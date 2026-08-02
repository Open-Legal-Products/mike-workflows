---
name: "fa-ins-unterlagen-luecken"
description: "When Unterlagen und Lücken in Insolvency and Restructuring is required: drafts the appropriate document from facts, norm, evidence, and motion; produces a deadline and risk indicator with immediate action steps."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Fa Ins Unterlagen Luecken"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Insolvency and Restructuring"
  jurisdictions: "Germany"
  source-plugin: "fachanwalt-insolvenz-sanierungsrecht"
---

# Unterlagen und Lücken

## Einsatzlage

Diese Unterlagenprüfung für **Fachanwalt Insolvenz Sanierungsrecht** benennt fehlende Dokumente, streitige Tatsachen, Beweisrisiken und die kürzeste sichere Nachforderung.

## Fachlandkarte dieses Plugins

- `absonderungsrecht-paragraf-50-inso` — Absonderungsrecht Paragraf 50 Inso
- `anfechtung-vorsatz-paragraf-133-inso-bgh-ix-zr-65-16` — Anfechtung Vorsatz Paragraf 133 Inso BGH IX ZR 65 16
- `eigenverwaltung-schutzschirm-paragraf-270b-inso` — Eigenverwaltung Schutzschirm Paragraf 270b Inso
- `eroeffnung-behoerden-gericht-und-registerweg` — Eroeffnung Fachanwalt FAO Gläubigerantrag
- `fa-inso-sanierung-quellen-edge-case` — FA Inso Sanierung Quellen Edge Case
- `fa-insolvenz-schuldschein-und-lma` — FA Schuldschein
- `glaeubigerantrag` — Gläubigerantrag Insolvenzanfechtung
- `insolvenz-glaeubigerverhandlung-sanierung` — Gläubigerverhandlung Sanierung IDW S6 Krypto
- `insanw-eigenverwaltung-schutzschirm-spezial` — Insanw Eigenverwaltung Konzerninsolvenz
- `einstieg-schnelltriage-fallrouting` — Insanw Fortbestehensprognose
- `insolvenz-tatbestand-beweis-und-belege` — Insolvenz Insolvenzanfechtung Insolvenzrecht
- `insolvenzgeld-paragraf-165-sgb-iii` — Insolvenzgeld Paragraf 165 SGB III
- `insolvenzplan-paragraf-217-inso-bgh-ix-zb-66-19` — Insolvenzplan Paragraf 217 Inso BGH IX ZB 66 19
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Sollkatalog aufstellen: Welche Dokumente brauche ich für die konkrete Fachanwalt Insolvenz Sanierungsrecht-Frage zwingend (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets)?
- Ist-Abgleich: Welche Dokumente sind vorhanden, welche fehlen, welche sind unvollständig, undatiert oder ohne Unterschrift?
- Lückenliste priorisieren nach: fristrelevant (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), beweisrelevant, formerheblich.
- Rückfrageschreiben an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen entwerfen — Wer hat das Dokument, woher kann es beschafft werden, bis wann?
- Bei behördlichen Lücken: Akteneinsichtsrecht (z. B. § 29 VwVfG, § 147 StPO, § 25 SGB X) prüfen und nutzen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
