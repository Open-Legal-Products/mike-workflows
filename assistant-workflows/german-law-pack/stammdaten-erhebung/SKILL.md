---
name: "stammdaten-erhebung"
description: "When Stammdaten-Erhebung in Employment Law is required: organises file content, evidence, gaps, and follow-up requests; produces an interface map with conflict, jurisdiction, and evidence questions."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Stammdaten Erhebung"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Employment Law"
  jurisdictions: "Germany"
---

# Stammdaten-Erhebung

## Ziel

Einen vollständigen, fehlerfreien Zeugniskopf generieren. Falsche Stammdaten sind eigenständige Berichtigungspunkte.

## Eingang — was wird abgefragt

| Datenpunkt | Pflicht | Hinweis |
|---|---|---|
| Vollständiger Name | ja | Exakte Schreibweise aus dem Personalausweis |
| Geburtsdatum | ja | TT.MM.JJJJ |
| Eintrittsdatum | ja | Datum des ersten Arbeitstages |
| Austrittsdatum | ja | Letzter vertraglich relevanter Tag; bei Zwischenzeugnis leer lassen |
| Positionsbezeichnung | ja | Exakt wie im Arbeitsvertrag oder zuletzt gültiger Zusatz |
| Hierarchiestufe | bei Führungskräften | z.B. „Leiterin", „Senior", „Teamleiter" |
| Abteilung/Bereich | empfohlen | Für Einordnung im Aufgabenblock |
| Unternehmensname und Rechtsform | ja | GmbH, AG, GbR usw. |
| Unternehmensanschrift | ja | Für Briefkopf |
| Name und Funktion des Unterzeichners | ja | Muss hierarchisch befugt sein |

## Generier-Regeln

- Einleitungssatz: „[Vollständiger Name], geboren am [Datum], war vom [Eintrittsdatum] bis zum [Austrittsdatum] in unserem Unternehmen als [Positionsbezeichnung] tätig."
- Präzise Positionsbezeichnung verwenden — nicht „Mitarbeiter" wenn „Projektleiter IT-Infrastruktur" die korrekte Bezeichnung ist.
- Bei Beförderungen oder Positionswechseln während der Beschäftigungszeit: alle Positionen mit jeweiligen Zeiträumen nennen (siehe Skill mehrere-positionen-im-zeugnis).
- Geburtsdatum ist im qualifizierten Zeugnis üblich; bei Widerspruch des Arbeitnehmers kann es entfallen.

## Platzhalter-Konventionen

Fehlende Daten werden immer als Platzhalter gesetzt:
- `[Vorname Name]`
- `[TT.MM.JJJJ]`
- `[Positionsbezeichnung]`
- `[Unternehmen GmbH]`

Platzhalter niemals stillschweigend erfinden — der Nutzer muss sie explizit bestätigen.

## Formalia-Check

Nach Paragraf 109 GewO und BAG, Urteil v. 21.09.1999 – 9 AZR 893/98 muss der Unterzeichner genau die Person sein, deren Name und Funktion am Ende des Zeugnisses in Maschinenschrift erscheint. HR-Sachbearbeiter dürfen nicht für den Vorgesetzten unterzeichnen, wenn dieser namentlich genannt wird.

## Stolpersteine

- Arbeitnehmer führte faktisch eine höhere Funktion aus als der Vertrag aussagt — Generator kann nur die vertraglich oder zuletzt gültig kommunizierte Bezeichnung verwenden; Hinweis auf mögliche Diskrepanz geben.
- Eintrittsdatum bei Übernahme aus Zeitarbeit oder befristeten Vorverträgen unklar — immer beim Nutzer nachfragen, da es den Gesamteindruck des Zeugnisses prägt.
- Austrittsdatum fehlt bei laufendem Verfahren — Zwischenzeugnis-Harness aktivieren.

## Anti-Muster

- Positionsbezeichnung eigenständig „aufhübschen" (aus „Sachbearbeiter" wird „Spezialist").
- Geburtsdatum weglassen, ohne den Nutzer darauf hinzuweisen, dass es im Bewerbungsverkehr üblich ist.
- Unternehmensname ohne Rechtsform nennen.

## Ausgabeformat

Das Endprodukt wird in vollständigen, ausformulierten und grammatikalisch sauberen Sätzen geliefert; Stichworte, Halbsätze, leere Klauselrümpfe und reine Aufzählungs-Skelette sind als Endprodukt unzulässig (Ausformulierungspflicht). Die hier katalogisierten Formeln und Bausteine sind Zwischenergebnisse und werden im fertigen Zeugnis zu vollständigem Fließtext verbunden. Soweit technisch möglich, verwendet das formatierte Enddokument Times New Roman in 11 pt und ausschließlich dezimale Gliederung (1, 1.1, 1.1.1); bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch ausdrücklich als Exporthinweis vermerkt.
