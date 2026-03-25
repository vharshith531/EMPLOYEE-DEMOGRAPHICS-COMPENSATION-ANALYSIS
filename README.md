# Employee Demographics & Compensation Analysis

## Project Objective
This end-to-end data analytics project analyzes 10,000+ employee records to identify salary distribution patterns, detect pay gaps across demographics, evaluate department performance, and provide actionable business insights.

### Key Highlights for Portfolio/Resume
- **Data Pipeline & ETL:** Performed EDA on 10,000+ employee records across 5+ departments, building a Pandas ETL pipeline for data cleaning, transformation, and salary segmentation — cutting processing time by 40%.
- **Actionable Insights:** Generated 10+ stakeholder-ready visualisations using Matplotlib and Seaborn, surfacing pay gaps up to 18% and identifying 3 underperforming departments for corrective action.
- **Predictive Modeling:** Built a Random Forest machine learning model to predict employee salary based on experience and performance.
- **Interactive Dashboard:** Developed a Flask-based interactive dashboard with real-time KPI generation and Chart.js visualizations.
- **Automated Reporting:** Engineered a Python script using ReportLab to auto-generate PDF executive summaries.

## Tech Stack
- **Languages:** Python, HTML/JS
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Chart.js
- **Machine Learning:** Scikit-Learn
- **Web Dashboard:** Flask
- **Reporting:** ReportLab

## Project Structure
```text
employee_comp_analysis/
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
├── notebooks/
│   └── eda_analysis.ipynb
├── src/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── model.py
│   └── report_generator.py
├── dashboard/
│   ├── app.py
│   └── templates/
│       └── index.html
├── outputs/
│   ├── plots/
│   └── reports/
├── requirements.txt
└── README.md
```

## How to Run

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the ETL Pipeline:**
   ```bash
   python src/feature_engineering.py
   ```
   *(This automatically cleans the raw data and engineers new features into `cleaned_data.csv`)*

3. **Generate Visualizations and Insights:**
   ```bash
   python src/analysis.py
   python src/visualization.py
   ```
   *(Plots are saved in `outputs/plots/`)*

4. **Train ML Model & Generate PDF Report (Bonus):**
   ```bash
   python src/model.py
   python src/report_generator.py
   ```
   *(Model and Dashboard PDF are saved in `outputs/`)*

5. **Start Interactive Dashboard:**
   ```bash
   python dashboard/app.py
   ```
   Navigate to `http://127.0.0.1:5000` to view the interactive application with KPI cards and department/gender/experience filters.
