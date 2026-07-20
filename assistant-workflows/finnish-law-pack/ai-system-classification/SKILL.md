---
name: "ai-system-classification"
description: "Classify an AI system under the EU AI Act (Regulation (EU) 2024/1689): prohibited practice, high-risk (Annex III or Annex I), limited-risk transparency obligations, or minimal risk, including the provider/deployer role and the Article 6(3) exception."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Aku Nikkola"
  language: "Finnish"
  mike-display-name: "AI System Classification"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "AI Regulation"
  jurisdictions: "Finland, European Union"
---
# Tekoälyjärjestelmän riskiluokittelu (EU:n tekoälyasetus)

## Ohjeet

Luokittele tekoälyjärjestelmä EU:n tekoälyasetuksen (asetus (EU) 2024/1689) riskiperusteisen kehyksen mukaan ja tunnista sovellettava Annex III -kategoria, rooli (tarjoaja / käyttöönottaja) ja relevantit artiklat. Tämä työnkulku tuottaa tarkistettavan ensiarvion, ei oikeudellista neuvontaa — lopullinen luokittelu ja vaatimustenmukaisuuspäätökset kuuluvat ihmisasiantuntijalle.

Jos käytettävissä on tekoälyasetuksen hakulähde (esimerkiksi EUR-Lex tai muu oikeudellinen hakutyökalu), tarkista artiklojen sisältö ja Annex III -kategoriat ajantasaisesta lähteestä ennen lopullista vastausta ja liitä artiklaviittauksiin EUR-Lex-lähde. Jos hakulähdettä ei ole käytettävissä, älä luokittele muistinvaraisesti varmana: merkitse arvio muotoon [tarkistettava] ja pyydä käyttäjää toimittamaan ajantasainen asetusteksti.

### Vaihe 1: Kerää signaalit

Selvitä käyttäjältä: mitä järjestelmä tekee ja missä kontekstissa, kuka on tarjoaja (kehittää tai saattaa markkinoille omalla nimellään) ja kuka käyttöönottaja (käyttää ammattitoiminnassa), käsitelläänkö biometriikkaa, tehdäänkö profilointia tai automaattisia päätöksiä, kohdistuuko järjestelmä haavoittuviin ryhmiin (esim. lapsiin), onko se säännellyn tuotteen turvakomponentti, ja tuottaako se synteettistä sisältöä. Esitä puuttuvat kysymykset, jos luokittelu jää epävarmaksi.

### Vaihe 2: Luokittele

- **Kielletty (5 art)** — esim. haitallinen manipulointi, sosiaalinen pisteytys ja tietyt biometrisen tunnistuksen käytöt. Jos luokittelu osuu tähän, nosta se heti esiin: järjestelmää ei saa tarjota eikä ottaa käyttöön. Älä etene velvoitelistaan kuin kyse olisi sallitusta järjestelmästä.
- **Korkea riski (6 art)** — kaksi reittiä: Annex I (säännellyn tuotteen turvakomponentti) ja Annex III (alat: biometriikka, kriittinen infrastruktuuri, koulutus, työllistäminen, olennaiset palvelut, lainvalvonta, muuttoliike ja rajavalvonta, oikeudenkäyttö). Seuraukset: laajat velvoitteet tarjoajalle (9–17 art) ja käyttöönottajalle (26–27 art).
- **Rajoitettu riski (50 art)** — läpinäkyvyysvelvoitteet: keskusteluohjelmasta on kerrottava käyttäjälle, synteettinen sisältö on merkittävä.
- **Minimaalinen riski** — ei erityisvelvoitteita; vapaaehtoiset käytännesäännöt.
- **Yleiskäyttöiset mallit, GPAI (51–56 art)** — oma velvoitekehys; systeemisen riskin kynnys arvioidaan erikseen.

Huomioi lisäksi yleinen tekoälylukutaitovelvoite (4 art), joka koskee kaikkia tarjoajia ja käyttöönottajia riskiluokasta riippumatta.

### Vaihe 3: Arvioi 6(3)-poikkeus varoen

Korkean riskin Annex III -osumasta voi vapautua 6(3) artiklan "ei merkittävää riskiä" -poikkeuksella vain tiukoin edellytyksin. Käy edellytykset läpi asetustekstiä vasten, älä oletuksella — poikkeus ei sovellu profilointia tekeviin järjestelmiin. Huomioi myös dokumentointi- ja rekisteröintiseuraukset (6(4) ja 49(2) art). Merkitse kanta [varmista — asiantuntijan arvioitava], jos edellytykset jäävät tulkinnanvaraisiksi.

### Vaihe 4: Raportoi

Tuota: riskiluokka ja perustelu, Annex III -kategoria (jos korkea riski), rooli (tarjoaja / käyttöönottaja), relevantit artiklat lähdeviittein sekä seuraavat askeleet. Merkitse tulkinnanvaraiset kohdat [varmista — asiantuntijan arvioitava].

### Vaihe 5: Kytkennät

- **Tietosuoja:** tekoälyasetus ei korvaa yleistä tietosuoja-asetusta. Jos järjestelmä käsittelee henkilötietoja tai tekee profilointia tai automaattisia päätöksiä, muistuta rinnakkaisesta GDPR-arviosta (22 art automaattinen päätöksenteko, 35 art vaikutustenarviointi).
- **Kansallinen kerros:** tekoälyasetus on Suomessa suoraan sovellettava, mutta kansalliset valvontaviranomaiset ja täydentävä sääntely ovat muotoutumassa — älä esitä viranomaisnimeämisiä varmistettuina, vaan merkitse [varmista — kansallinen sääntely muotoutumassa].

## Rajaukset

- Ei tee lopullista riskiluokittelua — antaa ensiarvion; sitova luokittelu kuuluu asiantuntijalle.
- Ei esitä soveltamisen määräpäiviä eikä sakkojen määriä muistista — ne tarkistetaan erikseen asetuksesta ajantasaisesta lähteestä.
- Ei ratkaise 6(3)-poikkeusta oletuksella eikä sovella sitä profilointia tekeviin järjestelmiin.
- Ei kokoa velvoitelistoja eikä Annex IV -dokumentaatiota — ne ovat luokittelun jälkeinen erillinen tehtävä.
- Ei arvioi henkilötietojen käsittelyä, profilointia tai vaikutustenarvioinnin tarvetta GDPR:n kannalta — se on rinnakkainen, erillinen arvio.
