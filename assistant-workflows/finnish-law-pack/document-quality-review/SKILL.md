---
name: "document-quality-review"
description: "Systematic multi-phase quality review of a Finnish legal document before signing, sending, or filing: context, structure, language, internal integrity, legal accuracy, gap analysis, risk signals, and a readiness verdict with severity-rated findings."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Aku Nikkola"
  language: "Finnish"
  mike-display-name: "Document Quality Review"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "General Practice"
  jurisdictions: "Finland"
---
# Asiakirjan tarkistus

Tämä työnkulku tuottaa tarkistettavan luonnoksen, ei oikeudellista neuvontaa. Lopullinen arvio kuuluu ihmisjuristille.

## Ohjeet

Tarkista juridinen asiakirja (sopimus, lausunto, valitus, hallintopäätös, muistio, luonnos) järjestelmällisesti vaiheissa 1–8 ennen käyttöä. Perusteellisuus menee nopeuden edelle. Raportoi jokainen löydös muodossa:

- **Vakavuus**: Kriittinen / Merkittävä / Vähäinen
- **Vaihe ja sijainti**: pykälä, kohta tai sivu
- **Kuvaus ja miksi merkityksellinen**: ongelma ja sen vaikutus tai riski
- **Korjausehdotus**: konkreettinen korjaus
- **Luottamus**: Korkea / Keskitaso / Matala — Matala, jos kohta vaatii lähteen tai asiantuntijan tarkistuksen

### Vaihe 1 — Konteksti

Selvitä asiakirjatyyppi ja sen vakiintuneet vaatimukset, jurisdiktio ja oikeudenala (Suomen oikeus, EU-oikeus, Ahvenanmaan erityisasema), osapuolet ja lukijat valta-asemineen (esim. kuluttaja vs. elinkeinonharjoittaja), asiakirjan tarkoitus sekä panokset, jos se epäonnistuu. Jos tyyppiä tai jurisdiktiota ei voi määrittää, kysy käyttäjältä ennen jatkamista.

### Vaihe 2 — Käytettävyys ja rakenne

Palveleeko muoto käyttöä: löytääkö lukija olennaisen; ovatko velvoitteet, oikeudet, määräajat ja toimet selvästi merkitty? Taloudelliset sitoumukset (hinnat, irtisanomis- ja peruutusehdot, automaattiset jatkumiset, korotusmekanismit) näkyvästi esillä, ei haudattuna.

### Vaihe 3 — Kieli ja ilmaisu

Monitulkintaiset ilmaukset ("kohtuullinen aika", "viipymättä", "olennainen") — määritelty tai sidottu kontekstiin? Johdonmukainen termistö: samasta asiasta sama termi, ei synonyymeja. Vääräperäinen täsmällisyys: lupaako teksti tarkkuutta, jota ei voi toteuttaa; näyttävätkö esimerkkiluettelot tyhjentäviltä (lisää "muun muassa")? Oikeinkirjoitus ja pykäläviittausten muoto.

### Vaihe 4 — Rakenteellinen eheys

Sisäiset viittaukset osoittavat olemassa oleviin kohtiin, ei orpoja eikä kehäviittauksia. Numerointi juokseva, ei kaksoiskappaleita. Määritellyt termit määritelty ja käytetty johdonmukaisesti; ei käyttämättömiä tai ristiriitaisia määritelmiä. Hauraat ulkoiset viittaukset (olennainen sisältö yksipuolisesti muutettavan linkin takana) merkitään. Liitteet, allekirjoituslohkot ja osapuolitiedot täydellisiä.

### Vaihe 5 — Sisällöllinen oikeellisuus

**Taso 1 — sisäinen (korkea luottamus):** kohtien keskinäinen johdonmukaisuus; laskelmat, summat ja päivämäärät täsmäävät; määräaikalaskenta oikein (arkipäivät vs. kalenteripäivät, pyhät, viikonloppuun osuva määräpäivä); ei viittauksia kumottuun lakiin tai lakkautettuun viranomaiseen.

**Taso 2 — ulkoiset oikeuslähteet:** säädösnumerot, pykälät, ratkaisutunnukset ja HE-viittaukset sekä ristiriita pakottavan lainsäädännön kanssa (esim. työsopimuslaki, kuluttajansuojalaki). Jos käytettävissä on suomalaisen oikeuden hakulähde (esimerkiksi Finlex-tietokanta tai oikeudellinen hakutyökalu), tarkista nämä ajantasaisesta lähteestä ennen lopullista vastausta. Jos hakulähdettä ei ole, älä vahvista viittausta muistista: merkitse se [tarkistettava], anna löydökselle Luottamus: Matala ja pyydä käyttäjää toimittamaan ajantasainen säädösteksti.

### Vaihe 6 — Täydellisyys ja aukot

Puuttuvat vakiolausekkeet (sovellettava laki, riidanratkaisu, voimassaolo, irtisanominen, vastuunrajoitus). Hiljaisuus, joka sattuu: velvoite ilman vastuutahoa; oikeus ilman seuraamusta rikkomisesta; ehtojen etusijajärjestys ristiriidassa; siirtymämekaniikka tilasta A tilaan B. Skenaariotestaus: sopimusrikkomus, viivästys, ylivoimainen este, irtisanominen. Asiakirjatyypin pakolliset osat: valitukselta vaatimukset, perusteet ja määräaika; hallintopäätökseltä perustelut ja muutoksenhakuohje (hallintolaki).

### Vaihe 7 — Riski ja pätevyys (riskisignaalit, ei johtopäätöksiä)

Pätemättömyys- tai sovitteluriski: oikeustoimilain (228/1929) 36 §:n kohtuullistaminen, pakottava kuluttajansuoja, työoikeuden pakottavuus, kilpailukieltojen rajat, sopimussakon kohtuullisuus. Loogiset virheet: mahdoton ehto, näennäisesti molemminpuolinen mutta epäsymmetrinen velvoite, poikkeus joka nielee pääsäännön. Epäjohdonmukaiset kynnysarvot ja määräajat; toisaalla annettu ja toisaalla kumottu oikeus. Yksipuolisuus ja heikomman osapuolen suoja. Kaikki tämän vaiheen löydökset ovat asiantuntijan arviota vaativia signaaleja.

### Vaihe 8 — Valmius käyttöön

Jäljellä olevat [TÄYDENNÄ]-kohdat, kirjoitusvirheet, allekirjoitus- ja jättövalmius, viranomaisen tai tuomioistuimen muotovaatimukset, sävy. Onko aiempien vaiheiden kriittiset löydökset ratkaistu?

## Loppuraportti

Tuota lopuksi: löydöstaulukko (tunnus, vakavuus, vaihe, sijainti, ongelma), lukumäärät vakavuuksittain, kokonaisarvio asteikolla *Valmis käyttöön / Valmis ehdolla / Ei valmis*, kriittiset löydökset, asiantuntijan tarkistusta vaativat kohdat ja priorisoidut seuraavat toimet. Viittaa säädöksiin muodossa: lain nimi ja säädösnumero ensimaininnassa (esim. työsopimuslaki (55/2001)), sen jälkeen vakiintunut lyhyt muoto ja tarkka kohta (esim. TSL 7:2); oikeustapaukset tunnisteella (esim. KKO 2024:15); epävarmat viittaukset [tarkistettava].

Työnkulku ei tee lopullisia oikeudellisia johtopäätöksiä, ei korjaa asiakirjaa puolestasi eikä takaa kaikkien riskien löytymistä; se kattaa vain Suomen oikeuden ja erikseen todetun EU-oikeuden.
