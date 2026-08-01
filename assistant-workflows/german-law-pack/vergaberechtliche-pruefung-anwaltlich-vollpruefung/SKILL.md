---
name: "vergaberechtliche-pruefung-anwaltlich-vollpruefung"
description: "When Vergaberechtliche Prüfung aus anwaltlicher Sicht: Vollprüfung in Public Procurement Law is required: calculates thresholds, amounts, variants, and control assumptions; produces a calculation table with thresholds, assumptions, and control questions."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Vergaberechtliche Pruefung Anwaltlich Vollpruefung"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Public Procurement Law"
  jurisdictions: "Germany"
---

# Vergaberechtliche Prüfung aus anwaltlicher Sicht: Vollprüfung

## Einsatzlage

Dieser Skill führt einen Volljuristen Schritt für Schritt durch die vollständige vergaberechtliche Prüfung einer konkreten öffentlichen Auftragsvergabe, entweder aus Sicht eines abgewiesenen oder ausgeschlossenen Bieters (Angriffsperspektive: Rüge, Nachprüfung, einstweiliger Rechtsschutz, Schadensersatz) oder aus Sicht des öffentlichen Auftraggebers (Verteidigungsperspektive: Verfahrensführung, Wertung, Vergabeakte, Stand der Prüfung).

Output ist ein anwaltliches Prüfgutachten im Gutachtenstil, das vollständig zitierfähig ist und an dem sich Schriftsätze für die Vergabekammer, sofortige Beschwerden zum Vergabesenat des OLG und Schadensersatzklagen zum Landgericht direkt orientieren lassen.

### Strikte Quellenhygiene

- **Rechtsprechung nur, wenn das Aktenzeichen vom Anwender verifiziert oder aus einer offiziellen Datenbank (BGH, BVerfG, OLG, juris, dejure) belegt ist.** Wenn ein Aktenzeichen nicht verifizierbar ist, wird es explizit als **unverifiziert** markiert und der Prufstand bleibt **offen**.
- **Keine Blindzitate aus BeckRS, IBR, ZfBR, VergabeR-Aufsaetzen, Kommentaren oder Schulungsunterlagen.** Solche Quellen werden nur dann angefuehrt, wenn der Mandant sie selbst beibringt.
- **Norm immer mit Paragraph, Absatz, Satz und Nummer zitieren** (z. B. § 160 Abs. 3 Satz 1 Nr. 1 GWB), nie nur "§ 160 GWB".
- **Schwellenwerte und Fristen** werden ohne Zahl-Komma-Zahl-Sequenzen angegeben (z. B. "EU-Schwelle Liefer- und Dienstleistungsauftraege oberhalb Bundesbehoerden Stand des Vergabeverfahrens"). Der konkrete Schwellenwert wird stets aus der **aktuell geltenden Schwellenwerteverordnung** uebernommen, nicht aus dem Gedaechtnis.

### Strikter Disclaimer-Hinweis

Dieser Skill begründet kein Mandatsverhältnis, ist keine Rechtsberatung im Einzelfall und ersetzt nicht die anwaltliche Prüfung der Originalunterlagen. Output ist ein Prüfraster, kein Schriftsatz; jede Verwendung in einem realen Mandat erfordert die Verifikation aller Tatsachen, Fristen, Aktenzeichen und Rechtsprechung durch den verantwortlichen Anwalt.

---

## Phase 0 — Mandantenrolle, Verfahrensart, Fristampel (Sofort-Check)

Bevor irgendetwas anderes geprueft wird, sind diese sechs Punkte zu klaeren. Jeder dieser Punkte kann das gesamte Mandat innerhalb weniger Stunden auf Fristverlust laufen lassen.

### A. Mandantenrolle

- Bieter (eingereichtes Angebot, Teilnahmeantrag, Interessenbekundung) — Angriffsperspektive.
- Bewerber, der **nicht** zur Angebotsabgabe aufgefordert wurde — Angriffsperspektive ohne Angebot.
- Nicht-Bieter mit subjektivem Recht auf Beteiligung (z. B. uebergangener Marktteilnehmer bei De-facto-Vergabe) — Angriffsperspektive nach § 135 GWB.
- Oeffentlicher Auftraggeber (Bund, Land, Kommune, juristische Person oeffentlichen Rechts, sektorenrelevante AG, beliehene Stelle) — Verteidigungsperspektive.
- Sektorenauftraggeber (Wasser, Verkehr, Energie, Postdienste) — Verteidigungsperspektive mit SektVO-Regime.
- Konzessionsgeber (Bau- oder Dienstleistungskonzession) — KonzVgV-Regime.

**Pflichtfrage:** "Ist der Mandant Bieter, Bewerber, uebergangener Marktteilnehmer oder Auftraggeber? Beleg: Eingangsbestaetigung, EU-Bekanntmachungstext, Aufforderungsschreiben."

### B. Verfahrensart

- Offenes Verfahren (§ 15 VgV) — alle Interessierten koennen Angebot abgeben.
- Nicht offenes Verfahren mit oeffentlichem Teilnahmewettbewerb (§ 16 VgV).
- Verhandlungsverfahren mit Teilnahmewettbewerb (§ 17 VgV).
- Verhandlungsverfahren ohne Teilnahmewettbewerb (§ 17 Abs. 5 VgV — Ausnahme, eng zu pruefen).
- Wettbewerblicher Dialog (§ 18 VgV).
- Innovationspartnerschaft (§ 19 VgV).
- Rahmenvereinbarung (§ 21 VgV).
- Direktauftrag im Unterschwellenbereich (UVgO § 14).
- Beschraenkte Ausschreibung mit oder ohne Teilnahmewettbewerb (UVgO §§ 10, 11).
- Verhandlungsvergabe (UVgO § 12).
- Bauauftrag nach VOB/A (Abschnitt 1 unterhalb, Abschnitt 2 oberhalb Schwelle).
- Konzessionsvergabe (KonzVgV).
- **De-facto-Vergabe**: Auftraggeber hat **ohne** vorherige Bekanntmachung vergeben — wichtigster Anwendungsfall des § 135 GWB.

**Pflichtfrage:** "Welches Verfahren wurde gewaehlt, und welche Norm rechtfertigt die Wahl? Beleg: Vergabevermerk, Bekanntmachung TED-Nr. oder Begruendung des Verzichts auf Bekanntmachung."

### C. Schwellenwert und Anwendungsbereich

- Anwendung von **GWB-Vergaberecht** (4. Teil GWB, VgV, SektVO, KonzVgV, VOB/A 2. Abschnitt) nur **oberhalb** der EU-Schwelle.
- **Unterhalb** der Schwelle: Haushaltsvergaberecht der Laender, UVgO oder VOB/A 1. Abschnitt. Rechtsschutz: kein GWB-Nachpruefungsverfahren, nur Verwaltungsrecht oder Zivilrecht und ggf. Verfassungsbeschwerde nach BVerfG-Rechtsprechung zum Bewerberschutz.
- **Schwellenwerte** sind in der jeweils geltenden Schwellenwerteverordnung festgelegt und werden zweijaehrlich durch EU-Delegierte VO angepasst.
- Pruefung der **Auftragswertschaetzung** nach § 3 VgV (Schaetzung zum Zeitpunkt der Absendung der Bekanntmachung; netto, ohne MwSt; einschliesslich Optionen, Vertragsverlaengerungen, Preisanpassungen).
- **Losweise Vergabe** (§ 97 Abs. 4 GWB, § 5 VgV): Schwellenwert wird durch **Addition der Lose** ermittelt; Bagatell-Lose nach § 3 Abs. 9 VgV (20 Prozent-Grenze) duerfen unterhalb der Schwelle vergeben werden.

**Pflichtfrage:** "Wie wurde der Auftragswert geschaetzt, und ist die Losbildung dokumentiert? Beleg: Vergabevermerk."

### D. Fristen-Sofortcheck (oberste Prioritaet)

Folgende Fristen entscheiden ueber den Erhalt der Antragsbefugnis. Wer sie verpasst, hat im Nachpruefungsverfahren ueberwiegend keine Erfolgsaussicht mehr.

- **§ 160 Abs. 3 Satz 1 Nr. 1 GWB — Ruege innerhalb einer gesetzlichen Frist von 10 Kalendertagen** ab Kenntnis des behaupteten Vergaberechtsverstosses. Die Frist ist **starr** und **nicht** mit dem dehnbaren "unverzueglich"-Standard des § 121 BGB gleichzusetzen; nach Fristablauf ist der Nachpruefungsantrag praekludiert. "Kenntnis" setzt positive Tatsachen- und Rechtskenntnis voraus; reine Vermutung genuegt nicht (vgl. BGH X ZB 14/06; spaeter bestaetigt und differenziert in zahlreichen OLG-Vergabesenat-Entscheidungen).
- **§ 160 Abs. 3 Satz 1 Nr. 2 GWB — Ruege erkennbarer Verstoesse in der Bekanntmachung spaetestens bis Ablauf der Angebots- oder Teilnahmefrist.**
- **§ 160 Abs. 3 Satz 1 Nr. 3 GWB — Ruege erkennbarer Verstoesse in den Vergabeunterlagen spaetestens bis Ablauf der Angebots- oder Teilnahmefrist.**
- **§ 160 Abs. 3 Satz 1 Nr. 4 GWB — Nachpruefungsantrag innerhalb von 15 Kalendertagen nach Eingang der Nichtabhilfemitteilung.**
- **§ 134 Abs. 1 GWB — Vorabinformationspflicht des Auftraggebers ueber den geplanten Zuschlag.** Stillhaltefrist **15 Kalendertage** ab Absendung der Vorabinformation per Post; **10 Kalendertage** bei elektronischer Uebermittlung (§ 134 Abs. 2 Satz 2 und 3 GWB).
- **§ 135 Abs. 2 GWB — De-facto-Vergabe-Frist**: 30 Kalendertage ab Kenntnis vom Verstoss, **spaetestens 6 Monate nach Vertragsschluss**. Bei einer in EU-Amtsblatt veroeffentlichten Ex-ante-Bekanntmachung greift die kuerzere 30-Tage-Frist ab Veroeffentlichung.
- **§ 171 Abs. 3 GWB — Sofortige Beschwerde gegen Entscheidungen der Vergabekammer**: 2 Wochen ab Zustellung beim zustaendigen Vergabesenat des OLG einlegen und begruenden.

