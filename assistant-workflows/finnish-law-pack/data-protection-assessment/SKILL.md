---
name: "data-protection-assessment"
description: "Assess planned personal data processing under the GDPR and the Finnish Data Protection Act: lawful basis, processing principles, special category data, and whether a data protection impact assessment (DPIA) is required."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Aku Nikkola"
  language: "Finnish"
  mike-display-name: "Data Protection Assessment"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Data Protection"
  jurisdictions: "Finland, European Union"
---
# Tietosuoja-arviointi

Tämä työnkulku tuottaa tarkistettavan arvion, ei oikeudellista neuvontaa. Korkean riskin käsittely, arkaluonteiset tiedot ja DPIA:n johtopäätökset kuuluvat tietosuojavastaavalle ja tarvittaessa juristille.

## Ohjeet

Arvioi henkilötietojen käsittelyn tietosuojavaatimukset. Sovellettava sääntely on EU:n yleinen tietosuoja-asetus (EU) 2016/679 (GDPR), jota tietosuojalaki (1050/2018) täsmentää ja täydentää kansallisesti. Työelämän käsittelyyn sovelletaan lisäksi lakia yksityisyyden suojasta työelämässä (759/2004) — se on pakottavaa, työnantajaa sitovaa sääntelyä. Älä viittaa kumottuun henkilötietolakiin (523/1999) voimassa olevana.

Jos käytettävissä on suomalaisen oikeuden hakulähde (esimerkiksi Finlex-tietokanta tai oikeudellinen hakutyökalu), tarkista kansallisen lain pykälät ja GDPR-artiklaviittaukset ajantasaisesta lähteestä ennen lopullista vastausta. Jos hakulähdettä ei ole käytettävissä, älä esitä säännöksen sisältöä varmana: merkitse viittaus muotoon [tarkistettava] ja pyydä käyttäjää toimittamaan ajantasainen säädösteksti.

### Vaihe 1: Kuvaa käsittely

1. Mitä henkilötietoja käsitellään ja keneltä (rekisteröityjen ryhmät)?
2. Mihin tarkoitukseen ja missä kontekstissa?
3. Kuka on rekisterinpitäjä; onko käsittelijöitä (alihankkijat, pilvipalvelut — 28 art edellyttää käsittelysopimusta)?
4. Siirretäänkö tietoja EU/ETA:n ulkopuolelle?
5. Onko kyse erityisistä henkilötietoryhmistä (terveys, etninen alkuperä, vakaumus, ay-jäsenyys, geneettiset ja biometriset tiedot, seksuaalinen suuntautuminen) tai rikostiedoista (10 art)?

### Vaihe 2: Määritä käsittelyperuste (GDPR 6 art)

Jokaisella käsittelyllä on oltava vähintään yksi peruste:

- Suostumus (6(1)(a)) — vapaaehtoinen, yksilöity, tietoinen, peruutettavissa. Heikko peruste työsuhteessa epätasapainon vuoksi.
- Sopimus (6(1)(b)) — käsittely tarpeen sopimuksen täyttämiseksi.
- Lakisääteinen velvoite (6(1)(c)).
- Elintärkeä etu (6(1)(d)).
- Yleinen etu / julkinen valta (6(1)(e)) — viranomaistoiminta.
- Oikeutettu etu (6(1)(f)) — edellyttää tasapainotestiä; ei sovellu viranomaisen tehtävien hoitoon.

Erityiset henkilötietoryhmät (9 art): käsittely on lähtökohtaisesti kielletty, ellei jokin 9(2) artiklan poikkeus sovellu (esim. nimenomainen suostumus, työoikeuden velvoitteet, tärkeä yleinen etu). Tarkista myös tietosuojalain kansalliset täsmennykset. Merkitse valittu peruste ja perustele; suostumuksesta dokumentoi vapaaehtoisuus, oikeutetusta edusta tasapainotesti.

### Vaihe 3: Tarkista käsittelyn periaatteet (GDPR 5 art)

Käy läpi: lainmukaisuus, kohtuullisuus ja läpinäkyvyys; käyttötarkoitussidonnaisuus; tietojen minimointi; täsmällisyys; säilytyksen rajoittaminen (määrittele säilytysaika); eheys ja luottamuksellisuus; osoitusvelvollisuus (dokumentointi). Nosta esiin, jos jokin periaate ei toteudu.

### Vaihe 4: Arvioi DPIA-tarve (GDPR 35 art)

Vaikutustenarviointi on tehtävä, kun käsittely todennäköisesti aiheuttaa korkean riskin rekisteröidyn oikeuksille. Tyypilliset liput:

- Laaja arkaluonteisten tietojen käsittely.
- Järjestelmällinen ja laaja-alainen seuranta (esim. profilointi tai automaattinen päätöksenteko oikeusvaikutuksin, 22 art).
- Henkilöiden järjestelmällinen valvonta yleisellä alueella.
- Uudet teknologiat, laaja rekisteröityjen joukko, haavoittuvat ryhmät (lapset, työntekijät, potilaat).

Kehota tarkistamaan myös tietosuojavaltuutetun toimiston julkaisema lista käsittelytoimista, jotka edellyttävät DPIA:ta. Jos DPIA tarvitaan, kuvaa sen rakenne (käsittelyn kuvaus, tarpeellisuus ja oikeasuhtaisuus, riskit, toimenpiteet) ja muistuta ennakkokuulemisesta (36 art), jos jäännösriski on korkea.

### Vaihe 5: Johtopäätös

Tuota tiivis arvio: 1) saako käsitellä — peruste (6/9 art) ja perustelu; 2) periaatteiden täyttyminen ja havaitut puutteet; 3) DPIA-tarve: kyllä / ei / rajatapaus perusteluineen; 4) seuraavat toimet: mitä on dokumentoitava (seloste käsittelytoimista, 30 art), miten rekisteröityjä informoidaan (13–14 art) ja mikä vaatii asiantuntijan arvion — merkitse [varmista].

## Rajaukset

- Älä vahvista GDPR-artikloja tai tietosuojalain pykäliä muistista — lähteestä tai [tarkistettava].
- Työnkulku ei laadi valmista vaikutustenarviointia eikä ennakkokuulemista — se arvioi vain DPIA:n tarpeen ja antaa rakenteen.
- Työnkulku ei tee ilmoituksia valvontaviranomaiselle eikä korvaa tietoturvaloukkauksen 72 tunnin ilmoitusta (33 art); korkean riskin loukkauksesta ilmoitetaan myös rekisteröidylle (34 art).
- Tietoturvan tekninen toteutus ei kuulu tähän työnkulkuun — vain turvatoimien tarpeen tunnistaminen.
