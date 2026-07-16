# Environmental Education Regression Analysis

This project implements a full end-to-end data science pipeline to analyze the relationship between air quality (NO2 levels) and 8th-grade math performance. This analysis provides a quantitative framework for policymakers to estimate the educational impact of environmental improvements.

## Project Overview

The project is structured as a modular pipeline:
*   **Data Engineering:** A custom script (`generate_mock_data.py`) processes raw environmental and educational datasets.
*   **Statistical Modeling:** An Ordinary Least Squares (OLS) regression model (`analysis.py`) quantifies the correlation between pollutants and test scores.
*   **Policy Simulation:** A predictive tool translates statistical findings into decision-ready impact estimates.
*   **Data Visualization:** The pipeline generates visual trends to facilitate data-driven decision-making.

## Code, Process & Output Mapping

This table outlines how the codebase translates into the final analytical insights:

| File | Process (The Logic) | Resulting Output (The Insight) |
| :--- | :--- | :--- |
| **`generate_mock_data.py`** | Processes raw data from `naep_math_grade8.csv` and `pollution_us_2000_2016.csv`. | A cleaned dataset ready for statistical analysis. |
| **`analysis.py`** | Fits an OLS Regression model using `statsmodels` to find the "line of best fit": Score = β0 + β1(NO2). | Console output showing the regression coefficient (-0.1887) and p-values. |
| **`analysis.py` (Simulation)** | Plugs input values (e.g., 25 ppb and 15 ppb) into the model to solve for the performance delta. | A calculated projection showing a 1.89-point performance increase. |
| **Analysis Plots** | The scripts generate visuals directly from the data/model results. | `pollution_vs_math.png` and `analysis_output.png` illustrating the correlation trend. |

## Technical Methodology

*   **The Math:** The model fits the linear equation: Math Score = β0 + β1(NO2) + ε.
*   **The Logic:** OLS minimizes the sum of the squared differences (residuals) between observed math scores and the scores predicted by the model, providing the most accurate "line of best fit."

## Key Insights & Output Interpretation

*   **Model Significance:** The analysis identified a strong negative correlation between NO2 levels and math performance (coefficient: -0.1887). This means for every 1 ppb increase in NO2, average math scores drop by approximately 0.1887 points.
*   **Policy Impact:** Using the simulation tool, we estimated that a reduction of air pollution from 25 ppb to 15 ppb could yield a 1.89-point increase in average 8th-grade math scores.

## Repository Structure

*   `analysis.py`: Contains the core OLS regression logic and policy simulation engine.
*   `generate_mock_data.py`: Script for generating/processing the study data.
*   `naep_math_grade8.csv` & `pollution_us_2000_2016.csv`: Underlying raw datasets.
*   `analysis_output.png` & `pollution_vs_math.png`: Visual representations of the regression results.
*   `README.md`: Project documentation.

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Raghavi-R12/environmental-education-regression.git](https://github.com/Raghavi-R12/environmental-education-regression.git)
    cd environmental-education-regression
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execute the pipeline:**
    ```bash
    python3 generate_mock_data.py
    python3 analysis.py
    ```

---
**Author:** Raghavi Ravichandran
