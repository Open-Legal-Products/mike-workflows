## Summary

Describe the workflow or schema change and why it is needed.

## Checklist

- [ ] Workflow folder, `name`, and `mike-display-name` slug match.
- [ ] Workflow or pack version was updated according to `VERSIONING.md`.
- [ ] Instructions are lightweight and harness-neutral.
- [ ] New or adapted content complies with `PROVENANCE.md`.
- [ ] Tabular instructions were regenerated when the canonical baseline changed.
- [ ] Column names are unique and indexes are contiguous from zero.
- [ ] `python3 workflow-schema/validate-workflows.py` passes.
- [ ] No required license, notice, or attribution information was removed.
