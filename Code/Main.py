import numpy as np
import pandas as pd
import mne
from mne.viz import plot_topomap
from fooof import FOOOFGroup
from fooof.bands import Bands
from fooof.analysis import get_band_peak_fg
from fooof.plts.spectra import plot_spectrum
#from mne.time_frequency import psd_welch
import scipy.signal as signal

data = pd.read_csv('Dataset\\Arithmetic_sub_1_trial.csv')
ch_names = ['CZ', 'FZ', 'Fp1', 'F7', 'F3', 'FC1', 'C3', 'FC5', 'FT9', 'T7', 'CP5', 'CP1', 'P3', 'P7', 'PO9','O1', 'PZ', 'OZ', 'O2', 'PO10', 'P8', 'P4', 'CP2', 'CP6', 'T8', 'FT10', 'FC6', 'C4', 'FC2', 'F4', 'F8','Fp2']
ch_types = ['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg']
sfreq = 128

info = mne.create_info(ch_names = ch_names, ch_types=ch_types,sfreq = sfreq)
raw = mne.io.RawArray(data.transpose(), info)
raw.plot()
builtin_montages = mne.channels.get_builtin_montages(descriptions=True)
for montage_name, montage_description in builtin_montages:
    print(f'{montage_name}: {montage_description}')


easycap_montage = mne.channels.make_standard_montage('easycap-M1')
print(easycap_montage)

easycap_montage.plot()  # 2D
fig = easycap_montage.plot(kind='3d', show=False)  # 3D
fig = fig.gca().view_init(azim=70, elev=15)  # set view angle for tutorial



raw.set_montage(easycap_montage)
fig = raw.plot_sensors(show_names=True)


# Select EEG channels from the dataset
#raw = raw.pick_types(meg=False, eeg=False, eog=False, exclude='bads')
print(raw.info)
raw.plot()


#raw.compute_psd(fmax=30).plot()
#raw.plot(duration=25, n_channels=32)
#raw.compute_psd(fmax=50,picks='misc').plot()
#raw.plot(duration=25, n_channels=32)
#raw.plot_psd(fmax=50, picks='eeg',show=True)

raw.set_montage(inst.set_channel_types)
raw.plot_sensors()

raw.compute_psd(fmin = 8., fmax= 12.).plot()
#raw.plot

'''
#raw.compute_psd(fmax=30, picks='misc').plot()
#raw.plot(duration=25, n_channels=32)
#(area_mode='range', tmax=10.0, show=True, average=True)


#times = np.arange(0.05, 0.151, 0.02)
#raw.plot_topomap(times, ch_type='mag')

# Calculate power spectra across the the continuous data
#spectra, freqs = psd_welch(raw, fmin=1, fmax=40, tmin=0, tmax=250,n_overlap=150, n_fft=300)


#(spectra, freqs)= scipy.signal.welch(raw, fs=128)

raw.compute_psd(fmin = 8., fmax= 12.).plot();



raw.compute_psd(fmin = 8., fmax= 12.)
raw.plot


(spectra, freqs)=signal.welch(raw, fs=128, nperseg=1024)

# Initialize a FOOOFGroup object, with desired settings
fg = FOOOFGroup(peak_width_limits=[1, 6], min_peak_height=0.15,
                peak_threshold=2., max_n_peaks=6, verbose=False)

# Define the frequency range to fit
freq_range = [1, 30]
# Fit the power spectrum model across all channels
fg.fit(freqs, spectra, freq_range)
# Check the overall results of the group fits
fg.plot()


# Define frequency bands of interest
bands = Bands({'theta': [3, 7],
               'alpha': [7, 14],
               'beta': [15, 30]})
# Extract alpha peaks
alphas = get_band_peak_fg(fg, bands.alpha)

# Extract the power values from the detected peaks
alpha_pw = alphas[:, 1]
# Plot the topography of alpha power
plot_topomap(alpha_pw, raw.info, cmap=cm.viridis, contours=0);
'''
