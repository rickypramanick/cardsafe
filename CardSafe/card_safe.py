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
print("Number of Legitimate Transactions: " + str(data[data['Class'] == 0].shape[0]))
print("Proportion of Fraudulent Transactions: " + str(data[data['Class'] == 1].shape[0]/data.shape[0]))

data_pi = data.copy()
data_pi[" "] = np.where(data_pi['Class'] == 1, "Fraud", "Legitimate")

# %matplotlib inline

# Pie Chart depicting proportion of Fradulent to Legitimate Transactions
# data_pi[" "].value_counts().plot(kind='pie')

# data.describe()

f, axes = plt.subplots(1, 2, figsize=(18, 4), sharex='all')

amount_val = data['Amount'].values
time_val = data['Time'].values

sns.displot(
    amount_val,
    color="m",
    kde_kws={"shade": True},
    ax=axes[0]).set_title("Distribution of Transaction Amounts")

sns.displot(
    time_val,
    color="m",
    kde_kws={"shade": True},
    ax=axes[1]).set_title("Distribution of Transaction Times")

plt.show()
