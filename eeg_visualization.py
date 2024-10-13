import os
import mne
import requests
from tqdm import tqdm  # For progress bar
import matplotlib.pyplot as plt

# List of EEG URLs from Physionet MIT 

# Need to find a more efficient way to visualize this data

# Patient 01 - urls
eeg_urls01 = [
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_01.edf",
    '''
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_02.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_03.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_03.edf.seizures",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_04.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_04.edf.seizures",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_05.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_06.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_07.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_08.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_09.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_10.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_11.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_12.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_13.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_14.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_15.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_15.edf.seizures",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_16.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_16.edf.seizures",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_17.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_18.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_18.edf.seizures",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_19.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_20.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_21.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_21.edf.seizures",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_22.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_23.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_24.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_25.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_26.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_26.edf.seizures",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_27.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_29.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_30.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_31.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_32.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_33.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_34.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_36.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_37.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_38.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_39.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_40.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_41.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_42.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_43.edf",
    "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_46.edf"
    '''
]

# Directory to store downloaded .edf files
download_dir = "eeg_files"
os.makedirs(download_dir, exist_ok=True)

# Function to download a file from a URL
def download_file(url, save_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kilobyte

    with open(save_path, 'wb') as file:
        for data in tqdm(response.iter_content(block_size), total=(total_size // block_size), unit='KB', unit_scale=True):
            file.write(data)

# Process each EEG file
for i, url in enumerate(eeg_urls01):
    print(f"\nProcessing EEG file {i+1}/{len(eeg_urls01)}: {url}")

    # Define the file path
    file_name = os.path.basename(eeg_urls01[i])
    file_path = os.path.join(download_dir, file_name)

    # Check if the file has already been downloaded
    if not os.path.exists(file_path):
        print(f"Downloading {file_name}...")
        download_file(url, file_path)
    else:
        print(f"{file_name} already exists. Skipping download.")

    # Load the .edf file using MNE
    try:
        raw = mne.io.read_raw_edf(file_path, preload=True)
        print(f"Successfully loaded {file_name}")

        # Plot the raw EEG signals (you can modify or comment this line if not needed)
        raw.plot(duration=10, n_channels=10)

        # OPTIONAL: Plot Power Spectral Density (PSD) to visualize frequency content
        raw.plot_psd(fmin=0.5, fmax=50)

        # OPTIONAL: Save the figure as an image (if visualization is too large to display all at once)
        # fig = raw.plot(duration=10, n_channels=10, show=False)
        # fig.savefig(f"{file_name}_eeg_plot.png")
        # plt.close(fig)

        # Process further as needed (e.g., segment, extract features, or train CNN)

    except Exception as e:
        print(f"Error processing {file_name}: {e}")

print("Processing completed!")
