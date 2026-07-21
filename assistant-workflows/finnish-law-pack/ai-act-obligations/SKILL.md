---
name: "ai-act-obligations"
description: "Compile the obligations that apply to an AI system under the EU AI Act (Regulation (EU) 2024/1689) by role (provider/deployer) and risk class, including the Annex IV technical documentation checklist for high-risk systems and GPAI obligations."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Aku Nikkola"
  language: "Finnish"
  mike-display-name: "AI Act Obligations"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "AI Regulation"
  jurisdictions: "Finland, European Union"
---
# Tekoälyasetuksen velvoitteet roolin ja riskiluokan mukaan

## Ohjeet

Kokoa tekoälyjärjestelmään kohdistuvat EU:n tekoälyasetuksen (asetus (EU) 2024/1689) velvoitteet, kun riskiluokka on tiedossa. Jos riskiluokka tai rooli on vielä auki, tee luokittelu ensin. Tämä työnkulku tuottaa tarkistettavan velvoiteluonnoksen, ei oikeudellista neuvontaa — sitova arvio velvoitteiden täyttymisestä kuuluu ihmisasiantuntijalle.

Jos käytettävissä on tekoälyasetuksen hakulähde (esimerkiksi EUR-Lex tai muu oikeudellinen hakutyökalu), tarkista artiklojen sisältö ja velvoiteluettelot ajantasaisesta lähteestä ennen lopullista vastausta ja liitä artiklaviittauksiin lähde. Jos hakulähdettä ei ole käytettävissä, älä luettele velvoitteita muistinvaraisesti varmoina: merkitse ne muotoon [tarkistettava] ja pyydä käyttäjää toimittamaan ajantasainen asetusteksti.

### Vaihe 1: Varmista rooli ja riskiluokka

- **Tarjoaja (provider)** kehittää järjestelmän tai saattaa sen markkinoille omalla nimellään.
- **Käyttöönottaja (deployer)** käyttää järjestelmää ammattitoiminnassaan.
- Sama organisaatio voi olla molempia eri järjestelmissä. Korkean riskin järjestelmän olennainen muuttaminen voi tehdä käyttöönottajasta tarjoajan (25 art) — nosta tämä aina esiin.

### Vaihe 2: Kokoa velvoitteet

Tyypilliset korkean riskin velvoitteet (vahvista lähteestä):

- **Tarjoaja:** riskienhallintajärjestelmä (9 art), datanhallinta (10 art), tekninen dokumentaatio (11 art ja Annex IV), lokitus (12 art), läpinäkyvyys ja käyttöohjeet (13 art), ihmisen valvonta (14 art), tarkkuus, robustius ja kyberturvallisuus (15 art), laadunhallintajärjestelmä (17 art), vaatimustenmukaisuuden arviointi (43 art) ja rekisteröinti (49 art).
- **Käyttöönottaja:** käyttö ohjeiden mukaan ja ihmisen valvonta (26 art), tietyissä tapauksissa perusoikeusvaikutusten arviointi FRIA (27 art).
- **Kaikki roolit ja luokat:** yleinen tekoälylukutaitovelvoite (4 art). Rajoitetun riskin järjestelmissä läpinäkyvyysvelvoitteet (50 art).

### Vaihe 3: Tekninen dokumentaatio (korkea riski)

Käy Annex IV:n mukaisen teknisen dokumentaation kohdat läpi lähteestä (yhdeksän osa-aluetta: mm. järjestelmän yleiskuvaus, kehitysprosessi, valvonta ja suorituskyky, riskienhallinta, muutokset elinkaaren aikana). Tunnista, mitä organisaatiolla on jo ja mitä puuttuu, ja tuota tarkistuslista. Huomioi pk-yritysten mahdollisuus kevennettyyn dokumentaatioon [tarkistettava].

### Vaihe 4: Yleiskäyttöisten mallien (GPAI) velvoitteet

Yleiskäyttöisille malleille kokoa tarjoajan velvoitteet (51–56 art) ja huomioi systeemisen riskin lisävelvoitteet (55 art), jos malli ylittää asetuksen laskentamääräkynnyksen — kynnys ja seuraukset vahvistetaan lähteestä.

### Vaihe 5: Raportoi

Tuota velvoitelista ryhmiteltynä (tarjoaja / käyttöönottaja), artiklaviittaukset lähdemerkinnöin sekä Annex IV -tarkistuslista korkean riskin tapauksessa. Erota selkeästi, mitä on jo olemassa ja mitä puuttuu. Merkitse tulkinnanvaraiset kohdat [varmista — asiantuntijan arvioitava]. Muistuta tarvittaessa GDPR-rinnakkaisuudesta (tekoälyasetus ei korvaa tietosuoja-asetusta) ja kansallisen kerroksen tarkistuksesta: Suomen toimivaltaiset viranomaiset ja menettelyt ovat muotoutumassa — merkitse [varmista — kansallinen sääntely muotoutumassa].

## Rajaukset

- Ei tee lopullista vaatimustenmukaisuuspäätöstä — kokoaa tarkistettavan velvoiteluonnoksen.
- Ei määritä riskiluokkaa — edellyttää, että luokka ja rooli ovat jo tiedossa.
- Ei laske määräpäiviä eikä sakkoja muistista — siirtymäajat ja enimmäisseuraamukset tarkistetaan erikseen ajantasaisesta lähteestä.
- Ei ratkaise GPAI-mallin systeemisen riskin kynnystä oletuksella — kynnys ja lisävelvoitteet vahvistetaan lähteestä.
- Ei vahvista kansallisia viranomaisnimeämisiä eikä rekisteröinnin yksityiskohtia.
- Ei laadi teknistä dokumentaatiota valmiiksi — tuottaa tarkistuslistan ja tunnistaa puutteet; sisällön kirjoittaminen jää organisaatiolle.
