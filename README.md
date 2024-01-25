# AKOS
AKOS - Acoustic inspection of weld seams on safety-critical components as part of quality assurance.
Dataset used - https://nx21454.your-storageshare.de/s/C5SF9GKQpzHRXfT/authenticate/showShare
Dataset Structure:

Organize your dataset with folders representing each wall (12 to 23).
Inside each wall folder, have sub-folders for each layer of welding, only considering folders with "pass" written at the end.
Welding Variations:

Understand the specific variations introduced in the welding process for each wall:
Wall 12 and 18: Oil added every third layer.
Wall 13 and 19: Gas concentration at 90% during every third layer.
Wall 15 and 20: Gas concentration at 80% during every third layer.
Wall 15 and 21: Gas concentration at 70% during every third layer.
Wall 16 and 22: Gas concentration at 50% during every third layer.
Wall 17: Normal welding with no oil and 100% gas concentration. Consider this as the ideal wall data with the least pores.
Signal Data Collection:

The signal data is collected using two types of microphones - Microtech Gefell and SE81.
The data is in I32 format.
Problem Statement:

The primary goal is to analyze the signal data to identify if pores are formed during welding.
The focus is on using Mel-Frequency Cepstral Coefficients (MFCC) features for pore recognition.
Deep learning techniques can be explored for this analysis.
Deep Learning Approach:

Utilize deep learning models, such as convolutional neural networks (CNNs) or recurrent neural networks (RNNs), to process the signal data and extract features.
Train the model on the dataset, considering the variations in welding conditions for each wall.
Use the MFCC features as input to the deep learning model for recognizing pores.
Utilize wall 17 data as the ideal wall data for training, as it has the least pores. This will help the model learn to distinguish between pore and non-pore instances.
Evaluation:

Evaluate the trained model's performance on a separate test set to ensure its ability to generalize to new data.
Metrics such as accuracy, precision, recall, and F1 score can be used for evaluation.
Documentation and Reporting:

Document the entire process, including data preprocessing, model architecture, training parameters, and evaluation results.
Provide clear insights into whether pores can be identified using the chosen approach.
