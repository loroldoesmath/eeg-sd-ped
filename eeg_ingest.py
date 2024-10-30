import mne
import matplotlib as plt
import os
import shutil

# Debug: URL streaming broken
def generate_interval_png(edf_url, start_sec, interval_duration=10, temp_dir="temp_pngs"):
    # Check that temporary directory exists
    os.makedirs(temp_dir, exist_ok=True)
    
    # Try to load the .edf file without preloading data
    try:
        data = mne.io.read_raw_edf(edf_url, preload=False)
    except Exception as e:
            print(f"Error reading the EDF file url: {e}")
            return None
    
    sfreq = int(data.info['sfreq'])  # Sampling frequency in Hz
    start_sample = int(start_sec * sfreq)
    end_sample = start_sample + int(interval_duration * sfreq)
    
    # Extract data for the specified interval
    data_segment, _ = data[:, start_sample:end_sample]
    
    # Create a temporary filename
    png_path = os.path.join(temp_dir, f"eeg_interval_{start_sec}_{start_sec + interval_duration}.png")
    
    # Plot and save the interval as a .png
    plt.figure(figsize=(10, 6))
    plt.plot(data_segment.T)
    plt.title(f"EEG Data from {start_sec} to {start_sec + interval_duration} seconds")
    plt.xlabel("Time (samples)")
    plt.ylabel("Amplitude (µV)")
    plt.savefig(png_path)
    plt.close()  # Free up memory
    
    return png_path

# Test generate_interval_png function

edf_file = "https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_01.edf"
test_start_sec = 0
interval_duration = 10

png_path = generate_interval_png(edf_file, test_start_sec, interval_duration)

if os.path.exists(png_path):
    print(f"File generated successfully: {png_path}")

    img = Image.open(png_path)
    img.show()
    img.close()

    print(f"Image size: {img.size}")
    print(f"Image mode: {img.mode}")
else:
    print("Failed to generate .png file :(")







# To Test - Plow raw EEG signals
"""
data.plot(title="Raw EEG Data", show=True, block=True)
"""