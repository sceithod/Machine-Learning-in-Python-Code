from pywt import wavedec
import matplotlib.pyplot as plot
from numpy.fft import fft, fftfreq
from scipy import signal
import pandas as pd
import numpy as np


data = pd.read_csv('Dataset\\Arithmetic_sub_1_trial.csv')

X = fft(data)

coeffs = wavedec([1,2,3,4,5,6,7,8], 'db5', level=2)

cA2, cD2, cD1 = coeffs




name = 'db5'; 
waveletFunction='db5';
# Compute the corresponding scaling filter.
coeffs = wavedec(data,'db5',5);
cA2,cD2,cD1,cD3,cD4,cD5 = coeffs
#cA2,cD2,cD1,cD3,cD4,cD5 = coeffs;


'''

[C,L] = wavedec(X,5,'db8');
'''
cD1 = detcoef(C,L,1);                   #NOISY
cD2 = detcoef(C,L,2);                  #Gamma
cD3 = detcoef(C,L,3);                   #Beta
cD4 = detcoef(C,L,4);                   #Alpha
cD5 = detcoef(C,L,5);                   #Delta
cA5 = appcoef(C,L,waveletFunction,5);   #Theta


figure,title('Feature Extraction');subplot(6,1,1)
plot(cA2)
title(' Theta')
subplot(6,1,2)
plot(cD5)
title('  Delta')
subplot(6,1,3)
plot(cD4)
title('  Alpha')
subplot(6,1,4)
plot(cD3)
title('  Beta')
subplot(6,1,5)
plot(cD2)
title('  Gamma')
