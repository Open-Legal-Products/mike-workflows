# German Liquidity Planning Pack

> **Hinweis nach Art. 50 KI-VO (EU AI Act).** Alle Inhalte dieses Packs wurden von einem Menschen überprüft und redaktionell kontrolliert. Ein Mensch trägt die redaktionelle Verantwortung (Art. 50 Abs. 4 Unterabsatz 2 Satz 5 KI-VO).
>
> **Notice under Article 50 EU AI Act.** All content in this pack has been reviewed and editorially controlled by a human. A human bears editorial responsibility (Article 50(4) subparagraph 2 sentence 5 of the EU AI Act).

**73 assistant workflows** for the single most load-bearing piece of German insolvency-prevention practice: the **13-week liquidity plan**. Includes the plugin's **mega-prompt (Werkstatt)** and **quick-start prompt (Schnellstart)** in `prompts/`.

Adapted from the open-source [claude-fuer-deutsches-recht](https://github.com/Klotzkette/claude-fuer-deutsches-recht) collection.

## What this is

In German corporate practice, a director's personal liability under § 15a InsO turns on whether the company is `zahlungsunfähig` (illiquid) or `überschuldet` (over-indebted). Both tests collapse into one operational question: *does the company have the cash to meet its obligations over the next 13 weeks, and if not, when exactly does the gap open up*?

The 13-week liquidity plan is the tool the profession uses to answer that question. It sits at the centre of:

- **Zahlungsunfähigkeitsprüfung** under § 17 InsO (liquidity gap ≥ 10 % that is not closed within three weeks = illiquid).
- **IDW S 11** — the profession's standard for solvency and filing-obligation assessments. Every S 11 opinion is built on a 13-week plan.
- **Fortbestehensprognose** under § 19 II InsO — the going-concern prognosis. The prognosis is only credible if there is a plan behind it that actually reaches, week by week, from today to the end of the prognosis horizon.
- **Krisenfrüherkennung** under § 1 StaRUG — since 2021, every director must run a forward-looking crisis-detection system. The 13-week plan is the first artefact the courts and creditors expect to see.
- **Insolvency plan and StaRUG restructuring plan** — every restructuring plan needs a liquidity plan to prove it works.

## What is in the pack

- **73 workflows** covering intake, structure, KPI selection, weekly bridge, sensitivity and stress cases, deviations, escalation, filings, communication with management, banks, and creditors, and the interfaces to IDW S 11, IDW S 6, § 15a InsO, § 19 II InsO, and § 1 StaRUG.
- **`prompts/liquiditaetsplanung-werkstatt.md`** — the **mega-prompt**. Long-form orchestration prompt that walks a full case from intake through the finished 13-week plan, chaining the workflows in the right order. In a plugin runtime it dispatches to the workflows automatically. Outside a plugin runtime it produces the same output structure by working through the same steps manually.
- **`prompts/liquiditaetsplanung-schnellstart.md`** — the **quick-start prompt**. Short prompt for a single narrow task inside the pack, for when a full mega-prompt would be overkill.

**Both prompts work in any chat model. The pack is the best experience; the two prompts are the portable fallback.**

## Language

**Workflow bodies are in German by design.**

Every workflow references German statutes (InsO, StaRUG, HGB, BGB, GmbHG, AktG, EStG), German case law (BGH, BAG, OLG), and German professional standards (IDW S 11, IDW S 6, IDW S 9). It uses German terminology — Zahlungsunfähigkeit, Überschuldung, drohende Zahlungsunfähigkeit, Fortbestehensprognose, Liquiditätsstatus, Finanzplan, Zahlungsstockung, Insolvenzreife. These terms have no clean English equivalents. Translating the bodies would either invent English terms that no German court accepts, or produce calques that neither German nor English readers can use.

**Frontmatter (name, description, display name, practice area) is in English** so the pack is browsable in an English-language catalogue.

## Coverage

- Intake — company, sector, distress signals, existing plans, quality of data
- Data ingestion — accounting exports, bank statements, receivables, payables, planning inputs
- 13-week bridge — opening cash, receipts by category, disbursements by category, closing cash per week
- KPI layer — Liquiditätsgrad, Deckungsgrad, Working-Capital-Kennzahlen
- § 17 InsO test — 10 % gap threshold, three-week rule, staged assessment
- § 18 InsO — drohende Zahlungsunfähigkeit horizon
- § 19 II InsO — Fortbestehensprognose horizon and integration with the plan
- § 1 StaRUG — crisis-detection duties for directors
- IDW S 11 — solvency test methodology and opinion structure
- IDW S 6 — restructuring concept interface
- Sensitivity and stress — bank-line loss, customer default, tax back-payment, cost shocks
- Deviation management — plan-vs-actual, rolling forward, root-cause on gaps
- Escalation — early-warning triggers, management-board reporting, bank communication, creditor communication
- Filings — § 15a InsO deadline management, Eigenverwaltung / Schutzschirm application interfaces
- Documentation — file structure, audit trail, evidence for the going-concern prognosis

## Source and licence

Sourced from the open-source [claude-fuer-deutsches-recht](https://github.com/Klotzkette/claude-fuer-deutsches-recht) collection. That upstream repo contains additional material — README documentation, agents, and harness-specific plumbing — that is out of scope for this catalogue. Anyone who wants more context, background, or the original harness-specific setup should consult the upstream repo.

MIT.
