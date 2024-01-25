# AKOS - Acoustic Inspection of Weld Seams

## Dataset
- Dataset created under AKoS project
- Reference: [AKoS-project.de](https://www.akos-projekt.de/index.php/beitraege)
- Dataset used: [Download Link](https://nx21454.your-storageshare.de/s/C5SF9GKQpzHRXfT/authenticate/showShare)

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

## Procedure
### Python Modules Used:
#### 1. Librosa
- Librosa is a Python package for music and audio analysis. It provides tools for feature extraction, time-series analysis, and more.

#### 2. NumPy
- NumPy is a fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with mathematical functions.

#### 3. Matplotlib
- Matplotlib is a versatile plotting library for creating static, animated, and interactive visualizations in Python.

#### 4. Scipy
- Scipy is an open-source library for mathematics, science, and engineering. It provides additional functionality on top of NumPy.

#### 5. OS and Regular Expression
- OS and re modules are used for operating system-related tasks and regular expression operations, respectively.

#### 6. Scipy.io
- Scipy.io provides tools for working with various file formats, including audio files.

#### 7. Pickle
- Pickle is used for serializing and deserializing Python objects, facilitating data storage and retrieval.

### 8. Pandas
- Pandas is a powerful data manipulation and analysis library, commonly used for working with structured data.

#### 9. Scikit-Learn
- Scikit-Learn is a machine learning library that provides simple and efficient tools for data mining and data analysis.

#### 10. TensorFlow
- TensorFlow is an open-source machine learning framework for high-performance numerical computations.

#### 11. Matplotlib 3D Plotting
- Matplotlib's 3D plotting toolkit for creating 3D visualizations.

#### 12. TensorFlow Keras
- TensorFlow Keras is a high-level neural networks API, part of TensorFlow, for building and training deep learning models.

#### 13. Seaborn
- Seaborn is a statistical data visualization library based on Matplotlib, providing a high-level interface for drawing informative graphics.

### Steps to execute the codes:
- **Step 1:** Run data_pros_akos to convert i32 file to .txt file for further processing.
- **Step 2:** Run akos_mfcc_dataset to extract mfcc features and store it in .txt file.
- **Step 3:** Run akos_plot_encoder to run autoencoder on the mfcc dataset created in step 2 to reduce dimension to 3D and plot it.
- **Step 4:** Run akos_visual_seperate_pores.py to further reduce the encoded 3D data to 2D for better visualization using kernel principal compnent analysis.
- **Step 5:** Run akos_prediction_svm.py to train SVM model on the dataset (Note: only data of 200 layers used for training)
- i32 dataset link provided in the begining

### Results:
### Output of step 3 on wall 16 which has layer welded with 50% gas concentration
![3D Visualization of two classes](https://github.com/iamgsshetty/AKOS/blob/main/Results/autoencoder_mfcc_wall_16.png)
### Output of step 4 on wall 16 which has layer welded with 50% gas concentration
![2D Visualization of two classes](https://github.com/iamgsshetty/AKOS/blob/main/Results/kpca_auto_zoom_wall_16.png)
### Output of step 3 on layers taken from each class (Oil, gas 50, gas 80, gas 70, gas 90)
![3D Visualization of many classes](https://github.com/iamgsshetty/AKOS/blob/main/Results/Figure_1_encoded%20feature.png)
### Output of step 5
![Results of SVM model](https://github.com/iamgsshetty/AKOS/blob/main/Results/Screenshot%202024-01-25%20114000.png)


## Visualize pore distribution
- **Modules Required:**
  - **Pandas:** it is a powerful data manipulation and analysis library. It provides data structures like DataFrame for efficient data handling and analysis.
  - **Matpltlib:** it is a plotting library that helps create static, animated, and interactive visualizations in Python.
  - **Seaborn:** it is a statistical data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
- Run code data_analysis.py to get plots:
  - Pore distribution histograms
  - Cumulative distribution plots
  - Violin plots for pore distribution by class
  - Pore distribution by layer (for a specific wall)
- Run code data_analysis_basic.py to get plots:
  - Pore distribution by class
  - Pore distribution by layer
  - Pore distribution by wall
  - Correlation between variables
- Run code pore_distribution.py to get plots:
  - Scatter plot for pore distribution along the layer
  - Heatmap for pore distribution along the layer  
- Run all of these codes on dataset pores_data_fit_eng

### Results:
![]()
![]()
![]()
![]()
![]()
![]()
![]()

