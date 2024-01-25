import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'pore_data_fit_eng.csv'
df = pd.read_csv(file_path, delimiter=';')

# Select a specific wall
selected_wall = 'fit12'
wall_df = df[df['wand_ids'] == selected_wall]

# Scatter plot for pore distribution along the layer
# plt.figure(figsize=(15, 8))
# sns.scatterplot(x='postion[mm]', y='diameters[mm]', hue='layer', data=wall_df, palette='viridis', s=50)
# plt.title(f'Pore Distribution along {selected_wall} Layers')
# plt.xlabel('Position along Layer [mm]')
# plt.ylabel('Pore Diameter [mm]')
# plt.legend(title='Layer')
# plt.show()


# Heatmap for pore distribution along the layer
plt.figure(figsize=(15, 8))
heatmap_data = wall_df.pivot_table(index='layer', columns='postion[mm]', values='diameters[mm]', aggfunc='mean')
sns.heatmap(heatmap_data, cmap='viridis', cbar_kws={'label': 'Pore Diameter [mm]'})
plt.title(f'Pore Distribution along {selected_wall} Layers (Heatmap)')
plt.xlabel('Position along Layer [mm]')
plt.ylabel('Layer')
plt.show()
