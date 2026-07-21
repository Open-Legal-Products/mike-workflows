---
name: "practice-profile-setup"
description: "Interview the user about their organization's legal practice conventions — house style, standard clauses, risk positions, applicable collective agreements — and produce a reusable practice-profile document that can be attached to future legal work."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Aku Nikkola"
  language: "Finnish"
  mike-display-name: "Practice Profile Setup"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "General Practice"
  jurisdictions: "Finland"
---
# Käytäntöprofiili

Tämä työnkulku haastattelee organisaation käytännöt ja kokoaa niistä uudelleenkäytettävän **käytäntöprofiilidokumentin**, jonka käyttäjä voi liittää tulevien juridisten tehtävien taustaksi. Näin "talon tapa" elää yhdessä paikassa eikä sitä tarvitse toistaa joka kerta.

Tämä työnkulku tuottaa tarkistettavan luonnoksen, ei oikeudellista neuvontaa. Lopullinen arvio kuuluu ihmisjuristille.

## Ohjeet

Noudata neljää periaatetta:

1. **Kysy, älä keksi.** Profiiliin kirjataan vain käyttäjän antamia tietoja. Puuttuva tieto jätetään pois — se kysytään tarvittaessa käyttöhetkellä.
2. **Profiili täydentää, ei korvaa.** Profiili ei ohita lakia: pakottava lainsäädäntö, lähteiden tarkistusvelvollisuus ja ihmisen lopullinen tarkistus pätevät aina profiilin sisällöstä riippumatta.
3. **Ei salaisuuksia profiiliin.** Asiakasnimiä, käynnissä olevien toimeksiantojen tietoja tai henkilötietoja ei tallenneta — profiili on pysyväisluonteinen ohjeistus, ei juttukansio.
4. **Versioi.** Merkitse profiiliin päivityspäivä ja päivittäjä; suosittele versiointia tai vuosikatselmusta.

### Vaihe 1 — Haastattelu

Kysy puuttuvat tiedot **yhdessä erässä**, vain organisaatiolle relevantit osiot:

- **Kaikille:** organisaation tyyppi ja toimiala (asianajotoimisto, yrityksen lakiosasto, virasto, kunta, järjestö); kenen näkökulmasta tekstit oletuksena kirjoitetaan; kirjoitustyyli, asiakirjapohjien kieli, allekirjoitustiedot ja vakiodisclaimer; tarkistusketju eli kuka hyväksyy luonnokset (esim. "osakas tarkistaa aina korkean riskin luokitellut").
- **Sopimustyö:** vakiolausekkeet ja mallipohjat (vastuunrajaus, riidanratkaisu, salassapito) ja missä ne sijaitsevat; riskilinjaukset eli mitä ei hyväksytä ilman eskalointia (esim. rajoittamaton vastuu, vieras lainvalinta).
- **Työnantajat:** sovellettavat työehtosopimukset ja henkilöstöpolitiikan vakiokohdat.
- **Julkinen sektori:** toimivaltarajat ja delegoinnit, hankintaohje, lausuntojen hyväksymisketju ja lausunnonantajaprofiili.
- **Compliance-toiminnot:** valvojat, ilmoituskanavat ja compliance-vastuuhenkilöt.

### Vaihe 2 — Kirjoita profiilidokumentti

Tuota jäsennelty dokumentti, jonka käyttäjä voi tallentaa ja liittää tulevaan työhön:

```markdown
# Käytäntöprofiili: <organisaatio>
<!-- Päivitetty: VVVV-KK-PP, päivittäjä: NN -->

## Organisaatio ja näkökulma
- ...

## Kirjoitustyyli ja vakiomuotoilut
- ...

## Mallipohjat ja vakiolausekkeet
- <nimi>: <sijainti> — käytä pohjana, kun ...

## Riskilinjaukset ja eskalointi
- ...

## Sovellettavat työehtosopimukset ja erityissääntely
- ...

## Tarkistus- ja hyväksymisketju
- ...
```

Jätä pois osiot, joihin käyttäjä ei antanut sisältöä. Näytä lopuksi yhteenveto kirjatuista linjauksista ja muistuta versioinnista sekä siitä, että profiili liitetään jatkossa tehtävän taustamateriaaliksi.

### Vaihe 3 — Ylläpito

Päivitys tehdään samalla prosessilla: näytä vanha sisältö ja vahvista muutos ennen ylikirjoitusta. Suosittele vuosikatselmusta: ovatko työehtosopimukset, pohjat ja linjaukset ajan tasalla.

## Rajaukset

- Ei keksi linjauksia tai pohjia — vain käyttäjän antamat tiedot kirjataan.
- Ei tallenna asiakas- tai henkilötietoja eikä käynnissä olevien toimeksiantojen tietoja.
- Ei arvioi linjausten oikeudellista kestävyyttä — jos linjaus vaikuttaa pakottavan säännöksen vastaiselta, nosta se esiin äläkä kirjaa sitä sellaisenaan.
- Profiili ei heikennä suojauksia: lähteiden tarkistus, epävarmuuksien merkintä ja ihmisen hyväksyntä pätevät aina.
