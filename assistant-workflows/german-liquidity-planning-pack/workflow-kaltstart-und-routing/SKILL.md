---
name: "workflow-kaltstart-und-routing"
description: "When Kaltstart und Routing in Insolvency and Restructuring Law is required: clarifies role, objective, deadline, documents, and the appropriate next specialist workflow; produces a deadline and risk indicator with immediate action steps."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Workflow Kaltstart Und Routing"
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

## Routing-Weichen Liquiditätsplanung
- **Zweck der Planung?**
  - **13-Wochen-Liquidität** (Standard in der Krise): Wochengranularität, taggenaue Cash-In/Cash-Out — Grundlage für ZU-Prüfung § 17 InsO und Sanierungssteuerung.
  - **24-Monats-Liquiditätsplan** (StaRUG/§ 18 InsO): Monatsgranularität, integriert mit GuV und Bilanz — Grundlage für drohende ZU und Frühwarnsystem § 1 StaRUG.
  - **12-Monats-Plan** für Fortbestehensprognose § 19 InsO (Überschuldung) — Methodik nach IDW EPS 11.
- **Datenbasis?**
  - **Direkte Methode** (bevorzugt in der Krise): Cash-Inflows aus OPOS-Listen, Cash-Outflows aus Fälligkeitslisten — robust gegen Bilanzeffekte.
  - **Indirekte Methode** (aus GuV/Bilanz abgeleitet): Cashflow aus Jahresabschluss-Forecast — geeignet für langfristige Planung, anfällig bei Krise.
- **Mandantenrolle?**
  - Geschäftsführer (Haftung § 15a, § 15b InsO): operative Steuerung.
  - Sanierungsberater: CRO, Erstellung 13-Wochen-Plan.
  - Insolvenzverwalter: Massesteuerung, § 158 InsO Fortführungsentscheidung.
  - Kreditgeber: Standstill-Begleitung, Covenants-Monitoring.

## Eilige Trigger
- Liquiditätslücke in nächsten 4 Wochen erkennbar → ZU § 17 InsO droht; 3-Wochen-Frist § 15a InsO greift, wenn Lücke ≥ 10 Prozent.
- Liquiditätsplan zeigt nur Vergangenheit, keine Vorausschau → unbrauchbar als Frühwarninstrument, Pflichtverletzung § 1 StaRUG.
