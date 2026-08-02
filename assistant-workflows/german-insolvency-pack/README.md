# German Insolvency and Restructuring Pack

> **Hinweis nach Art. 50 KI-VO (EU AI Act).** Alle Inhalte dieses Packs wurden von einem Menschen überprüft und redaktionell kontrolliert. Ein Mensch trägt die redaktionelle Verantwortung (Art. 50 Abs. 4 Unterabsatz 2 Satz 5 KI-VO).
>
> **Notice under Article 50 EU AI Act.** All content in this pack has been reviewed and editorially controlled by a human. A human bears editorial responsibility (Article 50(4) subparagraph 2 sentence 5 of the EU AI Act).

Eleven cloud plugins with **1254 assistant workflows** for the full German insolvency and restructuring practice plus its adjacent restitution and avoidance workstream, together with each plugin's mega-prompt and quick-start prompt.

This is the deepest and most battle-tested vertical in the [claude-fuer-deutsches-recht](https://github.com/Klotzkette/claude-fuer-deutsches-recht) collection.

## What is in the pack

### Eleven plugins, bundled as one pack

| Plugin | Workflows | Practice | Scope |
| --- | ---: | --- | --- |
| `fachanwalt-insolvenz-sanierungsrecht` | 505 | Insolvency and Restructuring | Full specialist bar qualification (Fachanwalt fuer Insolvenz- und Sanierungsrecht) under § 14 Fachanwaltsordnung |
| `insolvenzrecht` | 97 | Insolvency and Restructuring | Core insolvency law under InsO |
| `insolvenzverwaltung` | 53 | Insolvency and Restructuring | Insolvency administration (Verwalter, Sachwalter, Treuhaender) |
| `insolvenzforderungsanmeldungspruefung` | 60 | Insolvency and Restructuring | Claim registration and verification (§§ 174 ff. InsO) |
| `insolvenzplan-starug-planwerkstatt` | 58 | Insolvency and Restructuring | Insolvency plan (§§ 217 ff. InsO) and StaRUG restructuring plan (§§ 4 ff. StaRUG) |
| `verbraucherinsolvenz-schuldenbereinigung` | 69 | Insolvency and Restructuring | Consumer insolvency (§§ 304 ff. InsO), out-of-court debt settlement |
| `liquiditaetsplanung` | 73 | Insolvency and Restructuring | 13-week liquidity planning, IDW S 11 solvency test |
| `fortbestehensprognose` | 59 | Insolvency and Restructuring | Going-concern prognosis under § 19 II InsO / IDW S 6 |
| `krisenfrueherkennung-starug` | 58 | Insolvency and Restructuring | Early crisis detection under § 1 StaRUG |
| `forderungsmanagement-klagewerkstatt` | 84 | Insolvency and Restructuring | Claim management and dunning/litigation architecture |
| `bereicherungs-und-anfechtungsrecht-pruefer` | 138 | Restitution and Avoidance Law | Bereicherungsrecht (§§ 812 ff. BGB) and Anfechtungsrecht (AnfG plus §§ 129 ff. InsO) |

Bereicherungsrecht and Anfechtungsrecht sit next to insolvency because the moment a Bereicherungsanspruch runs into an insolvent debtor, or a creditor needs to reach an asset the debtor has moved away, Anfechtung is the next tool the practitioner picks up. Each workflow keeps its own practice area in its frontmatter so a downstream catalogue can still separate the two verticals.

### Mega-prompts and quick-start prompts

Every plugin ships with two orchestration prompts, included verbatim under `prompts/`:

- **`<plugin>-werkstatt.md` — the mega-prompt.** Long-form orchestration prompt that walks a full case from intake through work product, chaining the plugin's workflows in the right order. Cloud plugins run their workflows automatically. **Outside a plugin runtime, the mega-prompt produces the same output structure by working through the same steps manually.**
- **`<plugin>-schnellstart.md` — the quick-start prompt.** Short prompt for a single narrow task inside the plugin, for when a full mega-prompt would be overkill.

**Both formats work in any chat model. The cloud plugins are the best experience; the mega-prompts and quick-start prompts are the portable fallback.**

## Language

**Workflow bodies are in German by design.**

Every workflow references German statutes (InsO, StaRUG, BGB, HGB, ZPO, AnfG, GmbHG, AktG, EStG), German case law (BGH, BAG, OLG, Insolvenzgerichte), and German legal terminology (Zahlungsunfaehigkeit, Ueberschuldung, drohende Zahlungsunfaehigkeit, Fortbestehensprognose, Restschuldbefreiung, Vorsatzanfechtung, kongruente Deckung, Massearmut, Massekosten, Schlussrechnung, Leistungskondiktion, Eingriffskondiktion, Entreicherung, Rueckgewaehrschuldverhaeltnis). These terms have no clean English equivalents.

**Frontmatter (name, description, display name, practice area) is in English** so the pack is browsable in an English-language catalogue.

## Coverage highlights

**Insolvency and restructuring**

- Insolvency triggers — Zahlungsunfaehigkeit (§ 17 InsO), Ueberschuldung (§ 19 InsO), drohende Zahlungsunfaehigkeit (§ 18 InsO), corresponding filing duties (§ 15a InsO)
- Solvency and prognosis — 13-week liquidity plan, IDW S 11 solvency test, IDW S 6 restructuring concept, IDW S 9 restructuring opinion
- Filing and opening — Eigenverwaltung (§§ 270 ff. InsO), Schutzschirmverfahren (§ 270d InsO), preliminary administration
- Administration — Verwalter/Sachwalter/Treuhaender duties, Massesicherung, Schlussrechnung
- Claim registration — Anmeldung, Pruefung, Feststellung, Bestreiten, Tabellenauszug
- Restructuring — Insolvenzplan (§§ 217 ff. InsO), StaRUG plan (§§ 4 ff. StaRUG)
- Consumer insolvency — outside-settlement attempt (§ 305 InsO), simplified proceedings, Restschuldbefreiung
- Cross-border — European Insolvency Regulation (EIR), main and secondary proceedings, COMI
- Adjacent civil practice — Mahnverfahren, Zwangsvollstreckung, enforcement titles, security interests

**Restitution and avoidance**

- Bereicherungsrecht §§ 812 ff. BGB — Leistungskondiktion, Eingriffskondiktion, Verwendungskondiktion, condictio ob rem, condictio ob causam finitam
- Multi-party constellations — Anweisungsfall, Durchgriff, Zession, Verrechnung, Umbuchung, Dreiecksverhaeltnisse
- Exclusions and defences — §§ 814, 815, 817, 818 III, 819 BGB (Kenntnis der Nichtschuld, Zweckerreichung, Sittenverstoss, Entreicherung, verschaerfte Haftung)
- Restitution architecture — Rueckabwicklung, Wertersatz, Nutzungen, Verwendungen
- Anfechtungsrecht — AnfG (individual-creditor avoidance) and §§ 129 ff. InsO (insolvency avoidance): Vorsatzanfechtung, unentgeltliche Leistungen, kongruente / inkongruente Deckung, Anfechtungsfristen, Rueckgewaehr

## Slug conventions

Where the same generic filename (e.g. `anschluss-routing`) appears in multiple plugins, the slug is prefixed with a short plugin code (`fa-ins-`, `insr-`, `insv-`, `insf-`, `insp-`, `vins-`, `liq-`, `fbp-`, `kfe-`, `fkw-`, `ber-`) so every workflow id is unique inside the pack. The `source-plugin` field in each workflow's frontmatter records which upstream plugin the workflow came from.

## Source

Sourced from the open-source [claude-fuer-deutsches-recht](https://github.com/Klotzkette/claude-fuer-deutsches-recht) collection (MIT). That upstream repo contains additional material — README documentation, agents, and harness-specific plumbing — that is out of scope for this catalogue. Anyone who wants more context, background, or the original harness-specific setup should consult the upstream repo.

## Licence

MIT.
