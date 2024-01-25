#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:09:23 2023

@author: anastassiakustenmacher
"""

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
root=r"D:/Akos/UseCase_2_MSG_Alu_FitAG/UseCase_2_MSG_Alu_FitAG/Wall_12_AL_Oel_20220615/"

pattern = r'^L[0-5][0-9]_10-*'
files_dir = [
    f for f in os.listdir(root) if os.path.isdir(os.path.join(root, f)) and re.match(pattern, f)
]
files_dir.sort()

messung = {'Filename':'',
    'MikroGefell1_96khz': [],
               'MikroGefell2_96khz': [],
               'MikroSE81_48khz': [],
               'MikroSE82_48khz': [],
               'PositionX_10Hz': [],
               'PositionY_10Hz': [],
               'PositionZ_10Hz': [],
               'Schweissspannung_10khz': [],
               'Schweisstrom_10khz': []}

#layers=[{}]*len(files_dir)
layers=[{}]*10
count=0

for dirs in files_dir[0:10]:
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
        else:  messung[key] = dirs
        print(file)

    print(dirs)
    #layers[count]=make_change(layers.copy(), messung, count)
    layers[count]=messung.copy()
    count=count+1
    
    
#Plot the outputs for the first n-layers    
for layer in range(len(layers)):
    
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Layer_'+str(layer))
    axs[0, 0].plot(layers[layer]['MikroGefell1_96khz'])
    axs[0, 0].set_title('MikroGefell1_96khz')
    axs[0, 1].plot(layers[layer]['MikroGefell2_96khz'], 'tab:orange')
    axs[0, 1].set_title('MikroGefell2_96khz')
    axs[1, 0].plot(layers[layer]['MikroSE81_48khz'], 'tab:green')
    axs[1, 0].set_title('MikroSE81_48khz')
    axs[1, 1].plot(layers[layer]['MikroSE82_48khz'], 'tab:red')
    axs[1, 1].set_title('MikroSE82_48khz')
    
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('Layer_'+str(layer))
    axs[0, 0].plot(layers[layer]['PositionX_10Hz'])
    axs[0, 0].set_title('PositionX_10Hz')
    axs[0, 1].plot(layers[layer]['PositionZ_10Hz'], 'tab:orange')
    axs[0, 1].set_title('PositionZ_10Hz')
    axs[1, 0].plot(layers[layer]['Schweissspannung_10khz'], 'tab:red')
    axs[1, 0].set_title('Schweissspannung_10khz')
    axs[1, 1].plot(layers[layer]['Schweisstrom_10khz'], 'tab:cyan')
    axs[1, 1].set_title('Schweisstrom_10khz')

plt.show()