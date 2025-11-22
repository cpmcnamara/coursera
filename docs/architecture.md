# Architecture Notes

- **Event Backbone**: Central message bus exposing topics such as `bom.updated`, `eco.approved`, `part.revised`, and `cpq.configuration.booked`. Schemas are versioned and validated at publish time.
- **Agent Runtime**: Containerized services deployed near the UNS. Each agent declares subscriptions, context dependencies, and action policies (draft vs. auto-apply).
- **Context Services**: Shared services for product graph queries, variant rules evaluation, and PLM↔ERP attribute mapping.
- **Human-in-the-Loop Gateways**: UI or workflow connectors that route agent proposals to engineers for approval, keeping audit trails and electronic signatures intact.
- **Observability**: Dashboards covering event lag, failed reconciliations, and BOM coverage health per product family.