**Pflichtfrage in jedem Mandat:** "Welche dieser Fristen sind angelaufen und welche sind bereits abgelaufen? Beleg: konkretes Datum mit Uhrzeit aus der Vergabeakte oder dem Mandanten-Posteingang."

### E. Zustaendigkeit

- **Bundesauftraggeber** (Bund, bundesunmittelbare juristische Personen oeffentlichen Rechts): Vergabekammer des Bundes beim Bundeskartellamt.
- **Land** (Land, Kommune, kommunaler Zweckverband, Landeshochschule, sonstige Landeskoerperschaft): Vergabekammer des Landes (je nach Bundesland Regierungspraesidium, Bezirksregierung oder eigene Vergabekammer).
- **Sektorenauftraggeber** und **Konzessionsgeber**: gleiche oertliche Zustaendigkeit, getrennt nach Auftraggebertyp.
- **Vergabesenat des OLG** ist sofortiges Beschwerdegericht (§ 171 GWB).
- **Schadensersatzklage** (§§ 181 GWB, 33a, 33f GWB): ordentliche Gerichte, am Sitz des Auftraggebers.

### F. Sofort-Mandantenfrage

"Welche der folgenden 6 Fristen ist im konkreten Fall die naechste, die ablaeuft, mit kalendarischem Datum und Uhrzeit, gemessen ab welchem Ereignis?"
- Ruegefrist § 160 III Nr. 1 GWB
- Ruegefrist § 160 III Nr. 2 oder Nr. 3 GWB
- Stillhaltefrist § 134 GWB
- Nachpruefungsantragsfrist § 160 III Nr. 4 GWB
- Sofortige-Beschwerde-Frist § 171 III GWB
- 6-Monats-Frist § 135 II GWB

Wenn die Antwort fehlt oder unklar ist, wird die Pruefung **abgebrochen** und der Mandant **schriftlich** darauf hingewiesen, dass ohne fristgerechte Klaerung alle weiteren Schritte sinnlos sein koennen.

---

## Phase 1 — Anwendungsbereich des Vergaberechts (§ 99 ff. GWB)

### 1.1 Oeffentlicher Auftraggeber (§ 99 GWB) und Sektorenauftraggeber (§ 100 GWB)

**Wichtig:** § 99 GWB enumeriert die **klassischen** oeffentlichen Auftraggeber. **Sektorenauftraggeber** sind dagegen in **§ 100 GWB** separat geregelt und unterliegen dem SektVO-Regime; Konzessionsgeber stehen in **§ 101 GWB**. Diese Trennung in drei Auftraggebertypen ist konsequent zu beachten, sonst zitiert die spaetere Antragsschrift eine **nicht existente Norm** und verfehlt den persoenlichen Anwendungsbereich.

**§ 99 GWB** (oeffentliche Auftraggeber im klassischen Bereich) hat folgende vier Tatbestandsalternativen — jede einzeln pruefen, **niemals nur Nr. 1**:

- **§ 99 Nr. 1 GWB:** Gebietskoerperschaften, Bund, Laender, Gemeinden, deren Sondervermoegen, beliehene Stellen.
- **§ 99 Nr. 2 GWB:** Juristische Person des oeffentlichen oder privaten Rechts, die zu dem **besonderen Zweck** gegruendet wurde, im **Allgemeininteresse** liegende Aufgaben **nichtgewerblicher Art** zu erfuellen, **und** die ueberwiegend von der oeffentlichen Hand finanziert, kontrolliert oder dominiert wird (Funktionalbegriff).
- **§ 99 Nr. 3 GWB:** Verbaende, deren Mitglieder unter Nr. 1 oder Nr. 2 fallen.
- **§ 99 Nr. 4 GWB:** Natuerliche oder juristische Personen, soweit sie Bauauftraege oder Dienstleistungen im Zusammenhang mit Bauauftraegen erbringen, die zu mehr als 50 Prozent durch Auftraggeber nach Nrn. 1 bis 3 subventioniert werden, oberhalb bestimmter Schwellen.

**§ 100 GWB** (Sektorenauftraggeber) erfasst:

- Auftraggeber im Sinne von § 99 Nr. 1 bis 3 GWB, soweit sie eine **Sektorentaetigkeit** (§ 102 GWB: Wasser, Energie, Verkehr, Postdienste) ausueben.
- Unternehmen mit **besonderen oder ausschliesslichen Rechten** (Konzessionen, Versorgungsrechte), die eine Sektorentaetigkeit ausueben.
- Beherrschte Unternehmen, an denen die oeffentliche Hand eine **rechtliche oder tatsaechliche Beherrschungsstellung** innehat und die eine Sektorentaetigkeit ausueben.

Auf Sektorenauftraggeber findet die **SektVO** Anwendung (Phase 13), nicht die VgV.

**§ 101 GWB** (Konzessionsgeber): § 99 Nr. 1 bis 3 GWB-Auftraggeber bei Konzessionsvergabe; Anwendung der **KonzVgV** (Phase 13).

**Praxisfaelle:**

- Tochter-GmbH einer Kommune (z. B. Stadtwerke-Holding, Wohnungsbaugesellschaft, Klinikum gGmbH, Theater gGmbH): regelmaessig § 99 Nr. 2 GWB (vgl. EuGH stRspr. seit C-44/96 "Mannesmann Anlagenbau Austria" und C-360/96 "BFI Holding"; deutsche Rezeption u. a. BGH X ZR 80/14, soweit verifizierbar).
- Reine Beteiligungs-GmbH ohne eigene operative Allgemeininteressen-Aufgabe: oft **kein** Auftraggeber.
- Universitaetskliniken in landesrechtlicher Anstaltsform: regelmaessig § 99 Nr. 1 GWB; in GmbH-Form je nach Beherrschungs- und Finanzierungssituation Nr. 2.
- Kirchen und Religionsgemeinschaften: grundsaetzlich kein Auftraggeber, soweit sie **eigene** Mittel verwenden; bei staatlicher Foerderung von Bauauftraegen ggf. Nr. 4.

### 1.2 Oeffentlicher Auftrag (§ 103 GWB)

- Entgeltlicher Vertrag zwischen Auftraggeber und Unternehmen ueber **Liefer-, Bau- oder Dienstleistungen**.
- Liefer- und Dienstleistungsauftraege sind voneinander zu trennen (§ 103 Abs. 2, 4 GWB); bei gemischten Vertraegen entscheidet der Hauptzweck.
- **Konzessionen** sind keine Auftraege im Sinne von § 103 GWB, sondern Konzessionen im Sinne von § 105 GWB (eigenes Regime KonzVgV).
- **Inhouse-Vergabe** (§ 108 GWB): kein Vergaberecht anzuwenden, wenn drei kumulative Voraussetzungen vorliegen (aehnliche Kontrolle wie ueber eigene Dienststellen, ueberwiegend Taetigkeit fuer den kontrollierenden Auftraggeber, keine direkte private Kapitalbeteiligung; EuGH C-107/98 "Teckal" und Folgerechtsprechung). Bei mehreren oeffentlichen Auftraggebern: gemeinsame Kontrolle (§ 108 Abs. 4–6 GWB).
- **Oeffentlich-oeffentliche Kooperation** (§ 108 Abs. 6 GWB): drei kumulative Voraussetzungen, von einander unabhaengige Kontrolle, gemeinsame oeffentliche Aufgabe, weniger als 20 Prozent Drittumsatz.

### 1.3 Bereichsausnahmen (§§ 107, 116, 117 GWB)

Pruefe folgende Ausnahmekataloge auf Anwendbarkeit (eng auszulegen):

- **§ 107 GWB**: u. a. Sicherheitsdienste der Streitkraefte (mit §§ 145 ff. GWB Sondervergaberecht), Geheimhaltungsbeduerftigkeit, Schiedsgerichtsverfahren, oeffentlich-rechtliche Dienstvertraege ueber bestimmte Sozialleistungen.
- **§ 116 GWB**: Forschungs- und Entwicklungsdienstleistungen ohne Allein-Auftraggeber-Nutzen, audiovisuelle Mediendienstleistungen oeffentlicher Rundfunkanstalten.
- **§ 117 GWB**: Auftraege im Verteidigungs- und Sicherheitsbereich nach VSVgV.
- **§ 118 GWB**: Inhouse-Sondervorschriften fuer Auftraege durch Hersteller fuer eine andere Behoerde im Verteidigungsbereich.
- **§ 119 GWB Wirtschaftliche und finanzielle Verbindungen**: hier nicht einschlaegig.

