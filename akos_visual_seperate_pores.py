import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import KernelPCA
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the MFCC features and labels from the file
def load_data_from_file(filename, max_length=None):
    mfcc_features = []
    labels = []
    with open(filename, 'r') as file:
        for line in file:
            name, features_str = line.strip().split(': ')
            features = np.array(list(map(float, features_str.split(','))))
            # print(name)
            if '_io-' in name:
                label = 0
            elif 'gas80' in name:
                label = 0
            elif 'gas70' in name:
                label = 3
            elif 'gas90' in name:
                label = 0
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

# Define the autoencoder model
input_dim = mfcc_features.shape[1]  # Adjust as needed based on the padded sequence length
encoding_dim = 3  # Adjust as needed

autoencoder = models.Sequential([
    layers.InputLayer(input_shape=(input_dim,)),
    layers.Dense(256, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(encoding_dim, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(128, activation='relu'),
    layers.Dense(256, activation='relu'),
    layers.Dense(input_dim, activation='linear')
])

autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Train the autoencoder
autoencoder.fit(mfcc_features, mfcc_features, epochs=100, batch_size=32, shuffle=True)

# Extract encoder model for feature representation
encoder = models.Model(autoencoder.input, autoencoder.layers[3].output)

# Obtain encoded features for visualization
encoded_features = encoder.predict(mfcc_features)
print(encoded_features.shape)
# Apply Gaussian KPCA
kpca = KernelPCA(n_components=2, kernel='rbf', gamma=0.1)
kpca_result = kpca.fit_transform(encoded_features)
print(kpca_result.shape)
# Visualize in 2D
plt.figure(figsize=(8, 6))
plt.scatter(kpca_result[labels == 0, 0], kpca_result[labels == 0, 1], label='io')
plt.scatter(kpca_result[labels == 1, 0], kpca_result[labels == 1, 1], label='gas 50')
plt.scatter(kpca_result[labels == 2, 0], kpca_result[labels == 2, 1], label='gas 80')
plt.scatter(kpca_result[labels == 3, 0], kpca_result[labels == 3, 1], label='gas 70')
plt.scatter(kpca_result[labels == 4, 0], kpca_result[labels == 4, 1], label='gas 90')
plt.scatter(kpca_result[labels == 5, 0], kpca_result[labels == 5, 1], label='Oel')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('KPCA Visualization of Encoded Features')
plt.legend()
plt.show()
