"""CardSafe - Fraudulent Credit Card Transaction Detection """
import inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

data = pd.read_csv("creditcard.csv")

# Exploratory Data Analysis - Data Visualisation
print("Number of Fraudulent Transactions: " + str(data[data['Class'] == 1].shape[0]))
num_fraud_tran = data[data['Class'] == 1].shape[0]
print("Number of Legitimate Transactions: " + str(data[data['Class'] == 0].shape[0]))
num_legit_tran = data[data['Class'] == 0].shape[0]
print("Proportion of Fraudulent Transactions: " + str(data[data['Class'] == 1].shape[0]/data.shape[0]))
prop_fraud_tran = data[data['Class'] == 1].shape[0]/data.shape[0]

data_pi = data.copy()
data_pi[" "] = np.where(data_pi['Class'] == 1, "Fraud", "Legitimate")

# %matplotlib inline

# Pie Chart depicting proportion of Fradulent to Legitimate Transactions
data_pi[" "].value_counts().plot(kind='pie')

data.describe()

f, axes = plt.subplots(1, 2, figsize=(18, 4), sharex='all')

amount_val = data['Amount'].values
time_val = data['Time'].values

sns.displot(
    amount_val,
    color="m",
    kde_kws={"shade": True},
    ax=axes[0]).set_titles("Distribution of Transaction Amounts")

sns.displot(
    time_val,
    color="m",
    kde_kws={"shade": True},
    ax=axes[1]).set_titles("Distribution of Transaction Times")

plt.show()

print("Average Transaction Amount in a Fradulent Transaction: " + str(data[data['Class'] == 1]['Amount'].mean()))
avg_fraud_tran_amt = data[data['Class'] == 1]['Amount'].mean()
print("Average Transaction Amount in a Legitimate Transaction: " + str(data[data['Class'] == 0]['Amount'].mean()))
avg_legit_tran_amt = data[data['Class'] == 0]['Amount'].mean()


# Reorder the columns Amount, Time then the rest
data_plot = data.copy()
amount = data_plot['Amount']
data_plot.drop(labels=['Amount'], axis=1, inplace = True)
data_plot.insert(0, 'Amount', amount)

# Plot the distributions of the features
columns = data_plot.iloc[:,0:30].columns
plt.figure(figsize=(12,30*4))
grids = gridspec.GridSpec(30, 1)
for grid, index in enumerate(data_plot[columns]):
    ax = plt.subplot(grids[grid])
    sns.distplot(data_plot[index][data_plot.Class == 1], hist=False, kde_kws={"shade": True}, bins=50)
    sns.distplot(data_plot[index][data_plot.Class == 0], hist=False, kde_kws={"shade": True}, bins=50)
    ax.set_xlabel("")
    ax.set_title("Distribution of Column: " + str(index))
plt.show()