### 1.4 Subjektive Berechtigung (§ 97 Abs. 6 GWB)

§ 97 Abs. 6 GWB gewaehrt **subjektives Recht** auf Einhaltung der Vergabevorschriften an die **bietergeschuetzten Normen**. **Nicht jeder Vergaberechtsverstoss** verletzt das subjektive Recht; manche Vorschriften (z. B. interne Begruendungspflichten in der Vergabeakte) sind reine Innenpflichten ohne Drittschutz.

---

## Phase 2 — Bekanntmachung und Vergabeunterlagen

### 2.1 Bekanntmachung

- **EU-Bekanntmachung im TED** (Tenders Electronic Daily) ueber das **eForms**-Schema (verpflichtend seit 25.10.2023 fuer Oberschwellenvergaben; in DE auch ueber **DVAL — Datenservice oeffentlicher Einkauf**).
- **Nationale Bekanntmachung im Unterschwellenbereich** ueber Bekanntmachungsservice des Bundes (bund.de) und Landesvergabeportale.
- Fehler in der Bekanntmachung sind **erkennbare Vergaberechtsverstoesse** und mussten nach § 160 Abs. 3 Satz 1 Nr. 2 GWB **bis zum Ablauf der Angebots- oder Teilnahmefrist geruegt werden** — wer die Frist verpasst, ist mit der Ruege ausgeschlossen.

**Pruefraster Bekanntmachung:**

- Stimmt das Verfahren (Offen/Nicht offen/Verhandelt) mit der Verfahrensart in der Bekanntmachung ueberein?
- Sind die **Eignungskriterien** § 122 GWB in der Bekanntmachung oder in den Vergabeunterlagen **abschliessend** benannt? Eignungskriterien duerfen **nicht** nachgeschoben werden (EuGH C-336/12 "Manova"; OLG-Vergabesenat-Linie).
- Sind die **Zuschlagskriterien** mit Gewichtung in der Bekanntmachung oder den Vergabeunterlagen offengelegt (§ 127 Abs. 5 GWB)?
- Sind die **Eignungs- und Auswahlkriterien** sauber **getrennt** von den Zuschlagskriterien (Verbot der Doppelverwendung; EuGH C-31/87 "Beentjes" Linie)?
- Wurde die EEE (Einheitliche Europaeische Eigenerklaerung) als Pflichtformat verlangt (§ 50 VgV)?
- Stimmt die Aufteilung in Fachlose und Teillose mit § 97 Abs. 4 GWB ueberein?
- Ist die **Bestbieterzuschlagsregel** (§ 127 GWB iVm § 58 VgV) korrekt formuliert (wirtschaftlichstes Angebot, nicht bloss "guenstigstes")?

### 2.2 Vergabeunterlagen

Die Vergabeunterlagen umfassen mindestens (§§ 29 ff. VgV):

- Aufforderungsschreiben (Angebotsaufforderung).
- Bewerbungsbedingungen.
- Leistungsbeschreibung (§§ 121 GWB, 31 VgV) — produktneutral und diskriminierungsfrei. Verbot der "Konkurrenten-Beschreibung" (Festlegung auf konkretes Fabrikat ist nur bei sachlichem Grund und mit "oder gleichwertig"-Zusatz zulaessig).
- Vertragsentwurf einschliesslich AGB des Auftraggebers (oft VHB, BVB-Klauseln, Allgemeine Vertragsbedingungen ZVB/EVM).
- Eignungs- und Wertungskriterien mit Gewichtung.
- Preisblatt, Leistungsverzeichnis (bei Bauauftraegen GAEB), Preisermittlungsformulare.

**Pruefraster Vergabeunterlagen:**

- Sind die Vergabeunterlagen **vollstaendig**, **widerspruchsfrei** und **eindeutig** (§ 121 Abs. 1 GWB)? Widerspruechliche Vergabeunterlagen koennen zur Verfahrensaufhebung zwingen.
- Wird die **Mindestanforderung** klar von **Wuenschen** abgegrenzt?
- Werden **diskriminierende Anforderungen** an Sitz, Sprache, Zertifikat erkennbar erhoben? Sitz darf nicht gefordert werden; Zertifikate nur unter Gleichwertigkeitsvorbehalt (§ 49 VgV).
- Ist die Bewertungsmethodik der Zuschlagskriterien **transparent und nachvollziehbar** (vgl. BVerfG 1 BvR 1387/16, soweit verifiziert; EuGH-Rsp. zur Transparenz)?
- Sind unterhaltige Mindestloehne, ILO-Kernarbeitsnormen, soziale und oekologische Anforderungen klar geregelt (§§ 128, 129 GWB, § 31 LVergabeG des Landes)?
- Bietet der Auftraggeber **angemessene Fristverlaengerung** bei wesentlichen Aenderungen an (§ 20 VgV)?

---

## Phase 3 — Eignung und Eignungspruefung (§ 122 GWB, §§ 42 ff. VgV)

### 3.1 Eignungskategorien

§ 122 Abs. 2 GWB unterscheidet vier Eignungskategorien — **abschliessend**, andere Kategorien sind unzulaessig:

- Befaehigung und Erlaubnis zur Berufsausuebung.
- Wirtschaftliche und finanzielle Leistungsfaehigkeit.
- Technische und berufliche Leistungsfaehigkeit.
- Sonstige Kriterien, soweit ausdruecklich in § 122 GWB benannt.

Geforderte Nachweise muessen **verhaeltnismaessig** sein (§ 122 Abs. 4 GWB iVm § 42 Abs. 1 VgV).

### 3.2 Mindestanforderungen — Umsatz, Bilanz, Referenzen

- **Mindestjahresumsatz** (§ 45 Abs. 4 VgV): maximal das **Zweifache** des geschaetzten Auftragswerts, in begruendeten Ausnahmen mehr.
- **Eigenkapitalquote, Liquiditaet** (§ 45 Abs. 4 VgV): nur, wenn fuer die Auftragsausfuehrung **relevant**, mit klarer Begruendung.
- **Referenzauftraege** (§ 46 Abs. 3 Nr. 1 VgV): aus den letzten drei Jahren bei Lieferungen und Dienstleistungen, bei Bauauftraegen aus den letzten fuenf Jahren (laenger nur, wenn fuer angemessenen Wettbewerb noetig).
- **Personalqualifikation**, **Zertifikate** (§§ 46, 49 VgV): Gleichwertigkeitsklausel zwingend.

### 3.3 Eignungsleihe (§ 47 VgV)

- Eignung kann durch Dritte geliehen werden (Kapazitaeten anderer Unternehmen).
- Bei wirtschaftlicher und finanzieller Eignungsleihe: **gesamtschuldnerische Haftung** kann gefordert werden.
- Bei berufsspezifischen Anforderungen, Berufserfahrung der Schluesselpersonen: Eignungsleihe **nur**, wenn die ausleihende Person die Leistung tatsaechlich erbringt.

### 3.4 Eignungspruefung in der Vergabeakte

Pruefe — und das ist im Mandat **immer Streitgegenstand**:

- Hat der Auftraggeber die **Eignung** des Zuschlagsbieters anhand der **EEE und Belege** sorgfaeltig geprueft (§ 122 GWB, § 50 VgV)?
- Wurden **Verstoesse** im Vergabeverfahren des Zuschlagsbieters dokumentiert?
- Wurde **Nachforderung** ueber § 56 VgV korrekt gehandhabt (siehe Phase 4)?
- Sind die Eignungsnachweise des Zuschlagsbieters **plausibel und vollstaendig**? Fehlt eine Eigenerklaerung zu Ausschlussgruenden nach §§ 123, 124 GWB?

---

## Phase 4 — Angebotsoeffnung, Aufklaerung, Nachforderung (§ 56 VgV)

### 4.1 Angebotsoeffnung

- Elektronische Angebotsabgabe ist seit 18.10.2018 (für Bauauftraege seit 18.10.2018) verpflichtend (§ 53 VgV iVm § 41 Abs. 1 Nr. 6 VgV).
- Eingangsbestaetigung (§ 53 Abs. 4 VgV).
- **Formmaengel bei Angebotsabgabe** sind zwingender Ausschlussgrund nach § 57 VgV.
- **Nachgereichte oder verspaetete Angebote**: zwingender Ausschluss (§ 57 Abs. 1 Nr. 1 VgV).

### 4.2 Nachforderung von Unterlagen (§ 56 VgV)

- Auftraggeber **kann** fehlende, unvollstaendige oder fehlerhafte unternehmensbezogene Unterlagen ueber § 56 Abs. 2 VgV nachfordern; **er muss nicht**.
- **Nicht** nachforderbar: das **Angebot selbst** und **leistungsbezogene Unterlagen** (Preise, Preisermittlung, Erklaerungen zur Mindestanforderung), wenn dadurch das Angebot **wettbewerblich verbessert** wuerde (EuGH C-336/12 "Manova"; OLG-Vergabesenat-Linie konsistent).
- **Nachforderung muss diskriminierungsfrei** ausgeuebt werden: bei mehreren Bietern mit gleicher Luecke entweder alle oder keiner.
- Fristsetzung: angemessen, regelmaessig 5 bis 10 Kalendertage.

