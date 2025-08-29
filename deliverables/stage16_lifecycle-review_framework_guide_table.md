# Applied Financial Engineering — Framework Guide Template

This Framework Guide is a structured reflection tool.  
Fill it in as you progress through the course or at the end of your project.  
It will help you connect each stage of the **Applied Financial Engineering Lifecycle** to your own project, and create a portfolio-ready artifact.

---

## How to Use
- Each row corresponds to one stage in the lifecycle.  
- Use the prompts to guide your answers.  
- Be concise but specific — 2–4 sentences per cell is often enough.  
- This is **not a test prep sheet**. It’s a way to *document, reflect, and demonstrate* your process.

---

## Framework Guide Table

| Lifecycle Stage | What You Did | Challenges | Solutions / Decisions | Future Improvements |
|-----------------|--------------|------------|-----------------------|---------------------|
| **01. Problem Framing & Scoping** | Predicted stock price trends. | Too many features at start. | Focused on 3 key indicators, daily resolution. | Define success metrics earlier. |
| **02. Tooling Setup** | Used Python, pandas, sklearn, Jupyter. | Env mismatch at first. | Fixed with requirements.txt. | Use Docker for consistency. |
| **03. Python Fundamentals** | Applied loops, functions, pandas ops. | Slow code sometimes. | Vectorized operations. | Practice optimization more. |
| **04. Data Acquisition / Ingestion** | Pulled data from CSV + APIs. | Missing values and schema drift. | Cleaned + standardized input format. | Automate ingestion pipeline. |
| **05. Data Storage** | Stored in CSV/JSON. | Scaling issues with big files. | Split and managed versions. | Use database (SQL/Parquet). |
| **06. Data Preprocessing** | Cleaned nulls, normalized features. | Noisy data. | Used imputation + scaling. | Add feature pipelines. |
| **07. Outlier Analysis** | Detected extreme values. | Hard to separate errors vs real events. | Used capping and IQR. | Try anomaly detection models. |
| **08. Exploratory Data Analysis (EDA)** | Visualized trends, correlations. | Some misleading correlations. | Cross-checked with domain knowledge. | Add more domain-driven visuals. |
| **09. Feature Engineering** | Built ratios, lags, rolling averages. | Choosing features was tricky. | Kept interpretable features. | Automate feature selection. |
| **10. Modeling (Regression / Time Series / Classification)** | Trained regression + tree models. | Overfitting risk. | Regularized + cross-validation. | Try ensemble and deep models. |
| **11. Evaluation & Risk Communication** | Checked MAE, RMSE, AUC. | Tradeoff between accuracy vs interpretability. | Reported with error bands. | Add confidence intervals. |
| **12. Results Reporting, Delivery & Stakeholder Communication** | Made plots + report. | Explaining errors was hard. | Simplified visuals + summary. | Automate reports. |
| **13. Productization** | Saved model + utils.py. | Keeping code modular. | Added src/ folder + init.py. | Use CI/CD. |
| **14. Deployment & Monitoring** | Defined risks, alerts, KPIs. | Handling drift. | Monitoring plan at data, model, system levels. | Add automated retraining. |
| **15. Orchestration & System Design** | Broke pipeline into tasks (ingest→clean→train→report). | Task dependencies. | Used DAG + logging. | Automate retries + scheduling. |
| **16. Lifecycle Review & Reflection** | Reviewed full repo. | Keeping it organized. | Made checklist + guide. | Improve docs + reusability. |
---

### Reflection Prompts

- **What stage of the lifecycle was hardest for you, and why?**  
  Deployment & monitoring — because handling drift and alerts was new.  

- **Which part of your repo is most reusable in a future project?**  
  The utils.py and model training pipeline (can reuse directly).  

- **If a teammate had to pick up your repo tomorrow, what would help them most?**  
  A clear README + requirements.txt + organized folders.  

- **Which stage was the most difficult for you, and why?**  
  Orchestration — DAGs and dependencies took extra time to understand.  

- **Which stage was the most motivating?**  
  Modeling — fun to test and improve accuracy.  

- **How do the stages connect?**  
  Each builds on the previous (cleaning → features → modeling → deployment).  

- **If you repeated this project, what would you do differently across the lifecycle?**  
  Set success metrics early and automate more steps.  

- **Which skills do you most want to strengthen before your next financial engineering project?**  
  Orchestration, deployment automation, and monitoring tools.  

---