# Real Estate Finance Project

## Purpose
This project explores real estate price trends to support better investment decisions.

## Folder Structure
- data/ → datasets
- data/raw/ → unmodified source data
- notebooks/ → Jupyter notebooks for analysis
- src/ → reusable Python scripts
- docs/ → reports and documentation


## Data Storage
- **data/raw/** → original unmodified datasets (e.g., `house_prices_sample_project.csv`)
- **data/processed/** → cleaned or transformed datasets (e.g., `house_prices_processed_project.csv`)
- All code should load data using paths from the `.env` file (e.g., `os.getenv("DATA_DIR")`).
