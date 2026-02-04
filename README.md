Project Overview:
This project focuses on performing Exploratory Data Analysis (EDA) on a synthetic dataset representing customer transactions. The primary goal is to use Python to clean data, perform statistical analysis, and visualize trends to draw business insights.

Project Tasks & Implementation:
1. Data Generation
The project begins by using Pandas and NumPy to create a synthetic dataset of 500 records.

CustomerID: A unique sequential identifier.

Age: Random integers between 20 and 65.

AnnualIncome: Random values between RS30k and RS120k.

SpendingScore: Random scores ranging from 1 to 100.

2. Data Cleaning & Preparation:
To ensure the analysis is accurate, the data is loaded into a Pandas DataFrame for validation:

Missing Values: A check is performed to identify any null entries.

Type Casting: 'Age' is explicitly converted to an integer format to ensure mathematical consistency.

3. Descriptive Statistics:
We calculate five key metrics for the Age, Annual Income, and Spending Score columns:

Mean: The average value of the data.

Median: The middle point of the dataset.

Standard Deviation: The measure of how spread out the numbers are.

Minimum and Maximum: The range boundaries of the data.

4. Data Visualization:
Two distinct plots are generated to understand the data distribution and relationships:

Histogram: Displays the distribution of 'AnnualIncome' to see where most customers fall on the pay scale.

Scatter Plot: Explores the relationship between 'Age' and 'SpendingScore' to identify if age influences spending behavior.

 Expected Deliverables:
As per the project requirements, the final submission includes:

Python Code Implementation: The complete script for generation, cleaning, and visualization as plain text.

Statistical Table: A clear output of the mean, median, standard deviation, and range for all numerical variables.

Textual Interpretation: A 150–200 word summary explaining whether a correlation exists (or lacks thereof) between the variables observed in the plots.

Conclusion:
The analysis typically reveals whether demographics like Age or Income directly impact a customer's Spending Score. In most random simulations, a lack of correlation is observed between Age and Spending, suggesting that spending patterns are independent of customer age.
