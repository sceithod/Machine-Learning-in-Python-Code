import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from math import pi
import pandas as pd

sampling_freq = 128

duration = 25.0

t = np.arange(0.0, duration, 1/sampling_freq)

data = pd.read_csv('Dataset\\Arithmetic_sub_1_trial.csv')


#y = y_clean + 0.1 * np.sin(2*pi*60*t) + 0.2 * np.random.normal(size=len(t))
plt.figure(figsize=(18,4))
plt.plot(t, data)
#plt.plot(t, y_clean)
plt.xlabel('time (s)')
plt.ylabel('signal')
plt.show()

