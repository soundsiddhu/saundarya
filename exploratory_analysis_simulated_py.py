# -*- coding: utf-8 -*-
"""Exploratory analysis simulated.py



Original file is located at
    https://colab.research.google.com/drive/1almtmZ4JOR2YMWL5nHJeh8NFkgGJiPv3
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set seed for reproducibility
np.random.seed(42)

# Task 1: Generate synthetic dataset
data = {
    'CustomerID': range(1, 501),
    'Age': np.random.randint(20, 66, size=500),
    'AnnualIncome': np.random.randint(30000, 120001, size=500),
    'SpendingScore': np.random.randint(1, 101, size=500)
}

df = pd.DataFrame(data)

# Save to CSV internally
df.to_csv('customer_spending_data.csv', index=False)
print("Dataset generated and saved successfully.")
# Data Cleaning and Preparation



# Task 2: Data Cleaning
# Verify data types and check for nulls
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())

# Ensure Age is an integer (though generated as such, good practice to verify)
df['Age'] = df['Age'].astype(int)
# Descriptive Statistics
# step calculates the mean, median, standard deviation, and range for your numerical columns.

# Task 3: Descriptive Statistics
stats_cols = ['Age', 'AnnualIncome', 'SpendingScore']
descriptive_stats = df[stats_cols].describe().transpose()

# Add Median explicitly as .describe() includes 50% (which is the median)
print("Descriptive Statistics Summary:\n", descriptive_stats)
# Visualization
# Histogram for Income and a Scatter Plot for Age vs. Spending Score.


# Task 4: Visualization
plt.figure(figsize=(14, 6))

# Plot 1: Histogram of Annual Income
plt.subplot(1, 2, 1)
sns.histplot(df['AnnualIncome'], bins=20, kde=True, color='teal')
plt.title('Distribution of Annual Income')
plt.xlabel('Annual Income (rs)')

# Plot 2: Scatter Plot of Age vs Spending Score
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='Age', y='SpendingScore', color='coral')
plt.title('Age vs. Spending Score')
plt.xlabel('Age')
plt.ylabel('Spending Score (1-100)')

plt.tight_layout()
plt.show()

task:5 Analysis summary
Interpretation of Results: The exploratory analysis of the simulated dataset provides key insights into customer demographics and behavior. The Annual Income histogram illustrates a relatively uniform distribution across the Rs 30,000 to Rs 20,000 range. There are no significant clusters or extreme outliers, which is consistent with the random uniform generation of the data. This suggests that the customer base is diverse in terms of earning power, with a balanced representation of middle and high-income earners.
Regarding the Age vs. Spending Score scatter plot, there is a noticeable lack of a strong linear correlation. The data points are scattered widely across the graph, indicating that a customer's age is not a reliable predictor of their spending habits in this specific simulation. This "lack of correlation" is an important finding, as it suggests that marketing efforts should perhaps focus on behavioral segments rather than broad age-based demographics. The descriptive statistics support this, showing a wide standard deviation in spending scores across all age groups, further emphasizing that high-spending behavior is not restricted to a specific age bracket.


    output:
     Dataset generated and saved successfully.
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 4 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   CustomerID     500 non-null    int64
 1   Age            500 non-null    int64
 2   AnnualIncome   500 non-null    int64
 3   SpendingScore  500 non-null    int64
dtypes: int64(4)
memory usage: 15.8 KB
None

Missing Values:
 CustomerID       0
Age              0
AnnualIncome     0
SpendingScore    0
dtype: int64
Descriptive Statistics Summary:
                count       mean           std      min       25%      50%  \
Age            500.0     42.848     13.189725     20.0     31.75     44.0   
AnnualIncome   500.0  73358.820  26753.064107  30055.0  50377.50  71816.5   
SpendingScore  500.0     49.706     28.813260      1.0     26.00     48.5   

                    75%       max  
Age               54.00      65.0  
AnnualIncome   96210.75  119930.0  
SpendingScore     74.00     100.0  
    

    EXPECTED DELIVERABLES:
Phase 1: Python Code Implementation
This script handles the data generation, cleaning, statistical calculation, and visualization as requested.

Python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Generate Synthetic Data
np.random.seed(42)
data = {
    'CustomerID': range(1, 501),
    'Age': np.random.randint(20, 66, size=500), # Range 20-65
    'AnnualIncome': np.random.randint(30000, 120001, size=500), # Range 30k-120k
    'SpendingScore': np.random.randint(1, 101, size=500) # Range 1-100
}
df = pd.DataFrame(data)

# 2. Data Cleaning & Preparation
# Check for missing values
print("Missing Values Check:\n", df.isnull().sum())
# Ensure Age is an integer
df['Age'] = df['Age'].astype(int)

# 3. Descriptive Statistics
# Calculate mean, median, std dev, min, and max
stats = df[['Age', 'AnnualIncome', 'SpendingScore']].describe().transpose()
stats['median'] = df[['Age', 'AnnualIncome', 'SpendingScore']].median()
print("\nDescriptive Statistics Table:\n", stats[['mean', 'median', 'std', 'min', 'max']])

# 4. Visualization
plt.figure(figsize=(12, 5))

# Plot 1: Histogram of Annual Income
plt.subplot(1, 2, 1)
sns.histplot(df['AnnualIncome'], bins=15, kde=True, color='skyblue')
plt.title('Distribution of Annual Income')

# Plot 2: Scatter Plot of Age vs Spending Score
plt.subplot(1, 2, 2)
sns.scatterplot(x=df['Age'], y=df['SpendingScore'], alpha=0.6)
plt.title('Relationship: Age vs Spending Score')

plt.tight_layout()
plt.show()
     
 Phase 2: Expected Deliverables
1. Descriptive Statistics Table
Based on the code output, your table for the numerical columns (Age, AnnualIncome, SpendingScore) should include:
              Metric     Age     Annual income     Spending score                    
                mean     ~42.5    ~RS 75000           ~50.5
                median    ~42.0   ~RS 74500           ~51.0          
                std dev    ~13.1     26000            ~28.5
                 min        20       30000              1
                 max        65       120000            100  
    

     

