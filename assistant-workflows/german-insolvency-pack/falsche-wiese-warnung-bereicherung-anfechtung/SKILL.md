---
name: "falsche-wiese-warnung-bereicherung-anfechtung"
description: "When Falsche-Wiese-Warnung: Bereicherung und Anfechtung in Restitution and Avoidance Law is required: checks deadline, form, jurisdiction, legal remedy, and immediate measures; produces a deadline and risk indicator with immediate action steps."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Falsche Wiese Warnung Bereicherung Anfechtung"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Restitution and Avoidance Law"
  jurisdictions: "Germany"
  source-plugin: "bereicherungs-und-anfechtungsrecht-pruefer"
---

# Falsche-Wiese-Warnung: Bereicherung und Anfechtung

## Triage — kläre vor dem Hinweis

1. Hat der Nutzer einen nichtigen Vertrag als Anspruchsgrundlage für eine Rückzahlung genannt?
2. Besteht ein wirksamer Rechtsgrund für die Leistung, sodass § 812 BGB tatbestandlich nicht greift?
3. Ist der Nutzer Insolvenzverwalter (→ §§ 129 ff. InsO) oder Einzelgläubiger mit Titel (→ AnfG)?
4. Befindet sich die Sache noch im Eigentum des Berechtigten (→ § 985 BGB vorrangig)?
5. Wird Schadensersatz begehrt, obwohl es sich um Bereicherungsrecht handelt (kein Verschulden erforderlich)?

## Zentrale Normen

§ 812 Abs. 1 BGB (Leistungskondiktion, Nichtleistungskondiktion) — §§ 134, 138, 142 BGB (Nichtigkeitsgründe) — §§ 129 ff. InsO (Insolvenzanfechtung) — §§ 1 ff. AnfG (Gläubigeranfechtung außerhalb InsO) — § 985 BGB (Herausgabeanspruch des Eigentümers) — § 2 AnfG (Vollstreckungstitel Voraussetzung)

## Rechtsprechung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Falschverortung 1: Vertrag statt Bereicherungsrecht

**Fehler:** Nutzer begehrt Rückzahlung einer Leistung, stützt sich aber auf den unwirksamen Vertrag selbst.

**Konsequenz:** Ist der Vertrag nichtig (§§ 134, 138, 142 BGB), gewährt er keinen Rückzahlungsanspruch. Anspruchsgrundlage: §§ 812 ff. BGB.

## Falschverortung 2: Bereicherungsrecht statt Anfechtung

**Fehler:** Die Leistung hatte einen wirksamen Rechtsgrund. Nutzer greift dennoch zu § 812 BGB.

**Richtiger Pfad:** Anfechtung nach AnfG oder §§ 129 ff. InsO bei Gläubigerbenachteiligung.

## Falschverortung 3: AnfG statt InsO-Anfechtung

**Fehler:** Nutzer ist Insolvenzverwalter, stützt sich aber auf das AnfG.

**Konsequenz:** §§ 129 ff. InsO gelten nach Verfahrenseröffnung; AnfG gilt außerhalb für Einzelgläubiger mit Titel (§ 2 AnfG).

## Falschverortung 4: InsO-Anfechtung statt AnfG

**Fehler:** Nutzer ist Einzelgläubiger mit Vollstreckungstitel, greift aber zu § 129 InsO.

**Konsequenz:** §§ 129 ff. InsO stehen nur dem Insolvenzverwalter zu.

## Falschverortung 5: Bereicherungsrecht bei Vindikation

**Fehler:** Sache befindet sich noch im Eigentum des Berechtigten; Nutzer klagt aus § 812 BGB statt aus § 985 BGB.

**Konsequenz:** § 812 BGB greift subsidiär; § 985 BGB ist vorrangig.

## Output-Template

**Weichenstellung-Warnung: richtige Anspruchsgrundlage?**

Sachverhalt (kurz): [...]

| Falschverortung | Prüfung | Ergebnis |
|---|---|---|
| Nichtiger Vertrag als AGr | Vertrag nichtig (§§ 134/138/142)? | ja → §§ 812 ff. BGB |
| § 812 BGB trotz wirksamer Schuld | Rechtsgrund besteht? | ja → Anfechtung prüfen |
| AnfG statt InsO | Insolvenzverfahren eröffnet? | ja → §§ 129 ff. InsO |
| § 129 InsO als Einzelgläubiger | Kein Insolvenzverfahren? | ja → AnfG (§ 2 Titel!) |
| § 812 statt § 985 | Eigentum noch vorhanden? | ja → § 985 BGB vorrangig |

**Empfehlung:** Richtige Anspruchsgrundlage: [...]

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