**Streitige Konstellationen:**

- Fehlende Eigenerklaerung zur Tariftreue: nach § 56 VgV grundsaetzlich nachforderbar; auf landesrechtliche Sonderregeln im LVergabeG des Bundeslandes pruefen.
- Fehlendes Preisermittlungsformular: in der Regel **nicht** nachforderbar.
- Unklare Preise: § 60 VgV (ungewoehnlich niedriges Angebot) statt § 56 VgV.

### 4.3 Pruefraster Aufklaerung

- War die **Aufklaerung** sachlich notwendig (§ 15 EU VOB/A, § 58 Abs. 2 Satz 1 VgV)?
- Wurde der Bieter **nicht** zu einer **Angebotsaenderung** verleitet (Verbot der Angebotsverhandlung im offenen und nicht offenen Verfahren)?

### 4.4 Ungewoehnlich niedrige Angebote (§ 60 VgV, EuGH C-285/99 "Lombardini/Mantovani"-Linie)

- Bei deutlichem Abstand zum naechsten Angebot oder zur Schaetzung **muss** der Auftraggeber Aufklaerung verlangen.
- Aufklaerungsantworten sind zu pruefen: Personalkosten, Material, ungewoehnliche Subunternehmerstruktur, Beihilfe-Verdacht.
- **Kein automatischer Ausschluss** allein wegen Unterpreisigkeit, sondern **Pflicht zur Anhoerung**.

---

## Phase 5 — Ausschlussgruende (§§ 123, 124 GWB)

### 5.1 Zwingende Ausschlussgruende (§ 123 GWB)

Pruefe Katalog Nr. 1 bis Nr. 10 systematisch:

- **Geldwaesche**, **Terrorismusfinanzierung**, **Bestechung**, **Bestechlichkeit**, **Subventionsbetrug**, **Steuerhinterziehung**, **Organisierte Kriminalitaet**, **Menschenhandel**, **Vorenthalten von Arbeitsentgelt** (§ 266a StGB), **schwere Verstoesse gegen Arbeits-, Sozial- oder Umweltrecht** (Nr. 10 mit Verweis auf gesetzliche Pflichtverletzungen).
- Voraussetzung: **rechtskraeftige Verurteilung** oder bestandskraeftiger Bussgeldbescheid einer Leitungsperson **innerhalb der letzten 5 Jahre** (Selbstreinigungsmoeglichkeit § 125 GWB beachten).

**Bei Anhaltspunkten**: Auftraggeber muss **eigene Pruefung** durchfuehren; Eigenerklaerung des Bieters ist Ausgangspunkt, nicht Endpunkt.

### 5.2 Fakultative Ausschlussgruende (§ 124 GWB)

Der wichtigste praktische Streitpunkt:

- Nr. 1: Verstoss gegen Umwelt-, Sozial- oder Arbeitsrechtsvorschriften.
- Nr. 2: Insolvenzeroeffnung, Liquidation, Geschaeftstaetigkeitseinstellung.
- Nr. 3: nachweislich schwere Verfehlung, die seine Integritaet in Frage stellt.
- Nr. 4: Wettbewerbsverzerrende Absprachen (Kartellrecht, § 1 GWB).
- Nr. 5: Interessenkonflikt, der durch andere Mittel nicht behoben werden kann.
- Nr. 6: Wettbewerbsverzerrung aus vorheriger Beteiligung an der Vorbereitung des Verfahrens.
- Nr. 7: **erhebliche oder fortdauernde Maengel** bei der Erfuellung einer Vorgaengerleistung des oeffentlichen Auftraggebers, die zu vorzeitiger Beendigung, Schadenersatz oder vergleichbarer Rechtsfolge gefuehrt haben.
- Nr. 8: Vorlage falscher Erklaerungen, Verschleierung erheblicher Informationen.
- Nr. 9: Versuch der unzulaessigen Beeinflussung des Auftraggebers, Erlangung vertraulicher Informationen oder Fehlinformation.

**Anwendungsregel:** Fakultative Ausschluesse sind eine **Ermessensentscheidung** des Auftraggebers. Sie sind **begruendungspflichtig** und unterliegen vollumfaenglich der vergabekammergerichtlichen Kontrolle (Ermessensueberpruefung).

### 5.3 Selbstreinigung (§ 125 GWB)

- Der Bieter kann zwingenden oder fakultativen Ausschluss **abwenden** durch:
  - Schadenersatz oder Schadenswiedergutmachung.
  - Aktive Mitwirkung an der Aufklaerung (z. B. mit Behoerden).
  - Konkrete personelle, organisatorische und technische Massnahmen, die ein erneutes Fehlverhalten verhindern.
- Der Auftraggeber **prueft** die Selbstreinigung im Ermessenswege; bei rechtskraeftigem Ausschluss durch ein deutsches Gericht ist die Selbstreinigung weiterhin moeglich.
- **Wettbewerbsregister** (§ 6 WRegG): Auftraggeber **muss** ab geschaetzter Auftragswert oberhalb des relevanten Schwellenwertes Abfrage im Wettbewerbsregister beim Bundeskartellamt durchfuehren.

---

## Phase 6 — Wertungsentscheidung und Zuschlagskriterien (§ 127 GWB, § 58 VgV)

### 6.1 Wirtschaftlichstes Angebot

- **Maßstab: wirtschaftlichstes Angebot** (§ 127 Abs. 1 GWB, § 58 VgV). "Wirtschaftlichkeit" bezieht sich auf das **beste Preis-Leistungs-Verhaeltnis**, nicht nur auf den niedrigsten Preis. Reine Preisvergabe ist zulaessig, wenn die Qualitaet vorab durch Mindestanforderungen und Eignung **vollstaendig** standardisiert wurde.
- **Kein nachtraegliches Hinzufuegen** von Wertungskriterien oder Aenderung der Gewichtung (EuGH C-31/87 "Beentjes" und Folgerspr.).
- **Kein Mischen** von Eignung und Zuschlag (zwei-Stufen-Prinzip).

### 6.2 Wertungsmodelle

- **Einfache Punktwertung** mit klaren Bewertungsmaßstaeben.
- **UfAB-Modell** (Unterlagen fuer die Ausschreibung und Bewertung) — eingefuehrt vom Bundesministerium des Innern fuer IT-Vergaben, in Praxis weit verbreitet.
- **Eigenwirtschaftliche Modelle** mit Bonus-Malus-Systemen.
- **Lebenszykluskosten-Modell** (§ 59 VgV): Beruecksichtigung von Anschaffungs-, Nutzungs-, Wartungs-, Entsorgungskosten.

**Pruefraster Wertung:**

- Sind die Wertungspunkte **transparent dokumentiert**?
- Wird die **Bewertungsbegruendung** in der Vergabeakte konkret und nachvollziehbar?
- Werden **subjektive Bewertungselemente** durch zwei unabhaengige Wertende verifiziert?
- Sind **Konzepte** und **Praesentationen** sachlich anhand vorab veroeffentlichter Kriterien bewertet (kein Goodwill-Bonus, kein verstecktes Negativkriterium)?

### 6.3 Diskriminierung in der Wertung

Praxistypische Verstoesse:

- Bevorzugung eines Bestandsanbieters durch ueberraschend hohe Gewichtung von **Erfahrungen mit dem Auftraggeber**.
- "Heimatschutz": Standortvorgabe oder Sprachvoraussetzungen ueber das Erforderliche hinaus.
- **Bewertung der EEE**-Inhalte statt der Angebotsinhalte.
- Bewertung der **Eignungsmerkmale** als Zuschlagskriterium (Verbot der Doppelverwendung).

---

## Phase 7 — Vorabinformation (§ 134 GWB) und Stillhaltefrist

### 7.1 Pflicht des Auftraggebers

- **Schriftliche** Mitteilung an alle Bieter, deren Angebot **nicht** beruecksichtigt werden soll, **vor** Zuschlag:
  - Name des Zuschlagsbieters.
  - Gruende des Ausschlusses bzw. der Nichtberuecksichtigung.
  - Stillhaltefrist (siehe Phase 0 D).
- **Inhalt** muss so substantiiert sein, dass eine **fundierte Ruege und ein Nachpruefungsantrag** moeglich werden. Reine Floskeln wie "Ihr Angebot war nicht das wirtschaftlichste" reichen **nicht** (vgl. OLG Duesseldorf VII-Verg-Linie, EuGH-Transparenzgebot).

### 7.2 Stillhaltefrist (§ 134 Abs. 2 GWB)

- **15 Kalendertage** ab Absendung der Vorabinformation per Post.
- **10 Kalendertage** bei elektronischer Uebermittlung (E-Mail, eVergabe-Plattform).
- Zuschlag vor Ablauf der Stillhaltefrist ist **schwebend unwirksam** und kann bei rechtzeitig eingelegtem Nachpruefungsantrag **endgueltig nichtig** werden (§ 135 Abs. 1 Nr. 1 GWB).

### 7.3 Pruefraster Vorabinformation

- Wurde die Vorabinformation **schriftlich** und **rechtzeitig** versandt?
- Enthaelt sie die zwingenden Mindestangaben (§ 134 Abs. 1 GWB)?
- Ist die Begruendung **substantiiert**?
- Wurde die Stillhaltefrist **kalendertaggenau** dokumentiert?
- Wurde der **Zuschlag** vor Ablauf der Stillhaltefrist erteilt? Wenn ja: **Zuschlag unwirksam** nach § 135 GWB.

