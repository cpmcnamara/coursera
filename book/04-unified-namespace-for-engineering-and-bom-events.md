# Unified Namespace for Engineering and BOM Events

## Why Point-to-Point Fails
Point-to-point integrations create N² interfaces, duplicated mapping logic, and inconsistent behavior between PLM, ERP, CPQ, PDM, and service systems. Every new product or region spawns more scripts to maintain.

## Unified Namespace (UNS)
A UNS is an event backbone with consistent, semantic topics for engineering data. Example topics:
- `part.created`, `part.revised`
- `bom.updated`, `bom.released`
- `eco.submitted`, `eco.approved`, `ecr.logged`
- `material.master.changed`
- `cpq.configuration.booked`
- `service.installation.changed`

Payload sketch for `bom.updated`:
```json
{
  "product_code": "ABC-100",
  "revision": "D",
  "effectivity_date": "2024-08-01",
  "parent": "ASM-200",
  "components": [
    {"item": "P-123", "qty": 2, "uom": "EA", "refdes": ["R1", "R2"]},
    {"item": "P-789", "qty": 1, "uom": "EA", "alternate_group": "ALT-A"}
  ],
  "source_system": "PLM"
}
```

## How UNS Simplifies BOM Flows
- PLM publishes BOM change events; agents subscribe, derive impact, and update ERP or propose ECO bundles.
- CPQ publishes configuration selections; agents validate against variant rules and ensure manufacturing BOM coverage.
- Service tools publish installation updates; agents reconcile fielded configurations with released BOMs and flag gaps.

## Topic and Schema Guidance
- Use clear verbs and objects: `bom.updated`, `part.revised`, `configuration.validated`.
- Include revision, effectivity, and source system in payloads for traceability.
- Version schemas and keep them under configuration control alongside agent code.
