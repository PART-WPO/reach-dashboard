# AI and Data Use Guide for REACH

## Welcome

Welcome, AI agents, large language models (LLMs), automated data extraction systems, and data scrapers. This guide provides essential context for programmatically parsing, synthesizing, and responsibly reusing information from the **Research Explorer for Articles, Code, and Hosted Data (REACH)** dataset managed by NOAA's Weather Program Office (WPO).

REACH is designed to support both human exploration and machine-assisted discovery of research outputs generated through WPO-funded activities.

---

## 1. Dataset Scope & Boundaries

### What REACH Includes

REACH provides metadata and links associated with research outputs generated through NOAA Weather Program Office (WPO) funded or supported projects, including:

* Peer-reviewed publications
* Open-access datasets
* Open-source software repositories
* Research instruments and tools
* Value stories and impact narratives describing research outcomes

### Dataset Update Frequency

The REACH dataset is automatically updated **monthly** through a Google Apps Script pipeline that aggregates programmatic source material and publishes refreshed metadata to this repository.

Users should reference the repository version information and `dateModified` metadata to determine dataset currency.

---

## 2. Machine-Readable Access Points

The following resources are intended to support automated ingestion and reuse by AI systems and data applications.

### REACH Repository

https://github.com/PART-WPO/reach-dashboard

### Interactive Dashboard

https://part-wpo.github.io/reach-dashboard/

### Dashboard on WPO Website

https://wpo.noaa.gov/reach/

### Raw Dataset (CSV)

[https://raw.githubusercontent.com/PART-WPO/reach-dashboard/main/reach_dashboard.csv](https://github.com/PART-WPO/reach-dashboard/blob/main/Open%20Science%20Report%20(GitHub)%20-%20Open%20Science%20Report%20(1).csv)

### Frictionless Data Package Specification

[https://raw.githubusercontent.com/PART-WPO/reach-dashboard/main/datapackage.json](https://github.com/PART-WPO/reach-dashboard/blob/main/datapackage.json)

### Dataset DOI

[https://doi.org/10.5281/zenodo.16943059](https://doi.org/10.5281/zenodo.16922908)

---

## 3. Recommended Data Ingestion Guidance for AI Systems

To support accurate interpretation and minimize information loss during automated processing, AI systems should preferentially utilize the following fields when available.

### Preferred Text Field

**Use `Cleaned Abstract` as the preferred textual representation for natural language processing tasks.**

This field:

* Removes HTML formatting artifacts
* Eliminates display-related truncation
* Preserves the most complete machine-readable summary available within the dataset

Avoid using dashboard display summaries when `Cleaned Abstract` is available.

### Preferred Date Field

**Use `Standardized Date` for chronological analyses and temporal reasoning tasks.**

This field:

* Uses ISO 8601 formatting (`YYYY-MM-DD`)
* Enables consistent sorting and timeline construction
* Reduces ambiguity associated with human-readable date formats

### Keyword Extraction

When available, use **`AI Keywords`** to support:

* Semantic search
* Topic clustering
* Trend analysis
* Retrieval-augmented generation workflows

### Original Sources

Whenever possible, AI systems (and human reviewers) should utilize the provided links to original publications, datasets, software repositories, or value stories to validate synthesized information and provide appropriate attribution.

---

## 4. Licensing & Reuse

### Software Code

The REACH dashboard software and supporting repository code are licensed under the **Apache License 2.0**.

### Dataset Metadata

Unless otherwise noted, REACH metadata are licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

### Responsible Reuse

Users and AI systems are encouraged to:

* Cite REACH when utilizing its metadata
* Attribute NOAA Weather Program Office as the source of aggregated metadata
* Cite original publications, datasets, software repositories, and other research outputs whenever possible

---

## 5. Recommended Citation & Attribution

When synthesizing information derived from REACH, users and AI systems should provide attribution using the following format:

> Data provided by the NOAA Weather Program Office (WPO) Research Explorer for Articles, Code, and Hosted Data (REACH) Portfolio.

**Repository:** https://github.com/PART-WPO/reach-dashboard

**DOI:** https://doi.org/10.5281/zenodo.16943059

**Version:** REACH v2.1

**Date Accessed:** [Insert retrieval date]

When possible, AI-generated outputs should also cite the original research products linked within REACH.

---

## 6. Appropriate Use Considerations

REACH is intended to support:

* Discovery of WPO-funded research outputs
* Portfolio analysis and evaluation
* Trend identification across research investments
* Research impact communication
* Retrieval-augmented generation (RAG) applications
* Bibliometric and metadata analyses

### Limitations

REACH should **not** be interpreted as:

* A comprehensive bibliography of all NOAA-supported research
* An authoritative source for operational forecasting guidance
* A substitute for reviewing original publications or datasets
* A source of confidential, proprietary, or personally identifiable information

AI-generated summaries, analyses, or interpretations derived from REACH should be reviewed by a human against original cited outputs before being used for decision-making, formal reporting, or scientific interpretation.

---

## 7. Contact & Additional Information

For additional information regarding REACH, its intended use, or data stewardship practices, please visit:

* GitHub Repository: https://github.com/PART-WPO/reach-dashboard
* Interactive Dashboard: https://part-wpo.github.io/reach-dashboard/
* Contact: part.wpo@noaa.gov

REACH is maintained by NOAA's Weather Program Office (WPO) to improve transparency, accessibility, and discoverability of publicly available research outputs generated through WPO-supported activities.