---

## Phase 8 — Ruege (§ 160 Abs. 3 GWB)

### 8.1 Ruegeobliegenheit als Zulaessigkeitsvoraussetzung

§ 160 Abs. 3 Satz 1 GWB legt vier alternative Ruegeobliegenheiten als **Zulaessigkeitsvoraussetzungen** des Nachpruefungsantrags fest:

1. **Nr. 1**: Vergaberechtsverstoss, der dem Bieter **bekannt** geworden ist — Ruege **innerhalb einer Frist von zehn Kalendertagen** ab Kenntnis (gesetzliche Frist, nicht der frueher gebraeuchliche dehnbare Begriff "unverzueglich"; aktuelle Fassung seit den GWB-Aenderungen durch das Vergaberechtsmodernisierungsgesetz und Folgegesetze).
2. **Nr. 2**: in der Bekanntmachung **erkennbarer** Verstoss — spaetestens bis Ablauf der Angebots- oder Teilnahmefrist.
3. **Nr. 3**: in den Vergabeunterlagen **erkennbarer** Verstoss — spaetestens bis Ablauf der Angebots- oder Teilnahmefrist.
4. **Nr. 4**: Nichtabhilfemitteilung des Auftraggebers — Nachpruefungsantrag innerhalb von **15 Kalendertagen**.

### 8.2 Konkretisierung "innerhalb von zehn Kalendertagen"

§ 160 Abs. 3 Satz 1 Nr. 1 GWB legt eine **starre gesetzliche Frist von zehn Kalendertagen** fest. Das ist **keine** dehnbare Vernunftfrist im Sinne des frueheren "unverzueglich"-Standards (§ 121 BGB) und **kein** Ermessensspielraum des Bieters. Nach Fristablauf ist der Nachpruefungsantrag wegen der versaeumten Ruege **praekludiert**, auch wenn die Verzoegerung sachlich nachvollziehbar war (Komplexitaet der Rechtsfrage, notwendige anwaltliche Vorpruefung, Akteneinsichtsbeduerfnis aendern an der Praeklusion **nichts**).

Folgen fuer die Mandatsfuehrung:

- Bei Fristdruck ist **lieber unvollstaendig und fristwahrend** zu ruegen als verspaetet vollstaendig.
- Die Ruege kann **nachgeschaerft** werden, wenn nach Akteneinsicht weitere Verstoesse erkennbar werden — diese **neuen** Verstoesse loesen jedoch jeweils eigene Zehn-Tages-Fristen aus.
- Bei mehreren parallelen Verstoessen empfiehlt sich eine **Sammelruege** mit ausdruecklichem Hinweis auf den Vorbehalt weiterer Ruegen nach Akteneinsicht.
- Im Schadensersatzmandat nach Phase 15 kann der Anspruch auch dann bestehen, wenn die Nachpruefungs-Ruegefrist verstrichen ist — die Praeklusion betrifft den Primaerrechtsschutz, nicht den Sekundaerrechtsschutz.

**Achtung:** Die Frist beginnt mit **positiver Kenntnis** der Tatsachen **und** der rechtlichen Bewertung als Vergaberechtsverstoss. Eine "Ahnung" loest die Frist **nicht** aus (BGH-Linie verifizierbar). Bei Akteneinsicht im laufenden Verfahren beginnt fuer **neu** erkennbare Verstoesse jeweils eine eigene Zehn-Tages-Frist.

### 8.3 Form und Inhalt der Ruege

- **Form**: keine spezifische Form vorgeschrieben, aus Beweisgruenden zwingend **schriftlich** mit Empfangsbestaetigung; in der Praxis E-Mail mit Lesebestaetigung oder eVergabe-Plattform-Nachricht.
- **Adressat**: Auftraggeber.
- **Inhalt**: konkrete Beschreibung des geruegten Verstosses, Norm, geforderte Abhilfe. Reine Allgemeinplaetze wie "Das Verfahren ist nicht transparent" sind **unzureichend**.

### 8.4 Pruefraster Ruege

- Wurde **fristgerecht** geruegt?
- Wurde die Ruege **konkret und nachweisbar** zugestellt?
- Hat der Auftraggeber **Abhilfe** geleistet oder die Abhilfe schriftlich **abgelehnt** (Nichtabhilfemitteilung)?
- Lauft jetzt die **15-Tage-Frist** des § 160 Abs. 3 Satz 1 Nr. 4 GWB ab welchem Datum?
- Wurden alle bekannten Verstoesse **kumulativ** geruegt? **Eine zu spaete Nachreichung weiterer Ruegen ist im Nachpruefungsantrag praekludiert.**

---

## Phase 9 — Nachpruefungsverfahren (§§ 155 ff. GWB)

### 9.1 Eroeffnung und Antragsschrift

- Antrag an die zustaendige **Vergabekammer**.
- **Antragsfrist**: 15 Kalendertage nach Eingang der Nichtabhilfemitteilung (§ 160 Abs. 3 Satz 1 Nr. 4 GWB).
- **Antragsbefugnis** (§ 160 Abs. 2 GWB): Interesse am Auftrag, Verletzung in eigenen Rechten nach § 97 Abs. 6 GWB, kausal moeglich gewordener Schaden.
- **Bestimmtheit** des Antrags und der Begruendung: Schluessigkeitsanforderungen mittel.

### 9.2 Suspensiveffekt (§ 169 Abs. 1 GWB)

- Mit Zustellung des Nachpruefungsantrags an den Auftraggeber tritt der **automatische Zuschlagsstopp** ein.
- Auftraggeber **darf nicht** zuschlagen, bis die Vergabekammer entscheidet oder den Suspensiveffekt aufhebt (§ 169 Abs. 2 GWB Eilantrag des Auftraggebers — strenge Voraussetzungen).
- **Anti-Suspensive-Antrag** des Auftraggebers nach § 169 Abs. 2 GWB ist in der Praxis selten erfolgreich; muss substantiieren, dass die Versagung des Zuschlagsstopps **ueberragend wichtigen Gemeinwohlbelangen** dient.

### 9.3 Aktenakteneinsicht (§ 165 GWB)

- Antragsteller hat Anspruch auf Akteneinsicht.
- **Geheimhaltungsantrag** des Auftraggebers oder eines Beigeladenen kann zur **teilweisen Schwaerzung** fuehren (Geschaeftsgeheimnis, § 165 Abs. 2 GWB iVm GeschGehG).
- **Strategie**: Akteneinsicht **fruehzeitig** beantragen, im Antrag konkret bezeichnen, was eingesehen werden soll.

### 9.4 Beigeladene Stellung des Zuschlagsbieters

- Der **vorgesehene Zuschlagsbieter** ist regelmaessig **notwendig beigeladen** (§ 162 GWB).
- Er hat **eigene Rechte**: Akteneinsicht, Stellungnahme, ggf. Antrag auf Geheimhaltung.

### 9.5 Muendliche Verhandlung und Entscheidung

- Vergabekammer entscheidet in der Regel **muendlich** mit anschliessender schriftlicher Begruendung.
- **Entscheidungsoptionen** (§ 168 GWB):
  - Aufhebung der Wertungsentscheidung.
  - Anordnung der Wiederholung des Verfahrens ab bestimmtem Stand.
  - Anordnung bestimmter Massnahmen (z. B. erneute Eignungspruefung).
  - Feststellung der **Unwirksamkeit** des Zuschlags (§ 135 GWB).
  - Verwerfung als unzulaessig oder Zurueckweisung als unbegruendet.

### 9.6 Frist fuer Entscheidung (§ 167 GWB)

- **5-Wochen-Regel**: Entscheidung soll binnen fuenf Wochen ab Eingang des Antrags ergehen.
- Verlaengerung **um angemessene Zeit** durch Vorsitzenden moeglich; in komplexen Verfahren auch mehrere Wochen ueberschreiten.

---

## Phase 10 — Sofortige Beschwerde (§§ 171 ff. GWB)

### 10.1 Statthaftigkeit und Frist

- Statthaft gegen Entscheidung der Vergabekammer.
- **Frist 2 Wochen** ab Zustellung der Entscheidung (§ 172 Abs. 1 GWB).
- **Begruendungsfrist** zugleich 2 Wochen ab Einlegung (§ 172 Abs. 3 GWB).
- Beschwerde **muss begruendet** sein und konkrete Beschwerdegruende benennen.

### 10.2 Suspensiveffekt der Beschwerde

- **Aufschiebende Wirkung** kraft Gesetzes hinsichtlich der Vergabekammerentscheidung (§ 173 GWB).
- Auftraggeber kann **Aufhebung** der aufschiebenden Wirkung beim OLG-Vergabesenat beantragen (Eilantrag).

### 10.3 Beschwerdeverfahren

- Vergabesenat des **OLG** entscheidet. Sechs Vergabesenate sind besonders prominent: OLG Duesseldorf (VII-Verg), OLG Karlsruhe (15 Verg), OLG Muenchen (Verg), OLG Celle (13 Verg), OLG Frankfurt (11 Verg), OLG Brandenburg (Verg).
- Streitwert wird nach **§ 50 Abs. 2 GKG iVm § 182 Abs. 3 GWB** ermittelt: typischerweise **5 Prozent** des Bruttoauftragswertes; Mindestwert 2.500 Euro.

