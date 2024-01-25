import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the MFCC features and labels from the file
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

# Define the autoencoder model
input_dim = mfcc_features.shape[1]
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
autoencoder.fit(mfcc_features, mfcc_features, epochs=50, batch_size=32, shuffle=True)

# Extract encoder model for feature representation
encoder = models.Model(autoencoder.input, autoencoder.layers[3].output)

# Obtain encoded features for visualization
encoded_features = encoder.predict(mfcc_features)
print(encoded_features)
# Create a 3D scatter plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot points with different colors based on the true labels
ax.scatter(encoded_features[labels == 0, 0], encoded_features[labels == 0, 1], encoded_features[labels == 0, 2], label='io')
ax.scatter(encoded_features[labels == 1, 0], encoded_features[labels == 1, 1], encoded_features[labels == 1, 2], label='gas 50')
ax.scatter(encoded_features[labels == 2, 0], encoded_features[labels == 2, 1], encoded_features[labels == 2, 2], label='gas 80')
ax.scatter(encoded_features[labels == 3, 0], encoded_features[labels == 3, 1], encoded_features[labels == 3, 2], label='gas 70')
ax.scatter(encoded_features[labels == 4, 0], encoded_features[labels == 4, 1], encoded_features[labels == 4, 2], label='gas 90')
ax.scatter(encoded_features[labels == 5, 0], encoded_features[labels == 5, 1], encoded_features[labels == 5, 2], label='Oel')
ax.set_xlabel('Feature 1')
ax.set_ylabel('Feature 2')
ax.set_zlabel('Feature 3')
ax.set_title('Autoencoder Encoded Features Visualization')

plt.legend()
plt.show()
