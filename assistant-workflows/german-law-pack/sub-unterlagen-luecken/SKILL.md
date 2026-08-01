---
name: "sub-unterlagen-luecken"
description: "Wenn es um Unterlagen und Lücken in Subsumtions-Prüfer geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Sub Unterlagen Luecken"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Legal Methodology"
  jurisdictions: "Germany"
---

# Unterlagen und Lücken

## Einsatzlage

Diese Unterlagenprüfung für **Subsumtions Prüfer** benennt fehlende Dokumente, streitige Tatsachen, Beweisrisiken und die kürzeste sichere Nachforderung.

## Fachlandkarte dieses Plugins

- `anwenden-quellenkarte` — Anwenden Quellenkarte
- `beweisbedarf-und-belege-erfassen` — Beweisbedarf und Belege Erfassen
- `darlegungs-und-beweislast-verteilen` — Darlegungs und Beweislast Verteilen
- `einreden-compliance-dokumentation-und-akte` — Einreden Compliance Dokumentation und Akte
- `einschlaegige-normen-vorschlagen-de` — Einschlaegige Normen Vorschlagen DE
- `einschlaegige-normen-vorschlagen-eu` — Einschlaegige Normen Vorschlagen EU
- `eu-abgrenzung-einschlaegige-normen` — EU Abgrenzung Einschlaegige Normen
- `eu-vorabentscheidung-falsche-wiese` — EU Vorabentscheidung Falsche Wiese
- `europarecht-fristen-form-und-zustaendigkeit` — Europarecht Fristen Form und Zustaendigkeit
- `falsche-wiese-warnung` — Falsche Wiese Warnung
- `fehlerklasse-bgb-at-training` — Fehlerklasse BGB AT Training
- `generalklauseln-pruefen` — Generalklauseln Prüfen
- `grundrechte-pruefung-de-und-grch` — Grundrechte Prüfung DE und Grch
- `dokumente-intake` — Dokumente Intake
- `einstieg-routing` — Einstieg Routing

## Arbeitsweg

- Sollkatalog aufstellen: Welche Dokumente brauche ich für die konkrete Subsumtions Prüfer-Frage zwingend (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets)?
- Ist-Abgleich: Welche Dokumente sind vorhanden, welche fehlen, welche sind unvollständig, undatiert oder ohne Unterschrift?
- Lückenliste priorisieren nach: fristrelevant (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), beweisrelevant, formerheblich.
- Rückfrageschreiben an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen entwerfen — Wer hat das Dokument, woher kann es beschafft werden, bis wann?
- Bei behördlichen Lücken: Akteneinsichtsrecht (z. B. § 29 VwVfG, § 147 StPO, § 25 SGB X) prüfen und nutzen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
