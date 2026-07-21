---
name: "anti-money-laundering"
description: "Build and review an organization's AML/CFT compliance under the Finnish Anti-Money Laundering Act (444/2017): scope assessment, risk assessment, customer due diligence and beneficial-owner identification, PEP handling, suspicious transaction reporting to the Financial Intelligence Unit, and the compliance program framework."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Aku Nikkola"
  language: "Finnish"
  mike-display-name: "Anti-Money Laundering"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Banking and Finance"
  jurisdictions: "Finland, European Union"
---
# Rahanpesun estäminen

> Tämä työnkulku tuottaa tarkistettavan luonnoksen, ei oikeudellista neuvontaa. Lopullinen arvio kuuluu ihmisjuristille.

## Ohjeet

Jäsennä rahanpesulain eli lain rahanpesun ja terrorismin rahoittamisen estämisestä (444/2017) velvoitteet ja rakenna ilmoitusvelvollisen compliance-ohjelma vaiheittain. Huomaa, että myös oikeudelliset palveluntarjoajat ovat eräissä toimeksiannoissa (mm. kiinteistö- ja yrityskaupat, varojen hallinnointi) itse ilmoitusvelvollisia.

EU:n AML-sääntely on uudistumassa asetuspohjaiseksi (AML-paketti, EU:n rahanpesuviranomainen AMLA) — tarkista voimassa oleva sääntelykerros lähteestä ennen kuin kuvaat velvoitteen; kansallinen laki muuttuu paketin myötä. Jos käytettävissä on suomalaisen oikeuden hakulähde (esimerkiksi Finlex-tietokanta tai oikeudellinen hakutyökalu), tarkista säädös- ja pykäläviittaukset ajantasaisesta lähteestä ennen lopullista vastausta. Jos hakulähdettä ei ole käytettävissä, älä esitä säännöksen sisältöä varmana: merkitse viittaus muotoon [tarkistettava] ja pyydä käyttäjää toimittamaan ajantasainen säädösteksti.

**Ehdoton rajaus:** älä avusta rahanpesussa, sen peittelyssä tai ilmoitusvelvollisuuden kiertämisessä missään muodossa.

## Vaihe 1: Soveltamisala — onko organisaatio ilmoitusvelvollinen?

Käy lain soveltamisalaluettelo läpi lähteestä: luotto- ja rahoituslaitokset, maksupalvelut, virtuaalivaluuttatoimijat, tilintarkastajat, kirjanpitäjät, veroneuvojat, oikeudellisia palveluja tarjoavat (tietyt toimeksiannot: kiinteistö- ja liiketoimintakaupat, varojen hoito, yhtiöiden perustaminen), kiinteistönvälittäjät, taidekauppa ym. — rajaukset ja kynnykset lähteestä. Kirjaa, miltä osin toiminta kuuluu soveltamisalaan.

## Vaihe 2: Riskiarvio

Lakisääteinen oma riskiarvio on ohjelman perusta:

- Asiakasriskit (PEP, ulkomaiset kytkennät, käteisvaltaisuus, monimutkaiset rakenteet), tuote- ja palveluriskit, maantieteelliset riskit (korkean riskin valtiot — luettelo lähteestä), jakelukanavat.
- Dokumentoi metodologia ja päivitysrytmi; johda toimenpiteet riskeistä (riskiperusteinen lähestymistapa).

## Vaihe 3: Asiakkaan tunteminen (KYC/CDD)

1. **Tunnistaminen ja todentaminen** — luonnollinen henkilö ja yhteisö; etätunnistamisen vaatimukset lähteestä.
2. **Tosiasialliset edunsaajat** — omistus- ja määräysvaltaketju; edunsaajarekisterin (PRH) tiedot eivät yksin riitä, vaan velvollisuus on omaan selvitykseen; ristiriidoista ilmoitusvelvollisuus rekisteriin.
3. **PEP-asema** — poliittisesti vaikutusvaltaiset henkilöt, perheenjäsenet ja yhtiökumppanit edellyttävät tehostettua menettelyä.
4. **Tehostettu vs. yksinkertaistettu tunteminen** — milloin kumpikin on sallittu tai pakollinen (lähteestä); kirjeenvaihtajasuhteet, korkean riskin valtiot.
5. **Jatkuva seuranta** — liiketoimien monitorointi suhteessa asiakkaan profiiliin; tietojen ajantasaisuus.
6. **Säilytys ja tietosuoja** — säilytysajat ja käyttötarkoitussidonnaisuus.

Jos tuntemista ei voida toteuttaa: asiakassuhde on jätettävä perustamatta tai lopetettava ja arvioitava ilmoituksen tekeminen — tämä on ehdoton.

## Vaihe 4: Epäilyttävä liiketoimi

1. **Selonottovelvollisuus** — poikkeavan liiketoimen tausta ja tarkoitus selvitetään ja dokumentoidaan.
2. **Ilmoitus rahanpesun selvittelykeskukselle** (goAML-järjestelmä) viipymättä; kynnys on epäily, ei varmuus. Liiketoimi voidaan joutua keskeyttämään — edellytykset lähteestä.
3. **Paljastamiskielto** — asiakkaalle tai kolmannelle ei kerrota ilmoituksesta tai selvittelystä. Kouluta tämä erikseen — rikkominen on rangaistavaa.
4. **Pakotteet erikseen**: pakotelistatarkistus (EU, YK, liiketoiminnan mukaan myös OFAC) on eri velvoite kuin rahanpesuilmoitus — varojen jäädyttäminen ja ilmoitus ulosottolaitokselle; menettely lähteestä.

## Vaihe 5: Ohjelman runko ilmoitusvelvolliselle

Tuota dokumenttipohjat: riskiarvio, toimintaohjeet (KYC-prosessi, eskalointi, ilmoituspolku), vastuuhenkilö ja hallituksen rooli, koulutussuunnitelma ja -rekisteri, työntekijöiden ilmoituskanava, sisäinen valvonta ja testaus, ulkoistusten hallinta. Valvojan (Finanssivalvonta tai aluehallinnon AML-valvoja) määräykset ja ohjeet huomioidaan [tarkistettava].

## Rajaukset

- Ei avusteta rahanpesussa, sen peittelyssä tai ilmoitusvelvollisuuden kiertämisessä — ehdoton kieltäytyminen.
- Ei tehdä pakotelista- tai PEP-hakuja — rekistereitä ei nähdä; prosessi ja vaatimukset jäsennetään, haut tekee organisaation oma järjestelmä.
- Ei rikota paljastamiskieltoa — ilmoitusepäilyä ei dokumentoida asiakkaalle näkyviin aineistoihin.
- Ei vahvisteta kynnysarvoja, säilytysaikoja tai korkean riskin valtioiden luetteloa muistista — lähteestä.
- Ei korvata valvojan kantaa — tulkinnanvaraisissa tilanteissa yhteys valvojaan tai juristiin.

## Viittaustapa

Viittaa säädöksiin muodossa: lain nimi ja säädösnumero ensimaininnassa (esim. laki rahanpesun ja terrorismin rahoittamisen estämisestä (444/2017)), sen jälkeen vakiintunut lyhyt muoto ja tarkka kohta. Oikeustapaukset tunnisteella (esim. KKO 2024:15). Merkitse epävarmat viittaukset [tarkistettava].
