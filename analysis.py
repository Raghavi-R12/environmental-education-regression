import pandas as pd
import numpy as np
import statsmodels.formula.api as smf

# Load Data
pollution = pd.read_csv("pollution_us_2000_2016.csv")
naep = pd.read_csv("naep_math_grade8.csv")

# Clean/Process
naep = naep[naep['Group'] == 'All students'].copy()
pollution['Year'] = pd.to_datetime(pollution['Date.Local']).dt.year
pollution_agg = pollution.groupby(['State', 'Year']).agg({
    'NO2.Mean': 'mean', 'O3.Mean': 'mean', 'CO.Mean': 'mean'
}).reset_index()

# Merge
df = pd.merge(naep, pollution_agg, on=['State', 'Year'])

# Add Controls
urban_states = ["California", "New York", "Texas", "Florida", "Illinois"]
df['Urban'] = df['State'].apply(lambda x: 1 if x in urban_states else 0)
df['Free_Lunch_Pct'] = 0.45 

# Rename columns to avoid dots in formula
df = df.rename(columns={'NO2.Mean': 'NO2_Mean'})

# Regression Model
model1 = smf.ols('Average_Score ~ NO2_Mean + Free_Lunch_Pct', data=df).fit()

print("--- Regression Model Summary ---")
print(model1.summary())

# Policy Simulation
current_score = model1.predict({'NO2_Mean': 25, 'Free_Lunch_Pct': 0.45})
reduced_score = model1.predict({'NO2_Mean': 15, 'Free_Lunch_Pct': 0.45})
print(f"\nPolicy Simulation: Reduction from 25ppb to 15ppb results in {reduced_score[0] - current_score[0]:.2f} point change.")