### 10.4 Vorlage an EuGH und BVerfG

- Vorlage an EuGH bei unionsrechtlichen Auslegungsfragen ist regelmaessig **letztinstanzliche Pflicht** des OLG-Vergabesenats (Art. 267 Abs. 3 AEUV), sofern die Frage entscheidungserheblich ist.
- Verfassungsbeschwerde gegen vergaberechtliche OLG-Entscheidungen ist im Einzelfall moeglich, in der Praxis selten erfolgreich.

---

## Phase 11 — De-facto-Vergabe und Unwirksamkeit (§ 135 GWB)

### 11.1 Tatbestand

§ 135 Abs. 1 GWB erklaert oeffentliche Auftraege fuer **von Anfang an unwirksam**, wenn

- **Nr. 1**: der Auftraggeber gegen § 134 GWB (Vorabinformation, Stillhaltefrist) verstossen hat **und** dies in einem Nachpruefungsverfahren festgestellt wird;
- **Nr. 2**: der Auftraggeber **ohne vorherige Veroeffentlichung** einer Bekanntmachung im EU-Amtsblatt einen Auftrag vergeben hat, ohne dass dies nach GWB **gestattet** war (klassische De-facto-Vergabe).

### 11.2 Frist (§ 135 Abs. 2 GWB)

- **30 Kalendertage** ab Kenntnis des Verstosses, **spaetestens 6 Monate** nach Vertragsschluss.
- **Verkuerzung auf 30 Tage** ab Veroeffentlichung der Ex-ante-Bekanntmachung im EU-Amtsblatt (§ 135 Abs. 3 GWB) — Auftraggeber-Schutz-Mechanismus.

### 11.3 Rechtsfolge

- **Anfangsunwirksamkeit** ex tunc.
- Rueckabwicklung in Geld nach Bereicherungsrecht; gleichzeitig **Schadensersatzansprueche** des uebergangenen Bieters (§ 181 GWB iVm § 311 BGB analog).

### 11.4 Verteidigung des Auftraggebers

- **Inhouse-Argument** (§ 108 GWB): kein Vertragspartner ist ein "Unternehmen" im Sinne des Vergaberechts.
- **Eilbeduerftigkeit nach § 14 Abs. 4 Nr. 3 VgV**: "ausserordentliche Umstaende, die nicht von dem Auftraggeber zu vertreten sind" und die kein Verfahren mit Bekanntmachung zulassen.
- **Bagatell-Schwellenwert-Argument**: Auftragswertschaetzung unterhalb der EU-Schwelle.

---

## Phase 12 — Vergaberechtskonforme Vertragsanpassung (§ 132 GWB)

### 12.1 Grundsatz

Vertragsanpassung waehrend der Laufzeit ist **nicht frei**, sondern durch § 132 GWB **vergaberechtlich** begrenzt. Wesentliche Aenderungen sind **neue Auftraege** und muessen wiederum ausgeschrieben werden.

### 12.2 Tatbestaende der zulaessigen Aenderung

§ 132 Abs. 2 GWB nennt sechs Tatbestaende:

- Nr. 1: Aenderung war in den **urspruenglichen Vergabeunterlagen klar und eindeutig** vorgesehen (Optionsklausel, Preisgleitklausel).
- Nr. 2: **Zusatzleistungen** durch denselben Auftragnehmer, die wegen wirtschaftlicher oder technischer Verflechtung **erforderlich** sind; Wertgrenze 50 Prozent des urspruenglichen Auftragswertes je Aenderung.
- Nr. 3: **Unvorhersehbare Umstaende** (Naturkatastrophe, gesetzliche Aenderung).
- Nr. 4: Wesensaenderung **nicht** vorgenommen.
- Nr. 5: **De-Minimis**: Aenderung unter 10 Prozent des urspruenglichen Auftragswertes bei Liefer- und Dienstleistungsauftraegen, 15 Prozent bei Bauauftraegen und unterhalb des EU-Schwellenwertes.
- Nr. 6: Wechsel des Auftragnehmers durch **Insolvenz, Umwandlung, Restrukturierung**, wobei der Rechtsnachfolger die urspruenglichen Eignungsanforderungen erfuellt.

### 12.3 Wesentliche Aenderung (§ 132 Abs. 1 GWB)

Eine Aenderung ist **wesentlich**, wenn:

- die Bedingungen das Verfahren so geaendert haetten, dass andere Bieter zugelassen worden waeren;
- ein anderer Bieter den Zuschlag erhalten haette;
- das wirtschaftliche Gleichgewicht erheblich zugunsten des Auftragnehmers verschoben wird;
- der Auftrag erheblich erweitert wird;
- der Vertragspartner durch einen neuen ersetzt wird, soweit Nr. 6 oben nicht greift.

### 12.4 Rechtsfolge unzulaessiger Aenderung

- Behandlung als **De-facto-Vergabe** nach § 135 GWB.
- Nachpruefungsantragsmoeglichkeit fuer uebergangenen Marktteilnehmer mit 6-Monats-Frist (§ 135 Abs. 2 GWB).

---

## Phase 13 — Sektorenvergabe (SektVO) und Konzessionen (KonzVgV)

### 13.1 Sektorenauftraggeber (SektVO)

- Anwendung der SektVO oberhalb der **Sektoren-Schwellenwerte** (regelmaessig hoeher als die "klassischen" Schwellen).
- Anwendungsbereiche: Wasser, Energie (Strom, Gas, Waerme), Verkehr (Eisenbahn, Strassenbahn, Bus, Hafen, Flughafen), Postdienste.
- **Verfahrensarten** sind **freier** waehlbar: offenes Verfahren, nicht offenes Verfahren **und** Verhandlungsverfahren mit Bekanntmachung sind **gleichwertig**.
- **Eignung, Wertung, Zuschlag, Vorabinformation, Stillhaltefrist** sind analog zur VgV geregelt, mit sektorenspezifischen Abweichungen.

### 13.2 Konzessionen (KonzVgV)

- Bau- und Dienstleistungskonzessionen oberhalb der Konzessions-Schwelle.
- **Wesentlich**: Konzessionsgeber traegt **nicht** das Hauptrisiko; das **Betriebsrisiko** muss beim Konzessionsnehmer liegen (§ 105 GWB, EuGH C-274/09 "Privater Rettungsdienst Stadler"-Linie).
- Verfahrensregeln **flexibel**, aber Grundsaetze des Wettbewerbs, der Transparenz und der Gleichbehandlung gelten zwingend.
- **Schaedlich** in der Praxis: ueberproportionale Risikoabwaelzung auf den Konzessionsgeber durch versteckte Mindestumsatzgarantien oder Defizithaftungsklauseln — dann liegt **kein Konzessionsvertrag**, sondern **Dienstleistungsauftrag** vor.

---

## Phase 14 — Unterschwellenbereich und Haushaltsvergaberecht

### 14.1 UVgO und Landesrecht

- **UVgO 2017**: bundesweit eingefuehrt im Liefer- und Dienstleistungsbereich des Bundes und in den meisten Laendern.
- Landesvergabegesetze (LVergabeG): regeln zusaetzliche soziale und oekologische Anforderungen, Mindestloehne, Tariftreue, Frauenfoerderung.
- Bauauftraege im Unterschwellenbereich: **VOB/A Abschnitt 1**.

### 14.2 Verfahren im Unterschwellenbereich

- **Direktauftrag** (UVgO § 14): bis zur jeweiligen landes- bzw. bundesrechtlichen Wertgrenze.
- **Verhandlungsvergabe** (UVgO § 12): wenn die naechsten Bieter nicht ueber Direktauftrag erreichbar sind.
- **Beschraenkte Ausschreibung** (UVgO § 11): mit oder ohne Teilnahmewettbewerb.
- **Oeffentliche Ausschreibung** (UVgO § 9): Grundregel oberhalb der landes-/bundesrechtlichen Wertgrenze.

### 14.3 Rechtsschutz im Unterschwellenbereich

- **Kein GWB-Nachpruefungsverfahren**.
- Rechtsschutz ueber:
  - **Verwaltungsrecht** (Anfechtungs- oder Verpflichtungsklage gegen einen Verwaltungsakt, soweit der Vergabevorgang als Verwaltungsakt gestaltet ist).
  - **Zivilrecht** (Vertragsanbahnungshaftung, § 311 BGB iVm § 280 BGB).
  - **Verfassungsbeschwerde** bei evidenter Willkuer (BVerfG 1 BvR 1387/16 "Saechsische Vergabekammer" und Folgerspr.).
  - **Schadensersatz** ueber landeshaftungsrechtliche oder zivilrechtliche Anspruchsgrundlagen.

---

## Phase 15 — Schadensersatz (§ 181 GWB, § 280 BGB, § 33a, 33f GWB)

### 15.1 Anspruchsgrundlagen

