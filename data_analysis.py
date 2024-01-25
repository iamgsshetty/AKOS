import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'pore_data_fit_eng.csv'
df = pd.read_csv(file_path, delimiter=';')

# Pore distribution histograms
plt.figure(figsize=(15, 8))
sns.histplot(df, x='diameters[mm]', bins=30, hue='class', multiple="stack", kde=True)
plt.title('Pore Diameter Distribution by Class')
plt.xlabel('Pore Diameter [mm]')
plt.ylabel('Frequency')
plt.show()

# Cumulative distribution plots
plt.figure(figsize=(15, 8))
for class_label in df['class'].unique():
    class_data = df[df['class'] == class_label]['diameters[mm]']
    sns.ecdfplot(class_data, label=class_label)
plt.title('Cumulative Distribution of Pore Diameter by Class')
plt.xlabel('Pore Diameter [mm]')
plt.ylabel('Cumulative Probability')
plt.legend()
plt.show()

# Violin plots for pore distribution by class
plt.figure(figsize=(15, 8))
sns.violinplot(x='class', y='diameters[mm]', data=df, inner='quartile')
plt.title('Pore Diameter Distribution by Class (Violin Plot)')
plt.xlabel('Class')
plt.ylabel('Pore Diameter [mm]')
plt.show()

# Pore distribution by layer (for a specific wall)
selected_wall = 'fit12'
wall_df = df[df['wand_ids'] == selected_wall]

plt.figure(figsize=(15, 8))
sns.histplot(wall_df, x='diameters[mm]', bins=30, hue='layer', multiple="stack", kde=True)
plt.title(f'Pore Diameter Distribution in {selected_wall} by Layer')
plt.xlabel('Pore Diameter [mm]')
plt.ylabel('Frequency')
plt.show()
