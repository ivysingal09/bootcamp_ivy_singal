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

## Stage 5: Data Storage Homework

This stage demonstrates the ability to save and load tabular data using different file formats and environment-based folder configuration:

- Created environment variables for raw and processed data directories (`.env`)
- Saved a sample DataFrame to:
  - **CSV**: `data/raw/example.csv`
  - **Parquet**: `data/processed/example.parquet`
- Verified both files by reading them back into pandas and comparing (same shape and content)

