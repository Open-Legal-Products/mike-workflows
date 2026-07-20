---
name: "finnish-employment-contract-tabular-review"
description: "Use this workflow to review Finnish employment contracts under the Employment Contracts Act (työsopimuslaki 55/2001) and extract structured information into the tabular review columns defined in table-columns.yaml."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Aku Nikkola"
  language: "Finnish"
  mike-display-name: "Finnish Employment Contract Tabular Review"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "Employment Law"
  jurisdictions: "Finland"
---
# Suomalaisten työsopimusten taulukkokatsaus

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Tarkastusohjeet

- Sovellettava laki on työsopimuslaki (55/2001, TSL). Työlainsäädäntö on pakottavaa työntekijän hyväksi: ehto, joka alittaa pakottavan lain tai sovellettavan työehtosopimuksen (TES) vähimmäistason työntekijän vahingoksi, on tehoton. Keskeiset luvut: TSL 1 luku (sopimuksen kesto ja koeaika), 2 luku (työnantajan velvollisuudet, TSL 2:4 kirjallinen selvitys ehdoista, TSL 2:7 yleissitova TES), 3 luku (kilpailukielto TSL 3:5 ja salassapito TSL 3:4), 6 luku (irtisanomisajat TSL 6:2–6:3).
- Lähdekuri: jokainen solu viittaa siihen sopimuksen kohtaan, josta arvo on poimittu (esim. "kohta 5.2", "liite 1"). Jos tieto puuttuu sopimuksesta, merkitse "ei mainittu" — älä jätä solua tyhjäksi äläkä täytä sitä lain olettamalla ilman merkintää. Kun kirjaat lain olettaman, erota se selvästi sopimustekstistä (esim. "ei mainittu — lain olettama: ...").
- Lainaa ehdon sanamuoto sanatarkasti, kun sisältö on tulkinnanvarainen (erityisesti kilpailukielto, salassapito ja määräaikaisuuden peruste). Älä parafrasoi riskikohtia.
- Riskihavainnot: nosta esiin ainakin perusteeton tai perustelematon määräaikaisuus (TSL 1:3), koeaika yli lain enimmäispituuden (TSL 1:4), kilpailukielto ilman erityisen painavaa syytä tai korvausehtoa (TSL 3:5, uudistettu lailla 1018/2021), palkka tai muut ehdot alle sovellettavan TES:n vähimmäistason sekä ehdot, joilla yritetään poiketa pakottavasta laista työntekijän vahingoksi.
- Taulukko kertoo, mitä sopimuksissa lukee; ehdon pätevyys ja lainmukaisuus on erillinen, ihmisjuristin tarkistettava arvio. Merkitse epävarmat lakiviittaukset muotoon [tarkistettava]. Tuotos on tarkistettava luonnos, ei oikeudellista neuvontaa.
