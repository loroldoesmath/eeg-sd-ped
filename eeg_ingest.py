import mne
import matplotlib as plt

file01_01 = "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_01.edf"
data = mne.io.read_raw_edf(file01_01)
raw_data = data.get_data()

# Access metadata included in the file and a list of all channels:
info = data.info
channels = data.ch_names

# To Test - Plow raw EEG signals
data.plot(title="Raw EEG Data", show=True, block=True)