import pandas as pd

print("Running ETL pipeline...")

df = pd.read_csv('data/raw/survey_results_public.csv', low_memory=False)

columns_to_keep = [
    'ResponseId', 'MainBranch', 'Age', 'EdLevel', 'Employment', 
    'WorkExp', 'DevType', 'OrgSize', 'RemoteWork', 'Country', 
    'ConvertedCompYearly', 'JobSat', 'LanguageHaveWorkedWith', 
    'DatabaseHaveWorkedWith', 'AISelect', 'AISent'
]

df_cleaned = df[columns_to_keep]

df_cleaned = df_cleaned.dropna(subset=['ConvertedCompYearly'])

categorical_cols = [
    'Age', 'EdLevel', 'Employment', 'DevType', 'OrgSize', 
    'RemoteWork', 'JobSat', 'LanguageHaveWorkedWith', 
    'DatabaseHaveWorkedWith', 'AISelect', 'AISent'
]

for col in categorical_cols:
    mode_val = df_cleaned[col].mode()[0]
    df_cleaned[col] = df_cleaned[col].fillna(mode_val)

df_cleaned['WorkExp'] = pd.to_numeric(df_cleaned['WorkExp'], errors='coerce')
median_exp = df_cleaned['WorkExp'].median()
df_cleaned['WorkExp'] = df_cleaned['WorkExp'].fillna(median_exp)

q_low = df_cleaned['ConvertedCompYearly'].quantile(0.01)
q_hi  = df_cleaned['ConvertedCompYearly'].quantile(0.99)

df_cleaned = df_cleaned[df_cleaned['ConvertedCompYearly'] >= q_low]
df_cleaned = df_cleaned[df_cleaned['ConvertedCompYearly'] <= q_hi]

df_cleaned.to_csv('data/processed/cleaned_survey_results.csv', index=False)

print("ETL pipeline finished.")
