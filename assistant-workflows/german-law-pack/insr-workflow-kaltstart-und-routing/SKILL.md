---
name: "insr-workflow-kaltstart-und-routing"
description: "Wenn es um Kaltstart und Routing in Insolvenzrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert eine Fristen- und Risikoampel mit Sofortschritten."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Insr Workflow Kaltstart Und Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Insolvency and Restructuring"
  jurisdictions: "Germany"
---

# Kaltstart und Routing

## Aufgabe
Nutze diesen Workflow-Skill für Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.

## Kaltstart
Wenn Material vorliegt, arbeite zuerst mit dem Material. Stelle nur Rückfragen, die für die nächste Weiche nötig sind:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Spezialskills aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Insolvenzrecht-spezifische Routing-Weichen
- **Antragspflicht (§ 15a InsO)?** Geschäftsführer/Vorstand bei GmbH/AG → Drei-Wochen-Frist bei Zahlungsunfähigkeit (§ 17 InsO), Sechs-Wochen-Frist bei Überschuldung (§ 19 InsO). Sofort prüfen, ob Frist läuft. Bei Haftungsfrage: Skill für Geschäftsführerhaftung.
- **Eröffnungsgrund?** Zahlungsunfähigkeit § 17 InsO (Liquiditätslücke ≥ 10 Prozent über drei Wochen, BGH-Linie), drohende Zahlungsunfähigkeit § 18 InsO (Prognosezeitraum 24 Monate seit SanInsFoG), Überschuldung § 19 InsO (rechnerische Überschuldung plus negative Fortbestehensprognose, Prognosezeitraum 12 Monate).
- **Verfahrensart?** Regelinsolvenz, Eigenverwaltung § 270 InsO (Antrag mit Eigenverwaltungsplanung § 270a InsO), Schutzschirm § 270d InsO (drohende Zahlungsunfähigkeit oder Überschuldung, Bescheinigung nach IDW S6 oder vergleichbar), StaRUG-Restrukturierung § 29 StaRUG (nur drohende Zahlungsunfähigkeit).
- **Rolle des Mandanten?** Schuldner, Geschäftsführer (persönliche Haftung), Insolvenzverwalter, Gläubiger (Anmeldung, Aus-/Absonderung), Anfechtungsgegner, Sicherungsnehmer.
- **Eilige Trigger:** Insolvenzgeldvorfinanzierung läuft, Lohnzahlung steht an, Energieversorger droht Sperre, Vermieter kündigt § 112 InsO, Pfändung droht, Strafanzeige § 15a Abs. 4 InsO im Raum.

## Anti-Halluzinations-Hinweise
- Keine erfundenen BGH-Aktenzeichen. Wenn Datum/Az. nicht sicher: "BGH-Linie zu § 17 InsO, Az. bitte verifizieren".
- IDW S6 ist Standard für Sanierungskonzept, IDW S11 für Insolvenzgründe — Stand stets prüfen.
- Drei-Wochen-Frist § 15a InsO ist Höchstfrist, keine Mindestfrist. Verkürzung möglich, wenn Sanierung aussichtslos.
