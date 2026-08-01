---
name: "urh-quellen-livecheck"
description: "Wenn es um Rechtsquellen-Livecheck in Fachanwalt Urheber Medienrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Klotzkette"
  language: "German"
  mike-display-name: "Urh Quellen Livecheck"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Copyright and Media Law"
  jurisdictions: "Germany"
---

# Rechtsquellen-Livecheck

## Einsatzlage

Dieser Quellen-Livecheck für **Fachanwalt Urheber Medienrecht** trennt amtliche Normfassung, frei prüfbare Rechtsprechung, Behördenhinweise, Formularstand und offene Aktualitätsrisiken.

## Fachlandkarte dieses Plugins

- `abmahnung-sonderfall-edge-case` — Abmahnung Sonderfall Bild Eigenen
- `erstgespraech-mandatsannahme` — Erstgespraech Mandatsannahme Fachanwalt
- `workflow-mandantenkommunikation` — FA Urheber Medien Mandant Redteam Gate
- `einstieg-schnelltriage-fallrouting` — FA Urheber Medien Start Chronologie Fristen
- `erstpruefung-und-mandatsziel` — Fachanwalt Gewerblicher Kanzlei
- `filesharing-stoererhaftung` — Filesharing Stoererhaftung
- `filmrecht-paragraf-89-urhg` — Filmrecht Paragraf 89 Urhg
- `gegendarstellung-fehlerkatalog` — Gegendarstellung Fehlerkatalog
- `gegendarstellung-presse` — Gegendarstellung Presse Mandat Triage
- `gegendarstellung-presse` — Gegendarstellung Presse MOD Erklaerung
- `link-haftung-paragraf-7-tmg` — Link Haftung Paragraf 7 TMG
- `medienrecht-fristen-form-und-zustaendigkeit` — Medienrecht Lizenzvertrag Urhmr
- `medienstaatsvertrag-quellenkarte` — Medienstaatsvertrag Quellenkarte
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Tragende Normen (KUG, UWG, UrhG) zuerst amtlich verifizieren: gesetze-im-internet.de oder spezialisiertes Bundesgesetzblatt-Portal; nicht aus Modellwissen finalisieren.
- Rechtsprechung nur mit vollständiger Zitatkette: Gericht, Senat, Entscheidungsform, Datum, Aktenzeichen, Fundstelle (BGHZ/BVerfGE/amtl. Sammlung) und frei prüfbare Quelle (dejure.org, openJur, Pressemitteilungen des Gerichts, BGH-/BVerfG-Datenbank).
- Paywall-Quellen (juris, beck-online) nicht als alleinige Verifikation nutzen; immer eine freie Bestätigung beilegen.
- Dynamische Bereiche im Fachanwalt Urheber Medienrecht (Rechtsverordnungen, Verwaltungspraxis, Mietspiegel, Tarife) gesondert tagesaktuell prüfen, weil Modellwissen veraltet ist.
- Quellenstand und offene Unsicherheit im Output sichtbar machen — kein Pseudo-Zitat ohne Live-Check.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
