# Pediatric EEG-Based Seizure Detection

## Project Overview 

This project focuses on improving **EEG-based seizure detection** in children using a combination of **computational** and **machine learning methods**. Specifically, I apply **Convolutional Neural Networks (CNNs)** to analyze EEG data and detect seizures more accurately. 

## Project Motivation

When my one-year-old niece had a Grand Mal seizure, I'd never felt more powerless or scared. From that day, it became my goal to use my background in mathematics and data science to enhance our understanding and detection of pediatric seizure disorders.

## Dataset
I'm utilizing EEG data from the **CHB-MIT Scalp EEG Database**, which contains recordings from children aged **2 to 19**. This dataset is publicly available from PhysioNet at the following link:

[CHB-MIT Scalp EEG Database](https://archive.physionet.org/physiobank/database/chbmit/chb01/)

The EEG data is in **.edf format** and contains multiple recordings from various patients, including those with seizures. 

I convert the EEG data to a CSV file by sequencing parametric data.

## Files and Structure
- **`eeg_cnn1.py`**: This Python script handles the streaming of the `.edf` EEG data and defines the structural layout of the **Convolutional Neural Network (CNN)** model. The model is trained to classify seizure vs. non-seizure events in the provided EEG data.

## Key Methods and Approach
- **Machine Learning Approach**: A **CNN model** is employed to extract features from the EEG data and detect patterns associated with seizures. CNNs are well-suited for this type of time-series data due to their ability to automatically learn spatial hierarchies from input data.
  
- **Fast-Fourier Transform**:
  
- **Data Preprocessing**: The EEG data is preprocessed to ensure proper input formatting for the CNN. This includes steps like data normalization, segmentation of time windows, and transforming EEG signals into a form suitable for input into the neural network.

## How to Run
1. **Run the CNN Model**:
   - The `eeg_cnn1.py` script contains the full implementation of the model.
   - You can run the script using Python by navigating to the project directory and running:
     ```bash
     python eeg_cnn1.py
     ```

## Future Enhancements
- **Data Augmentation**: Implement data augmentation techniques to increase the robustness of the model.
- **Model Optimization**: Further optimize the model's hyperparameters and experiment with different architectures to improve detection accuracy.
- **Real-time Monitoring**: Develop a real-time monitoring system for continuous EEG streaming and seizure detection.

## Acknowledgments
This project was made possible thanks to the **CHB-MIT Scalp EEG Database** and **PhysioNet** for providing high-quality data. Shout out to all researchers making their data publically available in the hopes of saving lives.
This project was inspired by Elianna, who has given me so much hope for the future of this world just by being born.
