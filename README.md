# Stack Overflow Survey Analysis

## Overview
This project analyzes the technology sector, specifically focusing on software developer compensation, popular programming languages, and modern work arrangements (e.g., remote work and AI tool adoption). The goal is to provide data-driven insights into the current tech job market to help professionals and companies benchmark salaries and align with industry trends.

## Dataset
- **Source:** Stack Overflow Developer Survey 2024
- **Size:** Over 60,000 raw survey responses. Filtered to approximately 33,000 rows containing valid compensation data.
- **Location:** The raw data is located in `data/raw/` and the cleaned data is in `data/processed/`.
- **Key Columns:** `ConvertedCompYearly` (Salary), `LanguageHaveWorkedWith`, `WorkExp`, `RemoteWork`, `JobSat`, `AISelect`.

## Team Information
- **Team Name:** kuch bhi
- **Institute:** Newton School of Technology
- **Team Members:** 
    1. Vansh Singhal (Cyber-Vansh)
    2. Vaibhav Singh (Vaibhav-fusion)
    3. Md. Faisal (faisal0006)
    4. Shashwat Sharma (portneon)
    5. Soham Saranga (saranganet)

## Repository Structure
- `data/`: Contains raw and processed datasets.
- `notebooks/`: Jupyter notebooks for ETL, EDA, and statistical analysis.
- `scripts/`: Python scripts (e.g., `etl_pipeline.py`) for automated data processing.
- `reports/`: Contains the final project report and presentation.
- `tableau/`: Contains dashboard links and screenshots.