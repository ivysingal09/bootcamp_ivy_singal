# Stage 12 — Results Reporting & Delivery Design

## Executive Summary
We analyzed U.S. Real Estate ETF (IYR) data to forecast next-day closing prices.  
The goal: demonstrate a structured workflow from data collection to risk-aware modeling.  
Final results show our model outperforms a naive baseline, but risks remain.

---

## Problem Setup
- **Domain**: Finance & Real Estate (IYR ETF as proxy for real estate market).  
- **Objective**: Predict next-day closing price.  
- **Stages covered**: Data acquisition, preprocessing, feature engineering, modeling, evaluation.  

---

## Methods
- **Data**: Yahoo Finance (IYR ETF).  
- **Preprocessing**: Cleaned missing values, removed outliers, standardized features.  
- **Feature Engineering**: Lagged returns, moving averages, volatility, momentum, RSI.  
- **Models**:  
  - Stage 10a: Linear Regression (baseline).  
  - Stage 10b: Random Forest with TimeSeriesSplit CV.  

---

## Results
- **Linear Regression (Stage 10a)**: Reasonable baseline fit, interpretable.  
- **Random Forest (Stage 10b)**: Lower MAE & RMSE than naive baseline.  
- **Scenario Comparison**:  
  - Model MAE < Naive MAE (better predictions).  
  - Residuals show fat tails → volatility risk.  

---

## Assumptions
- Features computed without look-ahead.  
- Past relationships between lagged features and future returns hold stable.  
- Training/validation split was time-aware.  

---

## Risks
- **Market regime shifts** (rates, inflation, shocks) can break model.  
- **Residuals non-normal** → extreme moves not well captured.  
- **Overfitting** risk with complex models.  

---

## Scenario Example
- **Model vs Naive**: Model beats naive in MAE/RMSE.  
- **Sensitivity**: Performance could degrade if volatility doubles.  

---

## Next Steps
- Retrain model periodically (e.g., monthly).  
- Extend feature set with macroeconomic indicators.  
- Consider simpler deployment (linear + risk bands) for transparency.  

---

## Conclusion
The structured pipeline demonstrates **end-to-end applied data science in finance**:  
from problem framing to risk communication.  
Stakeholders can use this to guide decisions, but **should not rely solely on predictions without monitoring uncertainty and risks**.

