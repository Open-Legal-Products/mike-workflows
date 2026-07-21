---
name: "finnish-residential-lease-tabular-review"
description: "Use this workflow to review Finnish residential lease agreements under the Act on Residential Leases (laki asuinhuoneiston vuokrauksesta 481/1995) and extract structured information into the tabular review columns defined in table-columns.yaml."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Aku Nikkola"
  language: "Finnish"
  mike-display-name: "Finnish Residential Lease Tabular Review"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "Real Estate and Housing"
  jurisdictions: "Finland"
---
# Suomalaisten asuinhuoneiston vuokrasopimusten taulukkokatsaus

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Tarkastusohjeet

- Sovellettava laki on laki asuinhuoneiston vuokrauksesta (481/1995, AHVL). AHVL sisältää pakottavia säännöksiä vuokralaisen suojaksi (AHVL 3 §): ehto, jolla vuokralaisen lakisääteisiä oikeuksia rajoitetaan enemmän kuin laki sallii, on tehoton. Keskeiset kohdat: sopimuksen kesto ja muoto (AHVL 4–5 §), vakuuden enimmäismäärä (AHVL 8 §), vuokran tarkistaminen (AHVL 27 §), kunnossapito (AHVL 20 §), alivuokraus ja huoneiston luovutus (AHVL 17 § ja 8 luku), irtisanomisajat (AHVL 51–52 §).
- Tarkista ensin, että kohde on asuinhuoneisto: liikehuoneiston vuokraukseen sovelletaan eri lakia (laki liikehuoneiston vuokrauksesta 482/1995), joka on laajemmin tahdonvaltainen. Jos käyttötarkoitus on liiketila tai sekamuotoinen, kirjaa se riskihavaintoihin.
- Lähdekuri: jokainen solu viittaa siihen sopimuksen kohtaan, josta arvo on poimittu (esim. "kohta 4", "liite 2"). Jos tieto puuttuu sopimuksesta, merkitse "ei mainittu" — älä jätä solua tyhjäksi äläkä täytä sitä lain olettamalla ilman merkintää. Kun kirjaat lain olettaman, erota se selvästi sopimustekstistä (esim. "ei mainittu — lain olettama: ...").
- Lainaa ehdon sanamuoto sanatarkasti, kun sisältö on tulkinnanvarainen (erityisesti vuokrankorotusehto, vakuusehto ja päättämisehdot). Älä parafrasoi riskikohtia.
- Riskihavainnot: nosta esiin ainakin vakuus yli kolmen kuukauden vuokraa vastaavan määrän (AHVL 8 §), vuokralaisen irtisanomisaika yli yhden kuukauden tai vuokranantajan irtisanomisaika alle lain vähimmäisajan (AHVL 51–52 §), yksipuolinen tai epätäsmällinen korotusehto ilman mekanismia ja ilmoitusmenettelyä, lyhyiden määräaikaisten sopimusten ketjutus sekä muut ehdot, joilla poiketaan pakottavasta laista vuokralaisen vahingoksi.
- Taulukko kertoo, mitä sopimuksissa lukee; ehdon pätevyys ja lainmukaisuus on erillinen, ihmisjuristin tarkistettava arvio. Merkitse epävarmat lakiviittaukset muotoon [tarkistettava]. Tuotos on tarkistettava luonnos, ei oikeudellista neuvontaa.
