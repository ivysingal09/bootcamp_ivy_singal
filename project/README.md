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

## Feature Engineering  

From the cleaned dataset (`IYR_cleaned_project.csv`), we created new features to capture **trends, volatility, and momentum** in real estate ETF data.  

**Features added:**  
- **Lagged returns**: `ret_lag1`, `ret_lag5`  
- **Moving averages (MA)**: `ma_7`, `ma_21`, `ma_63`, `ma_126`  
- **Rolling volatility**: `vol_7`, `vol_21`, `vol_63`  
- **Momentum**: `mom_10`, `mom_20`, `mom_60`  
- **Cumulative return**: `cum_return`  
- **Technical indicators**: `ema_12`, `ema_26`, `rsi_14`  

**Output saved as**:  
`project/data/processed/IYR_features_project.csv`
