import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'pore_data_fit_eng.csv'
df = pd.read_csv(file_path, delimiter=';')

# Basic overview of the dataset
print(df.head())

# Summary statistics
print(df.describe())

# Pore distribution by class
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.boxplot(x='class', y='diameters[mm]', data=df)
plt.title('Pore Distribution by Class')
plt.show()

# Pore distribution by layer
plt.figure(figsize=(12, 6))
sns.boxplot(x='layer', y='diameters[mm]', data=df)
plt.title('Pore Distribution by Layer')
plt.show()

# Pore distribution by wall
plt.figure(figsize=(12, 6))
sns.boxplot(x='wand_ids', y='diameters[mm]', data=df)
plt.title('Pore Distribution by Wall')
plt.show()

# Correlation between variables
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix')
plt.show()
