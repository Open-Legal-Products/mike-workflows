---
name: "legal-citation-extraction"
description: "Extract every legal citation from an English-language text by pattern rather than judgement: ECLI identifiers (CJEU and national), EU act identifiers (CELEX, Official Journal references, Regulation and Directive numbers), case names and numbers, and cited provisions, then normalise, deduplicate, and resolve short references (ibid., id., supra, op. cit., the above-cited judgment) to their antecedents. The front-end to citation verification: find every citation first, then check it. Use before verifying authorities, before sending a brief or opinion, or when asked what a text cites."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Wieslaw Mazur / MateMatic Solutions"
  language: "English"
  mike-display-name: "Legal Citation Extraction"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Legal Research"
  jurisdictions: "European Union, General"
---
# Legal Citation Extraction

You can only verify what you first find. Grounding a citation checks whether it exists in the source - but it runs on a list that someone has to assemble first. This workflow is that front-end: it walks the text and lists every authority, so none slips past verification. A missed citation is an unverified one.

Extraction is mechanical - by patterns and rules, not by judgement - on purpose: an unconstrained reading might miss a citation or invent one.

## Three steps

1. Extraction - recognise and capture every reference by the patterns below.
2. Aggregation - resolve short references (ibid., id., supra, op. cit., "the above-cited judgment") to their full antecedent, so they count as one citation, not several.
3. Hand-off - pass the structured list to verification: does each cited authority exist, and does it say what the text claims.

## Citation patterns

### Case law
- ECLI (EU): `ECLI:EU:C:2020:559` (Court of Justice), `ECLI:EU:T:2019:...` (General Court).
- ECLI (national): `ECLI:NL:HR:2021:...`, `ECLI:DE:BGH:...`, `ECLI:PL:SN:...`.
- Case names and numbers: `Party v Party`; CJEU case numbers `C-123/20`, `C-123/20 P` (appeal), joined cases `C-123/20 and C-124/20`; General Court `T-456/19`.

### EU legislation
- CELEX: `32016R0679`, `32019L0790` (sector + year + type + number).
- Named acts: `Regulation (EU) 2016/679`, `Directive 2019/790`, `Regulation (EC) No 1/2003`.
- Official Journal: `OJ L 119`, `OJ C 326`.

### Provisions
- `Article 5(1)(a) GDPR`, `Art. 263 TFEU`, `section 12`, `§ 3(2)`.

## Aggregation - short references

Resolve each short reference to the full citation given earlier: `ibid.`, `id.`, `supra`, `op. cit.`, `the cited judgment`, `the above-cited`, `loc. cit.`. Each points to the nearest matching antecedent in the text - count it as the same citation, but record where it occurs.

## Output format

A numbered table with columns: Type, Citation (normalised), Occurrences (page or offset), Antecedent (if a short reference). Close with the list of citations to verify.

## Limits

- Extraction catches references in a known format. A descriptive reference with no identifier ("the Court's data-protection case law") has nothing to match - mark it "no identifier, manual check".
- This is not existence verification - it says what is cited, not whether the citation is real.
- The patterns cover the common EU and ECLI formats; an unusual citation style may slip through. At high stakes, review by hand as well.

## Attribution

The extraction, aggregation, and annotation architecture follows eyecite (Free Law Project), BSD-2-Clause (https://github.com/freelawproject/eyecite), as a design pattern only - no eyecite code is used. US reporter patterns are dropped; the ECLI, CELEX, OJ, and EU citation patterns and the antecedent rules are the author's own.
