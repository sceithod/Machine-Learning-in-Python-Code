import numpy as np
import pandas as pd
from numpy.fft import fft, fftfreq
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
from mne.time_frequency.tfr import morlet
from mne.viz import plot_filter, plot_ideal_filter

import mne

sfreq=128


dataset = open("Info.txt", "r")
s=dataset.read()
#data = pd.read_csv('Dataset\\Arithmetic_sub_1_trial.csv')
data1 = pd.read_csv("Dataset\\"+s)
X = fft(data1)

t = np.arange(len(data1)) / sfreq

plt.plot(t,X);
plt.title("FIR Filter using Preprocessing");
plt.show()
