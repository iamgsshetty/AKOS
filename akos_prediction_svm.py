import librosa
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Function for feature extraction
def extract_features(audio_file_path):
    y, sr = librosa.load(audio_file_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    flat_features = np.ravel(mfccs)
    return flat_features

def load_data_from_file(filename, max_length=None):
    mfcc_features = []
    labels = []
    with open(filename, 'r') as file:
        for line in file:
            name, features_str = line.strip().split(': ')
            features = np.array(list(map(float, features_str.split(','))))
            if '_io-' in name:
                label = 0
            elif 'gas80' in name:
                label = 2
            elif 'gas70' in name:
                label = 3
            elif 'gas90' in name:
                label = 4
            elif 'oel' in name:
                label = 5
            else:
                label = 1
            # label = 1 if 'gas-50' in name else 0
            labels.append(label)
            mfcc_features.append(features)

    # Pad sequences to a fixed length (you can set max_length as needed)
    mfcc_features_padded = pad_sequences(mfcc_features, dtype='float32', padding='post', truncating='post', maxlen=max_length)

    return mfcc_features_padded, np.array(labels)

# Load MFCC features and labels, and pad sequences to a fixed length
max_length = 11680  # Set max_length based on your requirement
mfcc_features, labels = load_data_from_file('mfcc_features_file_wall_all.txt', max_length)

# Normalize the MFCC features
mfcc_features = (mfcc_features - np.mean(mfcc_features, axis=0)) / np.std(mfcc_features, axis=0)

X = mfcc_features
y = labels

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# print(y_test)

# Train a Support Vector Machine (SVM) classifier
kernels = ['linear', 'rbf']
for kernel in kernels:
    clf = SVC(kernel=kernel)
    clf.fit(X_train, y_train)

    # for j,i in enumerate(mfcc_features):
    #     prediction_third_layer = clf.predict(i.reshape(1, -1))
    #     print(f"Prediction for the third layer: {prediction_third_layer[0]}, label = {labels[j]}")

    # Evaluate the model on the test set
    y_pred = clf.predict(mfcc_features)
    accuracy = accuracy_score(labels, y_pred)
    # cm = confusion_matrix(y_test, y_pred)
    print(f"Kernel: {kernel}")
    # print(f"Prediction for the third layer: {prediction_third_layer[0]}")
    print(f"Model accuracy on the test set: {accuracy}")
    # print(f"Confusion Matrix:\n{cm}")

    # Plot the confusion matrix
    # plt.figure(figsize=(4, 3))
    # sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
    #             xticklabels=labels, yticklabels=labels)
    # plt.title(f'Confusion Matrix ({kernel} Kernel)')
    # plt.xlabel('Predicted')
    # plt.ylabel('True')
    # plt.show()

    # Classification report
    print(f"Classification Report:\n{classification_report(labels, y_pred)}")
    print("\n" + "="*40 + "\n")
