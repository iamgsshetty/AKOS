import librosa
import numpy as np

def read_wall_data_from_file(filename):
    wall_name = []
    wall_data = []
    with open(filename, 'r') as file:
        for line in file:
            name, data_str = line.strip().split(': ')
            data_cube = [list(map(float, row.split(','))) for row in data_str.split(';')]
            wall_name.append(name)
            wall_data.append(data_cube)
    return wall_name, wall_data


def extract_mfcc_features(signal_data, num_mfcc=6):
    mfcc_features = []
    for signal in signal_data:
        mfcc = librosa.feature.mfcc(y=np.array(signal).flatten(), sr=44100, n_mfcc=num_mfcc)
        mfcc_features.append(mfcc.flatten())
    return mfcc_features

def store_mfcc_features_to_file(wall_name, mfcc_features, filename):
    with open(filename, 'w') as file:
        for name, features in zip(wall_name, mfcc_features):
            features_str = ','.join(map(str, features))
            file.write(f"{name}: {features_str}\n")


loaded_wall_name, loaded_wall_data = read_wall_data_from_file('wall_all.txt') # wall_all.txt is the text file containg the signal dataset

# Extract MFCC features
mfcc_features = extract_mfcc_features(loaded_wall_data)

# Store MFCC features to a new file
store_mfcc_features_to_file(loaded_wall_name, mfcc_features, 'mfcc_features_file_wall_all.txt')