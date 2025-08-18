# REACH Tool  
**Research Explorer for Articles, Code, and Hosted Data (REACH)**  

The [REACH Tool](https://wpo.noaa.gov/reach/) is a web-based open science platform developed by NOAA’s Weather Program Office (WPO) to provide public access to research outputs generated from WPO-funded projects.  

REACH turns static project lists into a **searchable, filterable, and user-friendly interface**, enabling users to:  
- 🔍 Search research outputs by keyword or award number  
- 🗂 Filter by program, funded year, output type, and other metadata  
- 📑 View outputs in structured card format with direct links to source materials  
- 🤝 Highlight collaborations through Partnership Cards  

## 📊 Data Sources  

**Primary Data Source**  
- Metadata originates from **Division-level Open Science Smartsheet Trackers** (maintained by each WPO division).  
- Trackers are updated when new outputs are identified, including **journal articles detected monthly via the CrossRef API**.  
- A **consolidated WPO Smartsheet Report** merges outputs from all divisions into a single dataset (award numbers, titles, authors, output types, hazard categories, resource links).  
- A **Google Apps Script** retrieves this dataset via the Smartsheet API, cleans/normalizes it, and uploads it as a CSV to this GitHub repository.  

**Partnership Data**  
- Embedded in the CSV with metadata (partnership name, organization, logo URL, and detail links).  
- Partnership Cards in the REACH UI provide visual attribution and navigation to related resources.

## 🔄 End-to-End Data Workflow  

### Step 1 – Automated Publication Detection (CrossRef API)  
- Monthly automation checks the **CrossRef API** for new publications containing WPO award numbers.  
- The PART Program receives automated email alerts when new matches are found.  
- *(See SOP for Collecting and Recording WPO Research Outputs for more details.)*  

### Step 2 – Smartsheet Data Entry  
- Newly detected publications are entered into **Division-level Open Science Smartsheet Trackers** (one per division).  
- Trackers capture metadata such as:  
  - Title  
  - Authors  
  - DOI  
  - Output type  
  - Award number(s)  
  - Program  
  - Links  

### Step 3 – Division Data Consolidation  
- Data from all three divisions is merged into a **single master sheet** using a Smartsheet Report.  
- This consolidated report serves as the source for **REACH data exports**.  

### Step 4 – Automated Data Retrieval (Google Apps Script + Smartsheet API)  
- A **Google Apps Script** calls the Smartsheet API to pull the consolidated report data.  

### Step 5 – Data Cleaning & HTML Preparation  
The Google Apps Script processes the data by:  
- Standardizing dates into consistent `MM/DD/YY` or `MM/DD/YYYY` formats  
- Combining title and abstract text into a single **search-optimized field**  
- Truncating abstracts for brief UI display  
- Consolidating multiple link fields into one column  
- Formatting output types with **HTML icons, labels, and color codes**  
- Adding **open access labels and icons** based on availability  
- Normalizing program and “Funded By” names  
- Sanitizing text to replace problematic characters and remove non-ASCII  
- Escaping special characters for HTML safety before CSV upload  

### Step 6 – Automated CSV Upload (Google Apps Script + GitHub API)  
- The cleaned dataset is saved as a **CSV file**.  
- The script calls the **GitHub API** to commit and push the CSV to PART’s REACH GitHub repository.  

### Step 7 – Public Rendering in REACH (GitHub Pages)  
- The REACH interface is served via a static HTML index file on **GitHub Pages**.  
- **CSS** defines the responsive grid layout, card formatting, colors, fonts, and accessibility.  
- On page load:  
  - The CSV is fetched from **GitHub’s Raw Content API**  
  - **PapaParse.js** parses CSV → JavaScript objects  
  - **Choices.js** enables multi-select dropdown filtering  
  - Results are displayed as responsive **cards**  
  - **Partnership Cards** replace standard program info for partnership outputs  

### Step 8 – Public Embedding on the WPO Website  
- The live REACH GitHub Page is embedded via an **iframe** on the WPO’s public-facing WordPress site.  
- Visitors can access the tool directly without leaving the WPO site.  

## 🔁 Update & Refresh Process  

- The **Google Apps Script** is configured with a **time-based trigger** to run automatically on the **15th of every month**.  
- When triggered, the script:  
  1. Calls the Smartsheet API to pull the latest consolidated data  
  2. Cleans, formats, and enriches the dataset  
  3. Uploads the updated CSV to the WPO GitHub repository via the GitHub API  
- The REACH Tool fetches the updated CSV automatically on the next page load, ensuring users always see the most current research outputs.  

## ⚙️ APIs, Libraries, and External Services  

| Component              | Purpose                                                      |
|-------------------------|--------------------------------------------------------------|
| **CrossRef API**        | Detects new publications tied to WPO award numbers           |
| **SmartsheetGov API**   | Retrieves consolidated research metadata                     |
| **GitHub API**          | Uploads updated CSV to repository                            |
| **PapaParse.js**        | Parses CSV → JS objects for REACH UI                         |
| **Choices.js**          | Provides multi-select dropdown filters                       |
| **GitHub Raw Content**  | Serves public CSV for REACH to fetch                         |

## 🎨 UI/UX Features  

- 🔍 Keyword and award number search for quick discovery of relevant outputs  
- 🗂 Filter options by **WPO Program, Output Type, Open Access Status, and Date**  
- 🎨 Color-coded headers and icons to visually distinguish output types  
- ⏱ Most recent outputs appear first for faster access to new resources  
- 🤝 **Partnership Cards** display outputs from WPO partnerships (partner name, organization, logo, links)  
- 📚 Top-right card icon indicates availability in the **NOAA Institutional Repository (IR)**  
- ⬇️ Option to download a customized list of search results (metadata + DOI links) for offline reference  

## 🚀 Hosting & Deployment  

- **Static Hosting:** GitHub Pages  
- **Fully Automated Pipeline:**  
  1. CrossRef detects new publications → Email sent to PART  
  2. PART enters data into Division Smartsheet Trackers  
  3. Consolidated Smartsheet Report merges all division outputs  
  4. Google Apps Script fetches consolidated report via Smartsheet API  
  5. Script cleans/normalizes data and saves as CSV  
  6. Script uploads CSV to GitHub via GitHub API  
  7. REACH fetches CSV on page load for public display  
  8. REACH GitHub Page is embedded via an **iframe** on WPO’s WordPress site  

## ⚠️ Known Limitations  

- Pipeline depends on **accurate award number entry** in publications for detection  
- Initial data entry into Smartsheet Trackers is still **manual**  
- API rate limits (GitHub, Smartsheet) may impact large updates  

## 🔮 Future Enhancements  

- Direct **CrossRef API → Smartsheet Tracker** integration to eliminate manual entry  
- Automatic **DOI metadata enrichment** (abstracts, citation formats)  
