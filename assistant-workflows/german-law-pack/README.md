# German Law Pack

Assistant workflows for German legal practice, covering all 24 Fachanwaltschaften (specialist bar qualifications recognised by the German Federal Bar under §§ 1 ff. Fachanwaltsordnung) plus adjacent workflows for insolvency, employment testimonials, and legal methodology.

## Language

**Workflow bodies are in German by design.**

Every workflow references German statutes (BGB, StGB, StPO, ZPO, HGB, InsO, GewO, StVG, EStG, and so on), German case law (BGH, BAG, BSG, BFH, BVerfG, OLG, LG, AG), and German legal terminology (Pflichtteilsergänzung, Zugewinnausgleich, Fortbestehensprognose, Substantiierungslast). These terms have no clean English equivalents. Translating the bodies would either invent English terms that no German court accepts, or produce word-salad calques that neither German nor English readers can use.

**Frontmatter (name, description, display name, practice area) is in English** so the pack is browsable and searchable in an English-language catalogue. When a workflow is invoked, the model reads the German body and produces German output — which is what German legal work requires.

For readers whose German is limited, most modern LLMs will translate a workflow's output on request ("please summarise this in English"). That is a runtime concern, not a maintenance burden that should live in the catalogue.

## Coverage

**All 24 Fachanwaltschaften:**

- Agricultural Law (Fachanwalt für Agrarrecht)
- Employment Law (Fachanwalt für Arbeitsrecht)
- Banking and Capital Markets (Fachanwalt für Bank- und Kapitalmarktrecht)
- Construction and Architects Law (Fachanwalt für Bau- und Architektenrecht)
- Inheritance Law (Fachanwalt für Erbrecht)
- Family Law (Fachanwalt für Familienrecht)
- Intellectual Property (Fachanwalt für gewerblichen Rechtsschutz)
- Commercial and Corporate Law (Fachanwalt für Handels- und Gesellschaftsrecht)
- Insolvency and Restructuring (Fachanwalt für Insolvenz- und Sanierungsrecht)
- International Business Law (Fachanwalt für Internationales Wirtschaftsrecht)
- IT Law (Fachanwalt für IT-Recht)
- Medical Law (Fachanwalt für Medizinrecht)
- Tenancy and Condominium Law (Fachanwalt für Miet- und Wohnungseigentumsrecht)
- Migration Law (Fachanwalt für Migrationsrecht)
- Social Security Law (Fachanwalt für Sozialrecht)
- Sports Law (Fachanwalt für Sportrecht)
- Tax Law (Fachanwalt für Steuerrecht)
- Criminal Law (Fachanwalt für Strafrecht)
- Transport and Freight Forwarding Law (Fachanwalt für Transport- und Speditionsrecht)
- Copyright and Media Law (Fachanwalt für Urheber- und Medienrecht)
- Public Procurement Law (Fachanwalt für Vergaberecht)
- Traffic Law (Fachanwalt für Verkehrsrecht)
- Insurance Law (Fachanwalt für Versicherungsrecht)
- Administrative Law (Fachanwalt für Verwaltungsrecht)

**Add-on workflows folded into the matching practice area:**

- Insolvency and Restructuring: `insolvenzrecht`, `insolvenzverwaltung`, `insolvenzforderungsanmeldungspruefung`, `insolvenzplan-starug-planwerkstatt`, `verbraucherinsolvenz-schuldenbereinigung`, `liquiditaetsplanung`
- Employment Law: `arbeitszeugnis-analyse`, `arbeitszeugnisgenerator`, `arbeitszeugnispruefer`
- Legal Methodology: `subsumtions-pruefer`

## Slug conventions

Where the same generic filename (e.g. `anschluss-routing`) appears in multiple Fachanwaltschaften, the slug is prefixed with a short practice code (`erb-`, `arb-`, `straf-`, `fam-`, and so on) so every workflow id is unique inside the pack.

## Source

Sourced from the open-source [claude-fuer-deutsches-recht](https://github.com/Klotzkette/claude-fuer-deutsches-recht) collection (MIT). That upstream repo contains additional material — README documentation, mega-prompts, quickstart prompts, agents, and harness-specific plumbing — that is out of scope for this catalogue. **Anyone who wants more context, background, or the original harness-specific setup should consult the upstream repo.**

## Licence

MIT.
