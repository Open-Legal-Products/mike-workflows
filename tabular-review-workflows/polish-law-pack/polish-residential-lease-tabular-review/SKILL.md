---
name: "polish-residential-lease-tabular-review"
description: "Use this workflow to review Polish residential lease agreements (umowa najmu lokalu mieszkalnego) under the Civil Code (Kodeks cywilny, Art. 659 et seq.) and the Tenant Protection Act (ustawa z dnia 21 czerwca 2001 r. o ochronie praw lokatorów) and extract structured information into the tabular review columns defined in table-columns.yaml."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "MateMatic Solutions"
  language: "Polish"
  mike-display-name: "Polish Residential Lease Tabular Review"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "Real Estate"
  jurisdictions: "Poland"
---
# Przegląd tabelaryczny polskich umów najmu lokalu mieszkalnego

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Wskazówki przeglądu

- Najem lokalu mieszkalnego podlega Kodeksowi cywilnemu (art. 659 i nast.) oraz ustawie z dnia 21 czerwca 2001 r. o ochronie praw lokatorów, mieszkaniowym zasobie gminy i o zmianie Kodeksu cywilnego. Ochrona lokatora jest w znacznej części bezwzględna, dlatego notuj postanowienia, które ją ograniczają, ale nie przesądzaj o ich skuteczności - to ocena prawnika.
- Rozróżnij rodzaj najmu, bo od niego zależą zarówno zakres ochrony, jak i limity: najem zwykły, najem okazjonalny (art. 19a i nast. ustawy) albo najem instytucjonalny, zawierany przez podmiot prowadzący działalność gospodarczą w zakresie wynajmowania lokali (art. 19f i nast. ustawy). Najem okazjonalny wymaga między innymi oświadczenia najemcy w formie aktu notarialnego o poddaniu się egzekucji i zgłoszenia umowy naczelnikowi urzędu skarbowego - odnotuj, czy umowa je przewiduje. Limit kaucji różni się między rodzajami najmu.
- Dyscyplina źródłowa: każda komórka wskazuje jednostkę redakcyjną umowy (np. "§ 3 ust. 1", "załącznik nr 2"). Jeżeli umowa milczy, wpisz "Nie wskazano" - nie zostawiaj komórki pustej i nie uzupełniaj jej regułą ustawową bez oznaczenia. Regułę ustawową oddzielaj wyraźnie od treści umowy.
- Postanowienia sporne cytuj dosłownie, zwłaszcza przesłanki wypowiedzenia, zasady podwyżki czynszu i rozliczenia kaucji.
- Sygnały ryzyka warte odnotowania: kaucja przekraczająca ustawowy limit, wypowiedzenie przez wynajmującego z przyczyn spoza katalogu ustawowego albo bez wymaganej formy, przerzucenie na najemcę napraw obciążających wynajmującego, kary umowne za wypowiedzenie, klauzule pozwalające na usunięcie najemcy bez tytułu wykonawczego.
- Odwołania do przepisów, których nie potwierdzasz w treści dokumentu ani we własnej wiedzy, oznaczaj jako [do weryfikacji]. Tabela pokazuje, co w umowach zapisano. Czy postanowienie jest ważne i skuteczne, rozstrzyga prawnik w odrębnej analizie - wynik tego przeglądu jest roboczym zestawieniem do sprawdzenia przez człowieka, nie poradą prawną.
