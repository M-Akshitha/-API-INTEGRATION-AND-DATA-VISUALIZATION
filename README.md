# -API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : MOTHKUR AKSHITHA REDDY

*INTERN ID* : CT06DA128

*DOMAIN* : PYTHON PROGRAMMING

*DURATION* : 6 WEEKS

*MENTOR* : NEELA SANTOSH

*DESCRIPTION* :

This credit risk visualization and analysis project is built using Python and focuses on exploring a comprehensive loan dataset to uncover patterns in borrower characteristics, loan performance, and credit risk. The project uses several key Python libraries to achieve this: Pandas for data loading, cleaning, transformation, and statistical analysis; Matplotlib for core plotting capabilities and subplot layout management; and Seaborn, which builds on Matplotlib to create aesthetically pleasing and insightful statistical plots. The dataset, loaded from a local CSV file, contains various attributes related to loan applications, including personal income, loan amount, loan intent, credit history length, employment length, age, and loan status (e.g., defaulted or fully paid).

The goal of the analysis is to visualize important trends that can help in understanding credit risk factors and support financial decision-making. The project begins with data cleaning using Pandas, specifically removing missing values to ensure the quality of insights derived. Binning techniques are applied to continuous variables like age and credit history using pd.cut() to create categorical groupings, which enhances interpretability in heatmaps and grouped visualizations.

The dashboard layout consists of six well-structured subplots. First, a scatter plot visualizes the relationship between a borrower's income and the loan amount, color-coded by loan grade, helping to identify how income levels affect the size and quality of loans. Second, a box plot illustrates the distribution of interest rates across different loan grades, further split by loan status, offering insight into how lenders may adjust interest rates based on risk assessments. Third, a heatmap shows the default rate based on borrower age groups and length of credit history, using a pivot table to compute default ratios. This visual is particularly useful in identifying high-risk demographics.The fourth plot is a bar chart that compares loan intent categories (e.g., education, medical, personal) against loan status, which is valuable for understanding how different loan purposes correlate with repayment behavior. The fifth plot is a histogram that visualizes the percentage of a borrower's income allocated to loan repayment, separated by loan status, which gives clues about borrower affordability and financial stress. Lastly, a violin plot displays interest rate distributions by employment length and loan grade, combining density estimation and categorical data to reveal deeper insights.

This project has real-world applications in banking, FinTech, and risk analytics, where understanding borrower profiles and default risks is essential. It can be used by credit analysts, loan officers, and financial institutions to guide lending strategies, minimize default exposure, and refine credit scoring models. Additionally, the analysis is valuable for data analysts and data scientists looking to showcase their skills in exploratory data analysis (EDA), financial analytics, and visualization. With further enhancements such as predictive modeling (e.g., logistic regression or machine learning classifiers) or deployment as an interactive web app using Streamlit or Dash, this project can evolve into a complete credit risk decision-support system.



