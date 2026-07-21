---
name: "document-table-comparison"
description: "Compare multiple similar legal documents side by side or extract structured tables from a single document, with every cell sourced to a document location, given a confidence score, and gaps marked explicitly instead of left blank."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Aku Nikkola"
  language: "Finnish"
  mike-display-name: "Document Table Comparison"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "General Practice"
  jurisdictions: "Finland"
---
# Taulukkokatsaus

Muuta joukko asiakirjoja tarkistettavaksi taulukoksi: **jokainen solu kertoo, mistä asiakirjan kohdasta se on otettu ja kuinka varma poiminta on** — kuten kokenut juristi tekee sopimussalkun yhteenvedon, vuokra-abstraktin tai due diligence -matriisin. Lopputuote on Markdown-taulukko (tai useita), ei muistio.

Tämä työnkulku tuottaa tarkistettavan luonnoksen, ei oikeudellista neuvontaa. Lopullinen arvio kuuluu ihmisjuristille.

## Ohjeet

**Periaate: joka solu on lähteistetty.** Jokainen solu saa kolme asiaa:

1. **Arvo** — sanatarkka, kun solu on tekstiä; numero numerona; päivämäärä muodossa VVVV-KK-PP; rahamäärä summana ja valuuttana.
2. **Lähde** — asiakirjan kohta: `5.2 §`, `liite 1 kohta 3`, `s. 4 toinen kappale`. Jos arvo on päätelty, lähde on `johdettu kohdasta 9.1` — ei koskaan tyhjä.
3. **Luottamus** — luku 0.0–1.0. Alle 0.7 nostetaan ihmisen tarkistukseen.

**Puuttuva tieto merkitään `ei mainittu`** — ei tyhjäksi soluksi. Tyhjä solu peittää aukon; "ei mainittu" tekee siitä löydöksen.

Kaksi käyttötapaa:

- **Tila A — monidokumenttivertailu:** samantyyppiset asiakirjat rinnakkain, rivi per asiakirja, sarake per vertailukohta. Teho on poikkeaman näkeminen — se yksi sopimus, jossa ehto poikkeaa tai puuttuu.
- **Tila B — yhden asiakirjan rakenteinen poiminta:** asiakirjan taulukkomaiset rakenteet omiksi taulukoikseen (maksuaikataulu, omistus- tai lunastustaulukko, vuokra-abstrakti, liite- ja rasiteluettelo). Useita taulukoita, ei yhtä.

### Vaihe 1 — Sarakkeiden suunnittelu

Tila A: määritä asiakirjatyyppi ja johda sarakkeet siitä, mikä tyypissä on olennaista — tyypillisesti osapuolet, kohde, kesto, hinta/vastike, irtisanominen, vastuunrajoitus, salassapito, sovellettava laki, riidanratkaisu; työsopimuksissa lisäksi koeaika ja kilpailukielto, vuokrasopimuksissa vuokrankorotusmekanismi ja vakuus. Tila B: käy asiakirja läpi ja tunnista jokainen taulukkomainen rakenne; ehdota kaikki tuotettavat taulukot ennen täyttöä. **Uskolliset sarakeotsikot:** käytä asiakirjan omaa termiä (jos asiakirja sanoo "vastike", älä nimeä saraketta "vuokraksi"). Jos asiakirjatyyppiä tai vertailtavaa joukkoa ei voi määrittää, kysy ennen jatkamista.

### Vaihe 2 — Täyttö solu kerrallaan

- Sanatarkkuus: kun solu on ehdon sanamuoto, lainaa asiakirjaa, älä parafrasoi.
- Ei rivien paisuttelua: kolme osapuolta = kolme riviä, ei täyterivejä.
- Määritellyt termit ja lyhenteet: lisää määritelmätaulukko (termi → merkitys → lähde).
- Rahamäärät valuuttoineen; määräajat yksikköineen (päivää / kuukautta / arkipäivää); epäselvyys laskee luottamusta.

### Vaihe 3 — Kaksi oikeellisuuden tasoa

- **Taso 1 — mitä asiakirja sanoo (korkea luottamus):** arvo on poimittu asiakirjasta. Tämä on työnkulun ydinalue.
- **Taso 2 — onko ehto pätevä tai lainmukainen:** älä arvioi muistista. Jos käytettävissä on suomalaisen oikeuden hakulähde (esimerkiksi Finlex-tietokanta tai oikeudellinen hakutyökalu), tarkista relevantti säännös sieltä ja merkitse solun luottamus matalaksi; muuten merkitse arvio [tarkistettava] ja pyydä ajantasainen säädösteksti. Esimerkki: kilpailukieltosarakkeessa ehdon *sisältö* on tason 1 poiminta, mutta "kestääkö lain" on tason 2 kysymys (työsopimuslaki (55/2001) 3 luku 5 §; korvausvelvollisuus lisätty lailla 1018/2021).

### Vaihe 4 — Poikkeamat ja aukot

Tuota taulukon jälkeen lyhyt poikkeamalista: poikkeava rivi (esim. yksi sopimus 12 kuukauden irtisanomisajalla muiden ollessa 3 kuukautta), puuttuva pakollinen kohta (`ei mainittu` kohdassa, jonka asiakirjatyypin pitäisi kattaa, esim. sovellettava laki), sisäinen ristiriita saman asiakirjan solujen välillä. Poikkeama on riskisignaali ihmisen arvioitavaksi, ei johtopäätös.

### Ulostulo ja yhteenveto

Tuota Markdown-taulukot, joissa lähde- ja luottamustieto on mukana (omina sarakkeina tai solun perässä). Lopuksi lyhyt yhteenveto: aineisto ja tila (A/B), taulukoiden otsikot, rivi- ja solumäärät, lähteistämättömiä soluja 0, poikkeamat ja aukot sekä tarkistettavat kohdat (luottamus alle 0.7 tai tason 2 arvio).

## Rajaukset

- Ei solua ilman lähdettä; puuttuva tieto on `ei mainittu`, ei tyhjä.
- Ei pätevyys- tai lainmukaisuusarviota muistista.
- Ei keksittyjä rivejä tai sarakkeita, joita asiakirjat eivät tue.
- Ei lopullisia oikeudellisia johtopäätöksiä eikä yksittäisen asiakirjan syvätarkistuksen korvaamista.
- Vain Suomen oikeus (ja erikseen todettu EU-oikeus).
