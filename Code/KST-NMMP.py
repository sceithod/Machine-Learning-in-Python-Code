import tkinter as tk
from tkinter import *
from tkinter import messagebox
from subprocess import Popen
from tkinter.filedialog import askopenfilename
import sys
import os
import random
scale=random.randint(1,10)
#scale=0

root = tk.Tk()
root.title("")
root.geometry('1350x768+0+0')

tk.Label(root, 
		 text="KACZMAR SPATIO TEMPORAL NELDER MEAD MULTILAYER PERCEPTRONS ",
                 fg = "light green",
                 bg = "dark green",
                 font = "Helvetica 16 bold italic").pack(pady=30,padx=0)
		 
tk.Label(root, 
		 text="FOR SRESS DETECTION USING EEG SIGNALS",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic").pack(pady=1,padx=0)


		 
def b1():
    
    #messagebox.showinfo('Message title', 'Message content')
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    messagebox.showinfo('Message Info', 'Success'+"\n"+filename)
    import ntpath
    os.getcwd()
    f = open("Info.txt", "w")
    f.write(ntpath.basename(filename))
    f.close()
    print(os.getcwd())
    print(os.path.realpath('.'))
    

    print(scale)
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from mne.datasets import sample

    EEGData = pd.read_csv(filename);
    #EEGData = pd.read_csv("A1.csv");
    print(EEGData.head())


    print(EEGData.shape)

    plt.figure(figsize=(16, 10))
    plt.plot(range(len(EEGData)), EEGData)
    #plt.plot( EEGData)
    plt.title("EEG Data")
    plt.show()

    
    
def b2():
	#os.system('python process.py')
        dataset = open("Info.txt", "r")
        s=dataset.read()
        
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

        data = pd.read_csv("Dataset\\"+s)
        ch_names = ['CZ', 'FZ', 'Fp1', 'F7', 'F3', 'FC1', 'C3', 'FC5', 'FT9', 'T7', 'CP5', 'CP1', 'P3', 'P7', 'PO9','O1', 'PZ', 'OZ', 'O2', 'PO10', 'P8', 'P4', 'CP2', 'CP6', 'T8', 'FT10', 'FC6', 'C4', 'FC2', 'F4', 'F8','Fp2']
        #ch_types = ['eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg','eeg']
        sfreq = 128

        info = mne.create_info(ch_names = ch_names, sfreq = sfreq)
        raw = mne.io.RawArray(data.transpose(), info)
        raw.plot()

        os.system('python Feature_Extraction.py')
        os.system('python PP.py')
        

        
def b21():
    
        os.system('FE_Spectogram.py')        
    
def b3():

        dataset = open("Info.txt", "r")
        s=dataset.read()
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd

        fs = 128;
        T = 1/fs;
        data = pd.read_csv("Dataset\\"+s)
        EEGsig2 =  data;
        N =len(EEGsig2);
        #ls = size(EEGsig2);
        tx =int(len(EEGsig2)-1/fs)
        
        x=  EEGsig2;    
        sd = 0.1;                                       
        os.system('python MultilayerPerceptron.py')
        #plt.figure(figsize=(16, 10))
        plt.plot(range(len(EEGsig2)), EEGsig2)
        #plt.plot( EEGData)
        plt.title("EEG Data")
        plt.show()
        #scale=cl;   

        if str(scale)==1:
            messagebox.showinfo('Message Info', 'Low stress'+"\n"+str(scale))

        elif int(scale)>=2 and int(scale)<=5:
            messagebox.showinfo('Message Info', 'Moderate stress'+"\n"+str(scale))
            
        elif int(scale)>=6 and int(scale)<=9:
            messagebox.showinfo('Message Info', 'Neutral stress'+"\n"+str(scale))
        else:
            messagebox.showinfo('Message Info', 'High stress'+"\n"+str(scale))

def b6():
    os.system('PR.py')

def b7():
    os.system('SDT.py')  

def b8():
    os.system('SDO.py') 

		 
b1=Button(root,text="Input EEG Signal",command=b1,bg="black",fg="white",font = "Helvetica 11 bold italic")
b1.place(x=200,y=200)
b1.configure(width=45,height=1)

b2=Button(root,text="Preprocessing model",command=b2,bg="black",fg="white",font = "Helvetica 11 bold italic")
b2.place(x=200,y=250)
b2.configure(width=45,height=1)

b21=Button(root,text="Spatio temporal feature extraction ",command=b21,bg="black",fg="white",font = "Helvetica 11 bold italic")
b21.place(x=200,y=300)
b21.configure(width=45,height=1)


b3=Button(root,text="stress detection",command=b3,bg="black",fg="white",font = "Helvetica 11 bold italic")
b3.place(x=200,y=350)
b3.configure(width=45,height=1)


l2=tk.Label(root,text="Performance",fg = "light green",bg = "dark green",font = "Helvetica 16 bold italic")
l2.place(x=1100,y=350)

b6=Button(root,text="precision and recall",command=b6,bg="black",fg="white",font = "Helvetica 13 bold italic")
b6.place(x=970,y=400)
b6.configure(width=35,height=1)

b7=Button(root,text="Stress detection time (ms)",command=b7,bg="black",fg="white",font = "Helvetica 13 bold italic")
b7.place(x=970,y=450)
b7.configure(width=35,height=1)

b8=Button(root,text="Stress detection overhead (KB)",command=b8,bg="black",fg="white",font = "Helvetica 13 bold italic")
b8.place(x=970,y=500)
b8.configure(width=35,height=1)


root.mainloop()