- **§ 181 GWB** — **Vertrauensschadenersatz**: Anspruch des uebergangenen Bieters auf Ersatz der **Aufwendungen fuer die Vorbereitung des Angebots und die Teilnahme am Vergabeverfahren**, wenn der Auftraggeber gegen Vergabevorschriften verstossen hat, die den Schutz der Bieter bezwecken (§ 97 Abs. 6 GWB), und der Bieter **eine echte Chance** auf den Zuschlag hatte, die durch den Verstoss **beeintraechtigt** wurde. **Verschulden ist nach dem Gesetzeswortlaut nicht erforderlich**; ebenso wenig muss der Bieter beweisen, dass er **tatsaechlich** den Zuschlag erhalten haette. Es genuegt die Beeintraechtigung der **Zuschlagschance**. Diese Anspruchsgrundlage ist daher gerade in Faellen wertvoll, in denen Verschulden des Auftraggebers schwer nachzuweisen ist oder die Zuschlagskausalitaet nicht zwingend feststeht.
- **§ 280 Abs. 1 iVm §§ 311 Abs. 2, 241 Abs. 2 BGB** — **vorvertragliche Pflichtverletzung** (culpa in contrahendo): Anspruch auf negatives oder ggf. positives Interesse, **setzt Verschulden voraus**. Anwendbar neben § 181 GWB; in der Praxis insbesondere fuer den Ersatz **entgangenen Gewinns** (positives Interesse) bedeutsam, soweit die strenge Kausalitaetsanforderung gefuehrt werden kann.
- **§§ 33a, 33f GWB** — **kartellrechtlicher Schadensersatz** bei kollusivem Zusammenwirken (Submissionsabsprache, Bieterkartell): Anspruchsgrundlage auch fuer den uebergangenen Bieter, der durch die Absprache benachteiligt wurde.

### 15.2 Schadensumfang

- **§ 181 GWB — Vertrauensschaden**: Aufwendungen fuer die Angebotserstellung, Reisekosten fuer Besichtigungstermine, externe Fachberatung, anwaltliche Vorpruefung der Vergabeunterlagen, konkret nachgewiesene anteilige Gemeinkosten. **Kein** entgangener Gewinn (das ist nicht der Schutzzweck von § 181 GWB).
- **Entgangener Gewinn** (positives Interesse): nur ueber § 280 BGB iVm § 311 BGB **und** nur, wenn der Mandant **mit hoher Wahrscheinlichkeit** den Zuschlag erhalten haette (in der Rechtsprechung sehr hohe Kausalitaetsanforderungen).
- **Vorhaltepauschale** und kalkulatorische Gemeinkosten sind nur ersatzfaehig, soweit **konkret** nachweisbar (Mitarbeiterstunden, Materialkosten, Reise- und Besichtigungskosten).

### 15.3 Beweislast

- **§ 181 GWB**: Anspruchsteller muss den **Vergaberechtsverstoss**, die **echte Zuschlagschance** und den **konkreten Vertrauensschaden** beweisen. **Kein** Vollbeweis erforderlich, dass der Bieter den Zuschlag tatsaechlich erhalten haette — die Beeintraechtigung der **realen Chance** genuegt.
- **§ 280 BGB iVm § 311 BGB**: zusaetzlich Verschulden und Kausalitaet zum entgangenen Gewinn beweisen.
- **Beweiserleichterung** ueber Anscheinsbeweis bei dokumentierten Vergaberechtsverstoessen und naheliegender Bestplatzierung.
- **Akteneinsicht** in die Vergabeakte ist regelmaessig zentral fuer den Schadensnachweis; § 165 GWB-Akteneinsicht im Nachpruefungsverfahren bewahren und sichern.

### 15.4 Verjaehrung

- **3 Jahre** ab Schluss des Jahres, in dem der Anspruchsteller von dem Anspruch Kenntnis erlangt hat oder ohne grobe Fahrlaessigkeit haette erlangen muessen (§ 195 iVm § 199 BGB).

---

## Phase 16 — Akteneinsicht, Geschaeftsgeheimnis, Whistleblower

### 16.1 Akteneinsicht

- **Vergabekammerverfahren**: § 165 GWB; Antragsteller hat Anspruch, Beigeladene koennen Geheimhaltung verlangen.
- **Vor** Nachpruefungsverfahren: Auskunfts- und Akteneinsichtsanspruch nach UVI G (Bundesinformationsfreiheitsgesetz) oder Landes-Transparenzgesetzen; teilweise eingeschraenkt durch Geschaeftsgeheimnis-Vorbehalt.
- **VgV § 8 Vergabeakte**: Auftraggeber muss eine vollstaendige Vergabeakte fuehren; das ist die wichtigste Beweisquelle.

### 16.2 Geschaeftsgeheimnis (GeschGehG)

- Bieterangaben zu Preiskalkulation, Subunternehmerstruktur, Personalmodellen koennen Geschaeftsgeheimnisse darstellen.
- Auftraggeber muss bei Vorabinformation und Akteneinsicht **Schutz** und **Transparenz** abwaegen.

### 16.3 Whistleblower- und Hinweisgeberschutzgesetz (HinSchG)

- Hinweise auf Vergaberechtsverstoesse fallen in den sachlichen Anwendungsbereich des HinSchG (§ 2 Abs. 1 Nr. 4 HinSchG, Verstoesse gegen Vergaberecht).
- Schutz vor Repressalien fuer Hinweisgeber relevant fuer Mitarbeiter und Subunternehmer des Auftraggebers oder Zuschlagsbieters.

---

## Phase 17 — Outputformate und Schriftsatzbausteine

### 17.1 Pruefgutachten

Standardstruktur des Pruefgutachtens:

1. Sachverhalt mit Beleg-Verweisen (Bekanntmachung TED-Nr., Aufforderungsschreiben, Bietererklaerungen).
2. Anwendungsbereich (Phase 1).
3. Verfahrensart und Verfahrensschritte (Phase 0 B).
4. Pruefung nach den Phasen 2 bis 11.
5. Fristen-Sofortcheck mit kalendarischer Aufstellung.
6. Rechtliche Bewertung (Subsumtion).
7. Empfehlung (Ruege, Nachpruefungsantrag, Schadensersatzanspruch, Verteidigung).
8. Disclaimer.

### 17.2 Ruegeschreiben

- Adressat: Vergabestelle des Auftraggebers.
- Betreff: Vergabeverfahren <Bezeichnung>, <TED-Nr.>, Ruege gemaess § 160 Abs. 3 GWB.
- Sachverhalt knapp.
- Konkrete Verstossbenennung mit Norm.
- Abhilfeforderung mit Frist.
- Hinweis: Nachpruefungsantrag wird angekuendigt, falls Abhilfe nicht erfolgt.
- Unterschrift Rechtsanwalt mit Vollmacht.

### 17.3 Nachpruefungsantragsschrift

- Rubrum: Antragsteller, Antragsgegner, Beigeladener (vorgesehener Zuschlagsbieter).
- Antrag (Tenor): konkrete Massnahmen, z. B. "Es wird festgestellt, dass die Wertungsentscheidung vom <Datum> rechtswidrig ist. Die Antragsgegnerin wird verpflichtet, die Wertung unter Beachtung der Rechtsauffassung der Vergabekammer zu wiederholen."
- Sachverhalt.
- Zulaessigkeit: Antragsbefugnis § 160 Abs. 2 GWB, Ruege, Frist § 160 Abs. 3 Satz 1 Nr. 4 GWB.
- Begruendetheit: konkret nach Phasen 1 bis 11.
- Beweisangebote: Akteneinsicht, Zeugen, Sachverstaendige.
- Antrag auf Akteneinsicht.
- Antrag auf Beibehaltung des Suspensiveffekts (§ 169 GWB).
- Anlagen.

### 17.4 Sofortige Beschwerde

- Rubrum mit Verfahrensbezeichnung der Vergabekammer.
- Beschwerdeantrag.
- Beschwerdegruende: prozessuale Maengel der Vergabekammerentscheidung, materielle Rechtsfehler, Beweiswuerdigungsfehler.
- Antrag auf Beibehaltung der aufschiebenden Wirkung.

### 17.5 Schadensersatzklage

- Zustaendiges Gericht: Landgericht am Sitz des Auftraggebers.
- Klageantrag: Zahlung einer konkreten Geldsumme oder Feststellung der Schadensersatzpflicht.
- Klagegrund: § 181 GWB iVm § 280 BGB.
- Bezifferung mit Anlagen (Angebotskosten, Vorhaltepauschalen, ggf. entgangener Gewinn).

---

## Phase 18 — Vermeidung typischer Mandatsfehler

Diese Fehler treten in der Praxis besonders oft auf — und sie sind **alle vermeidbar**:

1. **Frist verpasst** — Ruege nicht innerhalb der gesetzlichen 10-Kalendertage-Frist des § 160 Abs. 3 Satz 1 Nr. 1 GWB ab Kenntnis. Folge: Nachpruefungsantrag wird als unzulaessig verworfen, **ohne** Ermessensspielraum der Vergabekammer.
2. **Ruege zu allgemein** — "Das Verfahren ist intransparent" reicht nicht. Konkreter Verstoss, konkrete Norm.
3. **Falsches Verfahren** — Antrag an Verwaltungsgericht statt Vergabekammer im Oberschwellenbereich.
4. **Falsche Zustaendigkeit** — Vergabekammer des Bundes statt Land oder umgekehrt.
5. **Antragsschrift unschluessig** — Antragsbefugnis nicht konkret dargelegt, Schaden nicht behauptet.
6. **Akteneinsicht zu spaet** — wer erst in der muendlichen Verhandlung Einsicht beantragt, kann nicht mehr substantiieren.
7. **Begruendung schwammig** — keine konkrete Bezugnahme auf die Vergabeakte.
8. **Mandant ueberraschend nicht angehoert** — bei Vorabinformation Mandant innerhalb der Stillhaltefrist nicht erreicht, Frist verstrichen.
9. **Selbstreinigung nicht vorbereitet** — bei drohendem Ausschluss nach §§ 123, 124 GWB die § 125 GWB-Selbstreinigung nicht dokumentiert.
10. **Zu langsame Reaktion auf Nichtabhilfemitteilung** — 15 Kalendertage sind keine Empfehlung, sondern Praeklusion.

