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

data = pd.read_csv('Dataset\\Arithmetic_sub_1_trial.csv')

X = fft(data)

t = np.arange(len(data)) / sfreq

plt.plot(t,X);
plt.title("FIR Filter using Preprocessing");
plt.show()

