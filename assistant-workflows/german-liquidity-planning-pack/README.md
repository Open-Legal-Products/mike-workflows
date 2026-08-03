# German Liquidity Planning Pack

> **Hinweis nach Art. 50 KI-VO (EU AI Act).** Alle Inhalte dieses Packs wurden von einem Menschen überprüft und redaktionell kontrolliert. Ein Mensch trägt die redaktionelle Verantwortung (Art. 50 Abs. 4 Unterabsatz 2 Satz 5 KI-VO).
>
> **Notice under Article 50 EU AI Act.** All content in this pack has been reviewed and editorially controlled by a human. A human bears editorial responsibility (Article 50(4) subparagraph 2 sentence 5 of the EU AI Act).

**20 assistant workflows** covering the 13-week liquidity plan and the German insolvency-prevention duties that flow from it. Curated subset of a larger 73-workflow set — chosen to cover the full life cycle end to end without dead weight. Includes the plugin's **mega-prompt (Werkstatt)** and **quick-start prompt (Schnellstart)** in `prompts/`.

Adapted from the open-source [claude-fuer-deutsches-recht](https://github.com/Klotzkette/claude-fuer-deutsches-recht) collection.

## What this is

In German corporate practice, a director's personal liability under § 15a InsO turns on whether the company is `zahlungsunfähig` (illiquid) or `überschuldet` (over-indebted). Both tests collapse into one operational question: *does the company have the cash to meet its obligations over the next 13 weeks, and if not, when exactly does the gap open up*?

The 13-week liquidity plan is the tool the profession uses to answer that. It sits at the centre of the § 17 InsO illiquidity test, the § 18 InsO drohende-Zahlungsunfähigkeit horizon, IDW S 11 solvency opinions, § 19 II InsO Fortbestehensprognose, § 1 StaRUG crisis detection, and every Insolvenzplan / StaRUG restructuring plan.

## What is in the pack

20 workflows, grouped by phase:

**Intake and routing**

- `kaltstart-triage` — cold-start triage of a new mandate
- `einstieg-routing` — routes intake to the right sub-workflow
- `grundbegriffe-cashflow` — cash-flow primer for aligned terminology

**Data ingestion and status**

- `eingangsdaten-checkliste` — input-data checklist
- `dokumente-intake` — document intake
- `liquiditaetsstatus-quellenbelege` — liquidity status with source evidence
- `ausgabengruppen-systematik` — outflow-category taxonomy

**Plan build**

- `liqp-rollende-13wochen-bauleiter` — rolling 13-week plan build
- `liquiditaetsvorschau-3-6-12-monate` — 3/6/12-month medium-horizon forecast
- `forecast-wochenplanung` — weekly forecast layer
- `ampel-zahlen-schwellenwerte-berechnung` — threshold and traffic-light calculation

**Statutory tests**

- `bei-eingetretener-zahlungsunfaehigkeit` — § 17 InsO illiquidity assessment
- `bei-drohender-zahlungsunfaehigkeit` — § 18 InsO drohende Zahlungsunfähigkeit
- `idw-s6-integrierte-sanierungsplanung` — IDW S 6 restructuring-concept interface
- `export-forecast-fortbestehensprognose` — export for the § 19 II InsO Fortbestehensprognose

**Bank, sensitivity, quality**

- `kreditlinien-pruefen` — credit-line review
- `liqui-fuer-bankgespraech` — liquidity brief for bank meeting
- `sondereffekt-grossauftrag` — special-effect large-order stress case
- `szenarien-aufbauen` — scenario builder
- `redteam-qualitygate` — red-team quality gate

**Mega-prompt and quick-start prompt** (`prompts/`)

- `liquiditaetsplanung-werkstatt.md` — long-form orchestration prompt that walks a full case from intake through the finished 13-week plan. In a plugin runtime it dispatches to the workflows automatically. Outside a plugin runtime it produces the same output structure by working through the same steps manually.
- `liquiditaetsplanung-schnellstart.md` — short prompt for a single narrow task.

**Both prompts work in any chat model.** The pack is the best experience; the two prompts are the portable fallback.

## Language

Frontmatter (name, description, display name, practice area) is in English so the pack is browsable in an English-language catalogue. **Workflow bodies stay in German by design** — every workflow references German statutes (InsO, StaRUG, HGB, BGB, GmbHG, AktG, EStG), German case law (BGH, OLG), German professional standards (IDW S 11, IDW S 6, IDW S 9), and German terminology (Zahlungsunfähigkeit, Überschuldung, Fortbestehensprognose, Liquiditätsstatus, Zahlungsstockung, Insolvenzreife). These terms have no clean English equivalents.

## Source and licence

Sourced from the open-source [claude-fuer-deutsches-recht](https://github.com/Klotzkette/claude-fuer-deutsches-recht) collection. That upstream repo contains the full 73-workflow set plus README documentation, agents, and harness-specific plumbing — anyone who wants more context, background, or the original harness-specific setup should consult the upstream repo.

MIT.
