import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

states = ["California", "New York", "Texas", "Florida", "Illinois", "Mississippi", "New Mexico", "Alabama", "Louisiana"]
years = list(range(2000, 2017, 2))

# 1. Generate Mock Pollution Data
rows_poll = []
for state in states:
    for year in years:
        rows_poll.append({
            "Date.Local": f"{year}-06-15",
            "State": state,
            "NO2.Mean": np.random.uniform(10, 35),
            "O3.Mean": np.random.uniform(0.015, 0.035),
            "CO.Mean": np.random.uniform(0.1, 0.9)
        })
df_pollution = pd.DataFrame(rows_poll)
df_pollution.to_csv("pollution_us_2000_2016.csv", index=False)

# 2. Generate Mock NAEP Data
rows_naep = []
for state in states:
    for year in years:
        rows_naep.append({
            "Year": year,
            "State": state,
            "Group": "All students",
            "Average_Score": np.random.uniform(265, 298)
        })
df_naep = pd.DataFrame(rows_naep)
df_naep.to_csv("naep_math_grade8.csv", index=False)

print("Mock datasets successfully created inside your project folder!")