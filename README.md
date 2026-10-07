# Breast Cancer Classification using Artificial Neural Network (ANN)

## Project Overview

This project uses an Artificial Neural Network (ANN) to classify breast tumors as **Benign** or **Malignant** using the Breast Cancer Wisconsin Diagnostic dataset.

The project covers data cleaning, exploratory data analysis, feature encoding, train-test splitting, feature scaling, ANN model building, training, prediction, and model evaluation.

## Dataset

The dataset contains **569 records** and **30 numerical features** related to breast cell characteristics.

**Target Variable:** `diagnosis`

* B - Benign
* M - Malignant

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* TensorFlow
* Keras

## Project Workflow

1. Data Collection
2. Data Understanding
3. Data Cleaning
4. Exploratory Data Analysis (EDA)
5. Target Encoding
6. Train-Test Split
7. Feature Scaling
8. ANN Model Building
9. Model Compilation
10. Model Training
11. Prediction
12. Model Evaluation

## ANN Model Architecture

* Input Layer: 30 features
* Hidden Layer: 16 neurons
* Hidden Layer Activation: ReLU
* Output Layer: 2 neurons
* Output Activation: Softmax
* Optimizer: Adam
* Loss Function: Categorical Crossentropy
* Epochs: 20

## Model Evaluation

The model was evaluated using:

* Training Accuracy
* Validation Accuracy
* Test Accuracy
* Confusion Matrix
* Classification Report

## Results

| Metric              | Result |
| ------------------- | -----: |
| Training Accuracy   | 97.25% |
| Validation Accuracy | 96.70% |
| Test Accuracy       | 98.25% |

The model correctly classified most of the test samples, with only **2 misclassifications out of 114 test samples**.

## Conclusion

The Artificial Neural Network achieved a **test accuracy of 98.25%** on the test dataset and demonstrated strong classification performance for this dataset.

This project is intended for **educational and analytical purposes** and should not be used as a medical diagnostic system.
