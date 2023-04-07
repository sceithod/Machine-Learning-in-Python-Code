import os
import numpy as np
import mne

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mne.datasets import sample

EEGData = pd.read_csv("Dataset\\Arithmetic_sub_1_trial.csv");
#EEGData = pd.read_csv("A1.csv");
print(EEGData.head())


print(EEGData.shape)

plt.figure(figsize=(16, 10))
plt.plot(range(len(EEGData)), EEGData)
#plt.plot( EEGData)
plt.title("EEG Data")
plt.show()

lowcut = 0.3
highcut = 25
order = 10
nyquistFreq = 128

from scipy.signal import butter, sosfilt

low  = lowcut / nyquistFreq
high = highcut / nyquistFreq

sos  = butter(order, [low, high], btype='bandpass', output='sos')

# data is a numpy array containing the samples of one EEG channel
filtered = sosfilt(sos, EEGData)


plt.figure(figsize=(16, 10))
plt.plot(filtered)
plt.title("EEG Data")
plt.show()
