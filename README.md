# AKOS - Acoustic Inspection of Weld Seams

## Dataset
- Dataset used: [Download Link](https://nx21454.your-storageshare.de/s/C5SF9GKQpzHRXfT/authenticate/showShare)
- Reference: [AKoS-project.de](https://www.akos-projekt.de/index.php/beitraege)

### Dataset Structure
- Organized with folders representing each wall (12 to 23).
- Inside each wall folder, sub-folders for each layer of welding, considering only folders with "pass" written at the end.

### Welding Variations
- **Wall 12 and 18:** Oil added every third layer.
- **Wall 13 and 19:** Gas concentration at 90% during every third layer.
- **Wall 15 and 20:** Gas concentration at 80% during every third layer.
- **Wall 15 and 21:** Gas concentration at 70% during every third layer.
- **Wall 16 and 22:** Gas concentration at 50% during every third layer.
- **Wall 17:** Normal welding with no oil and 100% gas concentration. Ideal wall data with the least pores.

## Signal Data Collection
- Collected using Microtech Gefell and SE81 microphones.
- Data is in I32 format.

## Problem Statement
- Analyze signal data to identify pores formed during welding.
- Focus on using Mel-Frequency Cepstral Coefficients (MFCC) features for pore recognition.
- Explore deep learning techniques for analysis.

## Deep Learning Approach
- Utilized autoencoder to reduce mfcc dataset dimension to 3D 
- Train the model on the dataset, considering welding variations for each wall.
- Use MFCC features dataset as input.

## Evaluation
- Evaluate the trained model's performance on a separate test set to ensure generalization.
- Metrics: Accuracy, precision, recall, and F1 score.

## Procedure to run the code.
- **Step 1:** Run data_pros_akos to convert i32 file to .txt file for further processing.
- **Step 2:** Run akos_mfcc_dataset to extract mfcc features and store it in .txt file.
- **Step 3:** Run akos_plot_encoder to run autoencoder on the mfcc dataset created in step 2 to reduce dimension to 3D and plot it.
- **Step 4:** Run akos_visual_seperate_pores.py to further reduce the encoded 3D data to 2D for better visualization using kernel principal compnent analysis.
- i32 dataset link provided in the begining
## Visualize pore distribution
- Run code data_analysis.py to get plots
  - Pore distribution histograms, Cumulative distribution plots, Violin plots for pore distribution by class, Pore distribution by layer (for a specific wall)
- Run code data_analysis_basic.py to get plot Pore distribution by class, Pore distribution by layer, Pore distribution by wall, Correlation between variables  
