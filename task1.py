import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#loading a dataset
df = pd.read_csv("C:/Users/Akshitha/Downloads/cr_loan2.csv")
# Seting a dark theme for the plots
plt.style.use('dark_background')
# removing missing values
df.dropna(inplace=True)  
# matplotlib figure size 
plt.figure(figsize=(12, 8))

#1.Scatter Plot: Income vs Loan Amount
plt.subplot(2, 3, 1)
sns.scatterplot(
    data=df,
    x='person_income',
    y='loan_amnt',
    hue='loan_grade',
    alpha=0.7
)
plt.title('Income vs Loan Amount by Grade', fontsize=13, fontweight='bold')
plt.xlabel('Income ($)')
plt.ylabel('Loan Amount ($)')

#2.Boxplot: Loan Interest Rate by Grade 
plt.subplot(2, 3, 2)
sns.boxplot(
    data=df,
    x='loan_grade',
    y='loan_int_rate',
    hue='loan_status'
)
plt.title('Loan Interest Rate by Grade and Status', fontsize=13, fontweight='bold')
plt.xlabel('Loan Grade')
plt.ylabel('Interest Rate (%)')

#3.Heatmap: Default Rate by Age and Credit History Length
# Bin age and credit history
df['age_bin'] = pd.cut(df['person_age'], bins=[18, 25, 35, 45, 55, 65, 100])
df['cred_hist_bin'] = pd.cut(df['cb_person_cred_hist_length'], bins=[0, 5, 10, 15, 20, 30, 50])
#Creating Pivot for heatmap
heatmap_data = df.pivot_table(
    index='age_bin',
    columns='cred_hist_bin',
    values='cb_person_default_on_file',
    aggfunc=lambda x: (x == 'Y').mean()  # assuming 'Y' = defaulted
)

plt.subplot(2, 3, 3)
sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Default Rate by Age and Credit History Length', fontsize=13, fontweight='bold')
plt.xlabel('Credit History Length (years)')
plt.ylabel('Age Group')

#4.Bar Plot: Loan Intent vs Loan Status
plt.subplot(2, 3, 4)
sns.countplot(
    data=df,
    x='loan_intent',
    hue='loan_status'
)
plt.title('Loan Intent vs Loan Status', fontsize=13, fontweight='bold')
plt.xlabel('Loan Intent')
plt.ylabel('Number of Loans')
plt.xticks(rotation=45)

#5.Histogram: Loan Percent Income by Loan Status 
plt.subplot(2, 3, 5)
sns.histplot(
    data=df,
    x='loan_percent_income',
    hue='loan_status',
    kde=True,
    element='step'
)
plt.title('Loan Percent of Income by Loan Status', fontsize=13, fontweight='bold')
plt.xlabel('Loan % of Income')

#6.Violin Plot: Interest Rate by Employment Length and Grade
plt.subplot(2, 3, 6)
sns.violinplot(
    data=df,
    x='person_emp_length',
    y='loan_int_rate',
    hue='loan_grade',
    split=True,
    palette='muted'
)
plt.title('Interest Rate by Employment Length and Grade', fontsize=13, fontweight='bold')
plt.xlabel('Employment Length (Years)')
plt.ylabel('Interest Rate (%)')
plt.xticks(rotation=45)

# Seting  main title for the entire plot
plt.suptitle('Credit Analysis', fontsize=20, fontweight='bold', color='white')

# Adjust layout
plt.tight_layout()
# Adjust to make space for the main title
plt.subplots_adjust(top=0.9)  

# Showing all plots
plt.show() 
