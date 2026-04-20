# Data Dictionary

| Column Name | Description | Data Type |
| :--- | :--- | :--- |
| `ResponseId` | Unique identifier for each respondent | Integer |
| `MainBranch` | Describes whether the respondent is a professional developer, student, etc. | Categorical |
| `Age` | Age range of the respondent | Categorical |
| `EdLevel` | Highest level of formal education completed | Categorical |
| `Employment` | Current employment status (full-time, part-time, independent contractor) | Categorical |
| `WorkExp` | Number of years of professional coding experience | Numeric (Float) |
| `DevType` | Describes the respondent's primary developer role (e.g., Full-stack, Data Engineer) | Categorical |
| `OrgSize` | Number of employees in the respondent's organization | Categorical |
| `RemoteWork` | Describes the respondent's current remote work situation (In-person, Remote, Hybrid) | Categorical |
| `Country` | Country where the respondent resides | Categorical |
| `ConvertedCompYearly` | Total yearly compensation converted to USD | Numeric (Float) |
| `JobSat` | Respondent's self-reported job satisfaction | Categorical |
| `LanguageHaveWorkedWith` | Multi-select string of programming languages the respondent has worked with | String |
| `DatabaseHaveWorkedWith` | Multi-select string of databases the respondent has worked with | String |
| `AISelect` | Does the respondent currently use AI tools? (Yes/No/Plan to) | Categorical |
| `AISent` | Respondent's sentiment towards AI tools | Categorical |
| `Experience_Level` | Derived column grouping WorkExp into predefined bins (e.g., 0-2 years, 3-5 years) | Categorical |
| `Avg_Comp_by_Country` | Derived KPI: Average yearly compensation within the respondent's country | Numeric (Float) |
| `Is_Data_Scientist` | Boolean flag indicating if the respondent is a Data Professional | Boolean |
| `Primary_Language` | Derived KPI: First programming language listed for filtering | String |
