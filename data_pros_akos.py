from matplotlib import pyplot as plt
import numpy as np
from scipy import signal
import os
import re

import scipy.io
from scipy import signal
import pickle
import pandas as pd

from scipy.fftpack import fft, ifft
#import visualisation as myvis
import importlib
from bitstring import ConstBitStream
#importlib.reload(myvis)

def read_i32(filepath):
    file=open(filepath,'rb')
    raw=ConstBitStream(file)
    count=raw.len // 32
    floararray = [ ]
    for i in range(count):
        floararray.append(raw.readlist('floatle:32'))
    return floararray

#filepath = os.path.join(root, filename)
#directory = os.getcwd()
# Aufgabe: gehe über alle Z und checke die Höher
#root=r"/Users/anastassiakustenmacher/Documents/MeasX/Akos/all_data/UseCase_2/UseCase_2_MSG_Alu_FitAG/Wall_12_AL_Oel_20220615/L02_10-07-13_io-pass"
# root=r"/Users/anastassiakustenmacher/Documents/MeasX/Akos/all_data/UseCase_2/UseCase_2_MSG_Alu_FitAG/Wall_12_AL_Oel_20220615/"
root=r"D:/Akos/UseCase_2_MSG_Alu_FitAG/UseCase_2_MSG_Alu_FitAG/wall_test/"

pattern = r'^L[0-5][0-9]_*'
files_dir = [
    f for f in os.listdir(root) if os.path.isdir(os.path.join(root, f)) and re.match(pattern, f)
]
files_dir.sort()

messung = {'Filename':'',
    'MikroGefell1_96khz': []}

layer_number = len(files_dir)
# layers=[{}]*len(files_dir)
layers=[{}]*200
count=0
wall_data = []
wall_name = [] 
print("number of layers = ",layer_number)
for dirs in files_dir[0:200]:
    print(dirs)
    # read all files

    dir_path = os.path.join(root, dirs)
    files_file = [
    f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))
    ]
    for key in messung:
        messung.fromkeys(messung, [])
        file=[x for x in files_file if x.startswith(key)]
        if len(file)!=0:
            filepath = os.path.join(dir_path, file[0])
            messung[key]=read_i32(filepath)
            wall_data.append(messung[key])
        else:  
            messung[key] = dirs
            wall_name.append(messung[key])
        # print(file)

    # print(dirs)
    #layers[count]=make_change(layers.copy(), messung, count)
    layers[count]=messung.copy()
    print(count)
    count=count+1
# for w in wall_data:
#     print("wall data = \n",w)
    
def store_wall_data_to_file(wall_name, wall_data, filename):
    with open(filename, 'w') as file:
        for name, data_cube in zip(wall_name, wall_data):
            data_str = ';'.join(','.join(map(str, row)) for row in data_cube)
            file.write(f"{name}: {data_str}\n")

store_wall_data_to_file(wall_name, wall_data, 'wall_all.txt')
