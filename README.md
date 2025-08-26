# Bootcamp Repository

## Folder Structure
- **homework/** → All homework contributions go here.
- **project/** → All project contributions go here.
- **class_materials/** → Local files only, not pushed to GitHub.

## Homework Rules
- Each homework must be in its own folder (homework0, homework1, ...).
- Include all required files.

## Project Rules
- Keep files organized and clearly named.

# Bootcamp Homework – Ivy Singal  

This repository contains my homework submissions for the Bootcamp.  
It is structured to keep code, data, notebooks, and reports organized.

---

## 📂 Repository Layout  
- **/data** – Datasets used in assignments (raw/processed).  
- **/src** – Source code and helper scripts.  
- **/notebooks** – Drafts and exploration notebooks.  
- **/homework** – Final homework submissions (by stage).  

---

## Homework 1 – Stage 1: Problem Framing & Scoping  

### Problem Statement  
Credit risk assessment remains one of the most critical challenges in financial services. Traditional models depend mainly on bureau data and repayment history, which disadvantages borrowers with limited or no credit history. This project explores a more inclusive credit risk modeling framework that combines traditional signals with alternative data sources (e.g., transaction behavior, employment stability, digital footprints) to improve prediction accuracy, fairness, and financial inclusion.  

### Scope of Work  
- Identify limitations of existing credit risk assessment approaches.  
- Propose data sources (traditional + alternative) and justify their relevance.  
- Outline potential modeling approaches (machine learning, interpretable models).  
- Consider fairness, ethical, and regulatory aspects in evaluation.  
- Define clear success criteria: accuracy, fairness, and robustness.  

### Expected Outcomes  
- More accurate credit default prediction compared to baseline bureau-only models.  
- Expanded access to credit for underserved or “thin-file” borrowers.  
- Framework aligned with ethical and regulatory standards.  


For this stage, I worked with environment-driven paths (`DATA_DIR_RAW`, `DATA_DIR_PROCESSED`) to save and reload data in multiple formats.

### Files Created

- `data/raw/example.csv`
- `data/raw/example.csv.gz`
- `data/processed/example.parquet`
- `data/processed/example.snappy.parquet`

### Validation
Both CSV and Parquet were reloaded successfully and the data matched exactly (`Alice`, `Bob`, `Charlie`).

### File Sizes (KB)
- CSV: **0.03**
- CSV (gzip): **0.07**
- Parquet: **1.62**
- Parquet (snappy): **1.62**

### Observations
- For very small datasets, CSV may look smaller because Parquet carries schema + metadata overhead.  
- On larger datasets, **Parquet is typically smaller and much faster** for analytics because of its binary, columnar format and built-in compression.  
- CSV is human-readable and simple to share, but inefficient for storage and queries.  
- Parquet is not human-readable, but it is the better choice for scalable storage and analytical workloads.

**Conclusion:**  
Use **CSV** for small / human-readable cases.  
Use **Parquet** for efficient, large-scale data storage and analytics.
## Stage 5 – Data Storage

## Stage 6 – Data Preprocessing

This stage covers data cleaning and normalization using helper functions in [src/cleaning.py](src/cleaning.py).

- 📓 Notebook: [stage06_data-preprocessing_homework-starter.ipynb](notebooks/stage06_data-preprocessing_homework-starter.ipynb)  
- 🧹 Functions: [cleaning.py](src/cleaning.py)  
- 📂 Processed Dataset: [sample_data_cleaned.csv](data/processed/sample_data_cleaned.csv)  

Steps performed:
1. Filled missing values with column medians  
2. Dropped columns/rows with too many missing values  
3. Normalized numeric columns to [0,1]  
