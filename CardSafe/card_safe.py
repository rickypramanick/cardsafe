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

# Exploratory Data Analysis
print("Number of Fraudulent Transactions: " + str(data[data['Class'] == 1].shape[0]))
print("Number of Legitimate Transactions: " + str(data[data['Class'] == 0].shape[0]))
print("Proportion of Fraudulent Transactions: " + str(data[data['Class'] == 1].shape[0]/data.shape[0]))

data_pi = data.copy()
data_pi[" "] =np.where(data_pi['Class'] == 1, "Fraud", "Genuine")

# %matplotlib inline
data_pi[" "].value_counts().plot(kind='pie')

# data.describe()
