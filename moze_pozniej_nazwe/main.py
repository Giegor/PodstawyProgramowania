import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

# print(data.head().to_string())

# print(data.isnull().sum())

corr = data.loc[:, data.columns != 'diagnosis'].corr()

# print(corr.to_string())

'''sns.heatmap(corr, cmap='coolwarm')
plt.show()'''

'''data.drop('diagnosis', axis=1).hist(bins=30,figsize=(15,20))
plt.tight_layout()
plt.show()'''

data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})

# print(data.to_string())

data = data.drop(['id', 'Unnamed: 32'], axis=1, errors='ignore')

# print(data.to_string())

X = data.drop('diagnosis', axis=1).values
y = data['diagnosis'].values