import pandas as pd
import requests
from sklearn.preprocessing import StandardScaler


# Load data - q: is streaming the best way?
url = 'https://archive.physionet.org/physiobank/database/chbmit/chb01/chb01_04.edf'
response = requests.get(url, stream = True)

with open ('data_chunk.edf', 'wb') as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)

# Handle missing values?
# q - are there missing values to populate?



# Normalize/standardize data

# scaler = StandardScaler()
# scaled_data = scalar.fit_transform(data)