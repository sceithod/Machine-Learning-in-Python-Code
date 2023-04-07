import numpy as np
import mne
import pandas as pd
import matplotlib.pyplot as plt
from mne.stats import bootstrap_confidence_interval
from mne.baseline import rescale
import configparser

ch_names = ['Cz', 'FZ', 'Fp1', 'F7', 'F3', 'FC1', 'C3', 'FC5', 'FT9', 'T7', 'CP5', 'CP1', 'P3', 'P7', 'PO9','O1', 'PZ', 'OZ', 'O2', 'PO10', 'P8', 'P4', 'CP2', 'CP6', 'T8', 'FT10', 'FC6', 'C4', 'FC2', 'F4', 'F8','Fp2']
ch_types = ['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg']
sfreq = 128
df_subject_channels=pd.read_csv('Dataset\\Arithmetic_sub_1_trial.csv',
                              sep=',',
                              decimal=".")
print('size of channel data', df_subject_channels.shape)





      #channels labels 
#ch_labels=list(df_subject_channels.labels)
internal_montage = mne.channels.make_standard_montage('GSN-HydroCel-129')
s_freq=250
#create info for object
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
raw= mne.io.RawArray(df_subject_channels.transpose(), info)


filter_params = mne.filter.create_filter(raw.get_data(), raw.info['sfreq'],
                                         l_freq=0.2, h_freq=None)
mne.viz.plot_filter(filter_params, raw.info['sfreq'], flim=(0.01, 5))


reject_criteria = dict(mag=4000e-15,     # 4000 fT
                       grad=4000e-13,    # 4000 fT/cm
                       eeg=150e-6,       # 150 µV
                       eog=250e-6)       # 250 µV


epochs = mne.Epochs(raw,  tmin=-0.2, tmax=0.5,
                    reject=reject_criteria, preload=True)


raw.plot_image(picks=['eeg', 'eeg'])


#raw.compute_psd().plot_topomap(ch_type=ch_types, normalize=False)

      # let's explore some frequency bands
iter_freqs = [
          ('Theta', 4, 8),
          ('Alpha', 8, 16),
          ('Beta', 16, 32),
          ('Gamma', 32, 45)
      ]

     
tmin, tmax = 30,-1.
baseline = None

#resample to have to 250 hz, 
#this will allow us to compare with
#the HDHD dataset.
#raw.resample(r_s_freq, npad='auto')

      #set reference to Cz
raw.set_eeg_reference(ref_channels=['Cz'])

raw.drop_channels(['Cz'])
#return Raw object from mne class
#evs=evs.astype(int)
frequency_map=list()
for band, fmin, fmax in iter_freqs:
    # (re)load the data to save memory
    #raw = mne.io.read_raw_fif(raw_fname)
    raw.pick_types(eeg=True)  # we just look at gradiometers
    raw.load_data()

    # bandpass filter
    raw.filter(fmin, fmax, n_jobs=1,  # use more jobs to speed up.
                    l_trans_bandwidth=1,  # make sure filter params are the same
                    h_trans_bandwidth=1)  # in each band and skip "auto" option.

    '''
    # epoch
    epochs = mne.Epochs(raw, tmin, tmax, baseline=baseline,
                              preload=True)
    # remove evoked response
    epochs.subtract_evoked()

    # get analytic signal (envelope)
    epochs.apply_hilbert(envelope=True)
    frequency_map.append(((band, fmin, fmax), epochs.average()))
    del epochs
    del raw
    '''
    # Helper function for plotting spread
    def stat_fun(x):
        """Return sum of squares."""
        return np.sum(x ** 2, axis=0)

    # Plot
   # print(i,each_subject)
    fig, axes = plt.subplots(4, 1, figsize=(10, 7), sharex=True, sharey=True)
    colors = plt.get_cmap('winter_r')(np.linspace(0, 1, 4))
    plot_title=''
      
    for ((freq_name, fmin, fmax), average), color, ax in zip(frequency_map, colors, axes.ravel()[::-1]):
        times = average.times * 1e3
        gfp = np.sum(average.data ** 2, axis=0)
        gfp = mne.baseline.rescale(gfp, times, baseline=(0, 0.1))
        ax.plot(times, gfp, label=freq_name, color=color, linewidth=2.5)
          
        ax.axhline(0, linestyle='--', color='grey', linewidth=2)
        ci_low, ci_up = bootstrap_confidence_interval(average.data, random_state=0,
                                                        stat_fun=stat_fun)
        ci_low = rescale(ci_low, average.times, baseline=(None, 0))
        ci_up = rescale(ci_up, average.times, baseline=(None, 0))
        ax.fill_between(times, gfp + ci_up, gfp - ci_low, color=color, alpha=0.3)
        ax.grid(True)
          
        ax.set_ylabel('GFP')
        ax.annotate('%s (%d-%dHz)' % (freq_name, fmin, fmax),
                      xy=(0.95, 0.8),
                      horizontalalignment='right',
                      xycoords='axes fraction')
        ax.set_xlim(-1000, 3000)

    #i=i+1
        axes.ravel()[-1].set_xlabel('Time [ms]')
        ax.set_title(plot_title)

plt.show()