---

## Phase 19 — Verwendung dieses Vollprüfungs

### 19.1 Mandatsannahme-Check

Bevor dieser Vollprüfung auf einen konkreten Sachverhalt angewendet wird:

- Liegen alle relevanten Unterlagen vor? (Bekanntmachung, Vergabeunterlagen, eigenes Angebot, Vorabinformation, ggf. Vergabeakte-Auszug.)
- Ist die Mandantenrolle eindeutig?
- Ist die naechste Frist bekannt?
- Ist die Honorarvereinbarung (RVG Anlage 1 Nr. 3200, 3201 Berufungsgebuehr, ggf. Stundenhonorar) abgeschlossen?

### 19.2 Anwendung in der Reihenfolge

Phasen 0 bis 19 werden **in der Reihenfolge** angewendet. Phase 0 ist **immer** zuerst zu pruefen — Fristen entscheiden ueber alles andere. Wenn die naechste Frist binnen weniger Tage ablaeuft, hat **Ruege** Vorrang vor weiterer Sachverhaltsaufklaerung; lieber unvollstaendig fristwahrend ruegen als verspaetet vollstaendig.

### 19.3 Ausgabe

Der Vollprüfung erzeugt aus dem Sachverhalt heraus:

- Eine **Fristenkarte** (Was, Wann, Bis Wann, Naechster Schritt).
- Ein **Pruefgutachten** in Gutachtenstil mit Subsumtion.
- **Schriftsatzbausteine** (Ruege, Nachpruefungsantrag, Beschwerde, Klage, je nach Mandantenrolle und Phase).
- Eine **Empfehlung** mit Eskalationsstufen.
- Einen **Aktenvermerk** zur Vergabeakte (bei Auftraggeber-Mandat).

---

## Phase 20 — Verifizierte Rechtsprechung — Hinweis

Die in diesem Vollprüfung zitierten Aktenzeichen und Entscheidungen sind als **bekannte Linien-Entscheidungen** kenntlich gemacht und nicht abschliessend. Vor Verwendung in einem realen Mandat ist jede Entscheidung **eigenstaendig zu verifizieren** ueber:

- BGH-Entscheidungsdatenbank (bundesgerichtshof.de).
- BVerfG-Entscheidungssammlung (bundesverfassungsgericht.de).
- EuGH-Entscheidungssammlung (curia.europa.eu).
- juris oder dejure mit gepruefter Volltextfreigabe.
- OLG-Vergabesenat-Datenbanken der einzelnen Bundeslaender.

**Verboten** ist die Verwendung von **BeckRS**, **IBR**, **VergabeR-Aufsaetzen**, **NZBau-Anmerkungen** oder **Kommentar-Zitaten** ohne eigene Verifikation der Primaerquelle. Diese Vergaberechts-Quellenhygiene ist im Berufsrecht (BORA, FAO) und in der RVG-Vereinbarung mit dem Mandanten dokumentiert.

---

## Phase 21 — Glossar wesentlicher Begriffe

- **eForms**: EU-weites maschinenlesbares Schema fuer Bekanntmachungen im TED, verpflichtend seit 25.10.2023.
- **TED**: Tenders Electronic Daily, EU-Amtsblatt-Bekanntmachungsdienst (ted.europa.eu).
- **DVAL**: Datenservice oeffentlicher Einkauf, deutscher Bekanntmachungsservice ueber bund.de.
- **eVergabe**: elektronische Vergabeplattform (eVergabe-Plattform des Bundes, deutsche Vergabeplattform DVAL der Laender, kommerzielle Plattformen).
- **VHB**: Vergabe- und Vertragshandbuch des Bundes.
- **VOB/A**: Vergabe- und Vertragsordnung Bauleistungen, Abschnitt A; gilt fuer das Vergabeverfahren bei Bauauftraegen.
- **VOB/B**: Vergabe- und Vertragsordnung Bauleistungen, Abschnitt B; gilt fuer den Bauvertrag.
- **SektVO**: Sektorenvergabeverordnung (Wasser, Energie, Verkehr, Postdienste).
- **KonzVgV**: Konzessionsvergabeverordnung.
- **VSVgV**: Vergabeverordnung Verteidigung und Sicherheit.
- **EEE**: Einheitliche Europaeische Eigenerklaerung.
- **Stillhaltefrist**: § 134 Abs. 2 GWB, 15 bzw. 10 Kalendertage zwischen Vorabinformation und Zuschlag.
- **Beigeladene**: vorgesehener Zuschlagsbieter im Nachpruefungsverfahren.
- **De-facto-Vergabe**: Vergabe ohne vorherige Bekanntmachung, vom Gesetz als anfangsunwirksam angesehen.
- **Inhouse-Geschaeft**: § 108 GWB; Auftragsvergabe an kontrollierte juristische Person ohne Anwendung des Vergaberechts.
- **Wettbewerbsregister**: § 6 WRegG; Abfragepflicht des Auftraggebers zur Identifikation rechtskraeftig festgestellter Wirtschaftskriminalitaet.

---

## Phase 22 — Zusammenfassende Pruefmatrix

| Phase | Pruefkriterium | Norm | Frist |
| --- | --- | --- | --- |
| 0 | Mandantenrolle, Verfahrensart, Frist-Sofortcheck | gesamt | sofort |
| 1 | Anwendungsbereich, Auftraggebereigenschaft, Auftragstyp | §§ 99, 100, 101, 103 GWB | — |
| 2 | Bekanntmachung, Vergabeunterlagen | §§ 121, 127 GWB, §§ 29 ff. VgV | bis Angebotsfrist |
| 3 | Eignung, Eignungsleihe | § 122 GWB, §§ 42 ff. VgV | bis Angebotsfrist |
| 4 | Angebotsoeffnung, Aufklaerung, Nachforderung | §§ 56, 57 VgV | nach Angebotsoeffnung |
| 5 | Ausschlussgruende, Selbstreinigung | §§ 123, 124, 125 GWB | bis Wertung |
| 6 | Wertungsentscheidung, Zuschlagskriterien | § 127 GWB, § 58 VgV | bis Vorabinformation |
| 7 | Vorabinformation, Stillhaltefrist | § 134 GWB | 10 bzw. 15 Kalendertage |
| 8 | Ruege | § 160 Abs. 3 GWB | 10 Kalendertage (gesetzlich, Nr. 1) |
| 9 | Nachpruefungsverfahren | §§ 155 ff. GWB | 15 Kalendertage nach Nichtabhilfe |
| 10 | Sofortige Beschwerde | §§ 171 ff. GWB | 2 Wochen |
| 11 | De-facto-Vergabe, Unwirksamkeit | § 135 GWB | 30 Kalendertage, max. 6 Monate |
| 12 | Vertragsanpassung | § 132 GWB | — |
| 13 | Sektoren, Konzessionen | SektVO, KonzVgV | analog |
| 14 | Unterschwellenbereich | UVgO, VOB/A 1. Abschnitt | landesrechtlich |
| 15 | Schadensersatz | § 181 GWB, § 280 BGB | 3 Jahre |
| 16 | Akteneinsicht, Geschaeftsgeheimnis, Hinweisgeber | § 165 GWB, GeschGehG, HinSchG | verfahrensbezogen |

---

## Phase 23 — Schnellverwendung in einem fremden Chatbot

Wer diesen Skill in einem allgemeinen Chatbot ausserhalb einer Skill-fähigen Umgebung nutzt, geht so vor:

1. Diese gesamte Markdown-Datei in den Chatbot-Kontext laden (als Anhang oder per Copy-Paste in die erste Nachricht).
2. Ergaenzen: "Du bist Volljurist und arbeitest streng nach diesem Pruefraster. Halte die Quellenhygiene ein."
3. Mit dem Sachverhalt fortfahren: Bekanntmachung TED-Nr., Aufforderungsschreiben, Vergabeunterlagen, Angebot, Vorabinformation, ggf. Nichtabhilfemitteilung, ggf. Vergabekammer-Entscheidung.
4. Bei jedem Output **Frist** zuerst pruefen, dann Sache.
5. Zitierte Aktenzeichen vor Verwendung im realen Mandat **selbst** in BGH-, BVerfG-, EuGH-, juris- oder dejure-Datenbank verifizieren.

---

## Phase 24 — Abschluss-Disclaimer

Dieser Vollprüfung ersetzt **nicht** die anwaltliche Pruefung der Originalunterlagen, **nicht** die Mandatsuebernahme im Einzelfall und **nicht** die Verifikation aller Tatsachen, Aktenzeichen und Fristen. Er ist ein **Pruefraster zur Vorbereitung der anwaltlichen Bearbeitung**.

Verwendung im realen Mandat **nur** durch zugelassenen Rechtsanwalt mit eigener Sachverhaltskenntnis, eigener Fristenkontrolle und eigener Quellenverifikation.
