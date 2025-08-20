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

## Project Scoping
For this project I am looking at financial market data. The idea is to see how factors like interest rates, inflation, and stock indices might affect market movements.  

The stakeholder I am thinking of is an individual investor who just wants to make smarter choices. The answer I want to give is partly descriptive (summarizing past patterns) and partly predictive (to say something about possible future outcomes).  

The aim is to end up with a small data-driven tool that helps in making investment decisions with more confidence.

## Project Scoping (Stage 1)

**Problem:** Summarize financial market conditions and simple signals so an individual investor can make quick, informed decisions.  
**Stakeholder/User:** Individual investor (daily pre-market check).  
**Useful Answer:** Descriptive + simple predictive cues; small dashboard/notebook with metrics and plots.  
**Assumptions/Constraints:** Public data; daily cadence; keep secrets out of repo.  
**Risks:** API limits, data quality, sentiment noise.  
**Lifecycle → Deliverables:**  
- Stage 0 → env/repo (done)  
- Stage 1 → scoping + stakeholder memo (this HW)  
- Stage 2 → tooling (`.env`, `src/config.py`)  
- Stage 3 → fundamentals (`src/utils.py`, pandas/NumPy demo)  
- Stage 4 → ingestion pipeline (API/scrape to `/data/raw`)
