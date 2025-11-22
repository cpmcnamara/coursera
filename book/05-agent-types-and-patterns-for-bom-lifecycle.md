# Agent Types and Patterns for the BOM Lifecycle

## BOM Consistency Agents
- **Inputs**: `bom.updated`, `bom.released`, ERP BOM snapshots.
- **Context**: PLM↔ERP mapping tables, unit-of-measure rules, alternate/variant definitions.
- **Actions**: Compare PLM and ERP structures, highlight missing components or wrong revisions, and propose reconciliation steps or draft change tickets.
- **Scenario & Savings**: Before release, the agent identifies five mismatched alternates across two regions, saving 6–8 engineer hours otherwise spent on manual cross-checks.

## Change Impact & Dependency Agents
- **Inputs**: `part.revised`, `eco.approved`, `document.changed`, field failure events.
- **Context**: Product-variant graph, document associations, effectivity rules.
- **Actions**: Build impact reports listing affected BOMs, variants, documents, and test methods; suggest ECO/ECR bundles with priority.
- **Scenario & Savings**: A sterilization method change triggers a multi-product analysis and yields a ready-to-review ECO package, trimming impact analysis from days to hours.

## Variant & Configuration Agents
- **Inputs**: `cpq.configuration.booked`, variant master data, market/regional rules.
- **Context**: Configuration rules, compatibility matrices, valid option sets.
- **Actions**: Validate proposed configurations, flag unsupported variants, and identify “dead” variants lacking BOM coverage.
- **Scenario & Savings**: Sales proposes a new hospital bundle; the agent confirms BOM coverage and flags a missing regional label part, avoiding late-stage scramble.

## Documentation & Traceability Agents
- **Inputs**: `eco.approved`, `bom.released`, document library metadata.
- **Context**: Traceability matrices linking parts, tests, labels, and risk controls.
- **Actions**: Generate part catalogs, BOM views per region, change summaries, and traceability matrices; keep documentation synchronized with system-of-record data.
- **Scenario & Savings**: Automatically generated change summaries reduce technical writer workload by several hours per ECO while tightening audit readiness.

## Data Quality & Governance Agents
- **Inputs**: Attribute changes, UDI fields, risk class updates, code set revisions.
- **Context**: Allowed code lists, naming conventions, validation rules.
- **Actions**: Monitor for missing attributes or invalid codes, nudge engineers with inline fixes, and block releases if critical fields are incomplete.
- **Scenario & Savings**: Catches missing sterilization method data before release, preventing downstream ERP rework and field recall risk.

## Observability & Health Agents
- **Inputs**: Event flow telemetry, integration logs, agent execution results.
- **Context**: Service-level objectives for synchronization, expected event volumes.
- **Actions**: Detect failed synchronizations, alert on stuck BOM updates, and provide quick “where is this part inconsistent” dashboards.
- **Scenario & Savings**: Flags a stalled PLM→ERP queue before production is affected, saving production control from manual triage.
