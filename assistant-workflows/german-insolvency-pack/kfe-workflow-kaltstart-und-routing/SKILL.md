---
name: "kfe-workflow-kaltstart-und-routing"
description: "When Kaltstart und Routing in Insolvency and Restructuring is required: clarifies role, objective, deadline, documents, and the appropriate next specialist workflow; produces a deadline and risk indicator with immediate action steps."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Kfe Workflow Kaltstart Und Routing"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Insolvency and Restructuring"
  jurisdictions: "Germany"
  source-plugin: "krisenfrueherkennung-starug"
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

## Routing-Weichen Krisenfrüherkennung
- **Rechtspflicht:** § 1 StaRUG verpflichtet die Geschäftsleiter von haftungsbeschränkten Unternehmen (GmbH, AG, UG, SE, ggf. GmbH & Co. KG bei Haftungsbeschränkung), Entwicklungen, die den Fortbestand der juristischen Person gefährden könnten, fortlaufend zu überwachen und geeignete Gegenmaßnahmen zu ergreifen.
- **Beobachtungszeitraum:** Es gilt ein **rollierender 24-Monats-Horizont** (parallel zu § 18 InsO drohende Zahlungsunfähigkeit) — sobald in diesem Horizont eine Liquiditätslücke droht, ist die Pflicht ausgelöst.
- **Mandantenrolle?**
  - Geschäftsleitung selbst (haftungsrelevant): persönliche Pflicht nach § 1 StaRUG, kein Delegationsausschluss.
  - Berater (RA, StB, Sanierungsberater): Plausibilisieren des Frühwarnsystems.
  - Aufsichtsrat/Beirat: Überwachungspflicht (§ 111 AktG, § 52 GmbHG bei Beirat mit Aufsichtsfunktion).
- **Welcher Skill als Nächstes?**
  - Liquiditätsplanung (13-Wochen oder 24-Monate) → liquiditaetsplanung-Plugin.
  - Fortbestehensprognose → fortbestehensprognose-Plugin.
  - StaRUG-Plan oder Insolvenzplan → insolvenzplan-starug-planwerkstatt-Plugin.

## Eilige Trigger
- Hinweise auf drohende ZU → § 18 InsO greift, StaRUG-Anzeige § 31 StaRUG möglich.
- Eingetretene ZU/Überschuldung → § 15a InsO Antragspflicht, § 1 StaRUG tritt zurück.
- § 15b InsO Zahlungsverbot ist ab dem Zeitpunkt der materiellen Insolvenz zu beachten — Geschäftsführer haftet persönlich.
