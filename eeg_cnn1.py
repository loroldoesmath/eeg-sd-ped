import pandas as pd
import requests
from sklearn.preprocessing import StandardScaler


# Load data - q: is streaming the best way?
"""
url = 'https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_04.edf'
response = requests.get(url, stream = True)

with open ('data_chunk.edf', 'wb') as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)
"""

# Use generate_interval_png function
start_seconds = [0, 10, 20]  # List of intervals
for start_sec in start_seconds:
    png_path = generate_interval_png(edf_file, start_sec)
    
    # `png_path` has to be loaded as input to CNN?
    # Need to load the image and preprocess it for CNN input: image = load_image(png_path)

    # Remove the image to save space
    os.remove(png_path)

# Remove temp directory after processing all intervals
shutil.rmtree("temp_pngs")

# Normalize/standardize data

# scaler = StandardScaler()
# scaled_data = scalar.fit_transform(data)