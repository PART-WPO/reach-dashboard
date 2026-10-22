# REACH Scout Discovery Feed (public research staging only)

This folder is **not the REACH publication catalog**. It contains Scout's unreviewed research-output discovery candidates for human review in Discovery Hub. The feed does not insert, approve, or publish outputs.

## Layout

- `batches/YYYY-MM-DD-unique-run-id.csv` — **append-only** UTF-8 CSV for one Scout sprint; use the exact **24-column Discovery Hub CSV schema** in the same order.
- `manifest.json` — automatically generated pointer/index for every valid batch, with file SHA-256 and candidate count. Do not edit manually.
- `tools/build_manifest.py` — validates every batch and builds manifest.
- `.github/workflows/build-scout-discovery-manifest.yml` — GitHub Action triggered when a new batch is committed.

## Publication procedure for scheduled Scout sweeps

1. Finish the full public-source research sprint and save the comprehensive report, evidence ledger, and exact 24-column Discovery Hub CSV to ChatGPT Library `/REACH Scout` as before. **Do not overwrite the canonical registry or prior run files.**
2. Confirm the public CSV contains only public output metadata and evidence; blank out personal email fields and `Candidate ID` (Hub computes canonical identity). Retain A/B/C/D classifications in `Scout Discovery Rationale` and permanent REACH UIDs for known duplicates in `Existing REACH Match`.
3. Commit a **new** batch file at `scout-discoveries/batches/YYYY-MM-DD-<unique-run>.csv` using the connected GitHub tool. Never replace an existing batch or publish private source mapping, Smartsheet tokens, reviewer decisions, or internal notes.
4. GitHub Actions validates the batch and updates `manifest.json`. **A new batch becomes visible to Discovery Hub only after that action succeeds.** If the action fails, correct by adding a *new* batch with a unique ID; do not rewrite a previously imported batch.
5. Discovery Hub automatically checks the manifest when opened (or on its optional daily timer) and incrementally imports unseen batches into its **pending human review** queue. Manual `Import CSV` remains a fallback.

## Safeguards

- The `Candidate ID` is generated in Discovery Hub from normalized DOI, URL, or fallback title+award and is used to deduplicate repeated discoveries across sprints. Imported items **never** automatically receive human approval.
- A previously imported batch is immutable; if its ID is reused with a different SHA, Hub stops with an error rather than overwriting reviewer history.
- Changes to an existing candidate's substantive evidence result in `Needs re-review`, while unchanged previously recorded decisions remain preserved.
- The feed intentionally contains no native Smartsheet Row IDs or private mapping information. Only public scholarly/publisher evidence is allowed.
- The standalone new feed has no relation to `agent-data/`, which remains the published REACH catalog index.
