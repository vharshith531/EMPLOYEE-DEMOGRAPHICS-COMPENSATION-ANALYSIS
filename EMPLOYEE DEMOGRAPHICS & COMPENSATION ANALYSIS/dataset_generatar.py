import pandas as pd
import numpy as np

np.random.seed(42)

n = 10000

departments = ['HR', 'Engineering', 'Sales', 'Marketing', 'Finance']
job_roles = ['Manager', 'Analyst', 'Developer', 'Executive', 'Lead']
education_levels = ['Bachelors', 'Masters', 'PhD']
locations = ['Chennai', 'Bangalore', 'Hyderabad', 'Mumbai', 'Delhi']

data = pd.DataFrame({
    "Employee_ID": range(1, n+1),
    "Age": np.random.randint(22, 60, n),
    "Gender": np.random.choice(['Male', 'Female'], n),
    "Department": np.random.choice(departments, n),
    "Job_Role": np.random.choice(job_roles, n),
    "Experience_Years": np.random.randint(0, 30, n),
    "Education_Level": np.random.choice(education_levels, n),
    "Location": np.random.choice(locations, n),
    "Performance_Rating": np.random.randint(1, 6, n)
})

# Salary logic (realistic)
base_salary = {
    'HR': 30000,
    'Engineering': 60000,
    'Sales': 40000,
    'Marketing': 35000,
    'Finance': 50000
}

data["Salary"] = data.apply(
    lambda x: base_salary[x["Department"]] +
              x["Experience_Years"] * 2000 +
              np.random.randint(-5000, 5000),
    axis=1
)

# Bonus calculation
data["Bonus"] = (data["Salary"] * np.random.uniform(0.05, 0.20, n)).astype(int)

# Joining Date
data["Joining_Date"] = pd.to_datetime(
    np.random.choice(pd.date_range("2010-01-01", "2023-01-01"), n)
)

# Save dataset
data.to_csv("employee_data_10000.csv", index=False)

print("Dataset created successfully!")