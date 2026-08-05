---
name: "polish-contract-tabular-review"
description: "Use this workflow to review contracts governed by Polish law and extract structured information into the tabular review columns defined in table-columns.yaml. Column prompts are in Polish, tuned to Polish contract practice and due diligence."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "MateMatic Solutions"
  language: "Polish"
  mike-display-name: "Polish Contract Tabular Review"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "General Transactions"
  jurisdictions: "Poland"
---
# Przegląd tabelaryczny polskich umów

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Wskazówki przeglądu

- Kolumny odpowiadają typowym polom przeglądu polskich umów i badania due diligence: kara umowna (art. 483 Kodeksu cywilnego), właściwość sądu i zapis na sąd polubowny, umowa powierzenia przetwarzania danych osobowych (art. 28 RODO), zabezpieczenia wykonania umowy (weksel, poręczenie, zastaw, hipoteka, gwarancja bankowa), zakaz konkurencji.
- Dyscyplina źródłowa: każda komórka wskazuje jednostkę redakcyjną umowy, z której pochodzi wartość (np. "§ 5 ust. 2", "załącznik nr 1"). Jeśli umowa milczy w danej sprawie, wpisz "Nie wskazano" zgodnie z konwencją promptu - nie zostawiaj komórki pustej i nie uzupełniaj jej domysłem.
- Postanowienia ryzykowne (kara umowna, ograniczenie odpowiedzialności, zakaz konkurencji, cesja) cytuj w brzmieniu dosłownym, gdy treść jest niejednoznaczna. Nie parafrazuj miejsc spornych.
- Identyfikatory stron podawaj w polskiej konwencji: pełna firma z formą prawną (np. sp. z o.o., S.A.), numer KRS lub NIP, rola zdefiniowana w umowie w cudzysłowie.
- Tabela odzwierciedla to, co jest zapisane w umowach; ocena ważności i skuteczności postanowień to odrębna analiza prawnika. Wynik jest roboczym zestawieniem do weryfikacji przez człowieka, nie poradą prawną.
