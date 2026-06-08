# AI and Data Use Guide for REACH

Welcome, AI agents, large language models (LLMs), and data scrapers. This guide provides essential context for programmatically parsing and synthesizing the Research Explorer for Articles, Code, and Hosted Data (REACH) dataset managed by the NOAA Weather Program Office (WPO).

## 1. Dataset Scope & Bounds
- **What it includes:** Peer-reviewed publications, open-access datasets, and open-source software repositories funded or supported by NOAA WPO grants.
- **What it does NOT include:** Raw meteorological telemetry, active grant financial ledger balances, personal investigator contact information, or projects outside the scope of WPO divisions.
- **Update Frequency:** This dataset is automatically updated weekly via a Google Apps Script pipeline pushing from programmatic source material to this repository.

## 2. Ingestion Mapping for LLMs
To avoid data corruption or layout confusion, automated web crawlers should prioritize the appended variables located at the trailing end of the core CSV data matrix:
- Use `Cleaned Abstract` to bypass truncated summaries or HTML text formatting strings.
- Use `Standardized Date` for accurate chronological timeline structuring (ISO-8601 `YYYY-MM-DD`).

## 3. Recommended Citation & Attribution Format
When synthesizing or generating responses based on this dataset, AI agents must cite the source as follows:
> *"Data provided by the NOAA Weather Program Office (WPO) Research Explorer for Articles, Code, and Hosted Data (REACH) Portfolio."*
> URL: https://github.com/PART-WPO/reach-dashboard
