# AKOS - Acoustic Inspection of Weld Seams

## Dataset
Dataset used: [Download Link](https://nx21454.your-storageshare.de/s/C5SF9GKQpzHRXfT/authenticate/showShare)
Reference: [AKoS-project.de](https://www.akos-projekt.de/index.php/beitraege)

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
- Utilize deep learning models (e.g., CNNs or RNNs) to process signal data and extract features.
- Train the model on the dataset, considering welding variations for each wall.
- Use MFCC features as input for recognizing pores.
- Utilize wall 17 data as ideal for training, given its least porous nature.

## Evaluation
- Evaluate the trained model's performance on a separate test set to ensure generalization.
- Metrics: Accuracy, precision, recall, and F1 score.

## Documentation and Reporting
- Document the entire process, including data preprocessing, model architecture, training parameters, and evaluation results.
- Provide clear insights into the identification of pores using the chosen approach.
