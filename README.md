# Data Classification Using AI

## DecodeLabs Artificial Intelligence Internship - Project 2

### Project Overview

This project is part of the DecodeLabs Artificial Intelligence Internship.

The goal of this project is to build a basic classification model using a small dataset. The project demonstrates the basic supervised learning process, including loading and understanding data, splitting data into training and testing sets, training a classification model, and making predictions.

## Objective

The main objectives of this project are:

* Load and understand a dataset.
* Prepare data for machine learning.
* Split the dataset into training and testing sets.
* Apply a simple classification algorithm.
* Train a machine learning model.
* Test the model and measure its accuracy.
* Make a prediction using new data.

## Dataset

The project uses the **Iris dataset**, which contains measurements of iris flowers.

The dataset contains:

* **150 samples**
* **4 features**
* **3 classes**

### Features

* Sepal length
* Sepal width
* Petal length
* Petal width

### Classes

* Setosa
* Versicolor
* Virginica

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn

## Machine Learning Algorithm

A **Decision Tree Classifier** is used for classification.

The model learns patterns from the training data and uses those patterns to classify the testing data and new input data.

## Project Workflow


Load Dataset
     |
     v
Understand Dataset
     |
     v
Separate Features and Target
     |
     v
Split Data into Training and Testing Sets
     |
     v
Train Decision Tree Model
     |
     v
Test Model
     |
     v
Calculate Accuracy
     |
     v
Make New Prediction


## Training and Testing

The dataset is divided into:

* **80% training data** - 120 samples
* **20% testing data** - 30 samples

The training data is used to train the Decision Tree model, while the testing data is used to evaluate its performance.

## Results

The model was trained successfully and tested using the testing dataset.

### Model Accuracy

**100.00%**

### New Prediction

A new flower measurement was provided to the trained model.

The predicted class was:

**Setosa**

## Project Structure


Data-Classification-AI/
|
+-- main.py
+-- README.md
+-- requirements.txt
+-- venv/


## How to Run

### 1. Activate the virtual environment

powershell
.\venv\Scripts\Activate.ps1


### 2. Run the Python program

powershell

python main.py


## Expected Output

The program displays:

* Dataset information
* First five rows of the dataset
* Available class names
* Training and testing sample counts
* Model training status
* Model accuracy
* New prediction

## Learning Outcomes

Through this project, I practiced:

* Data handling using Pandas
* Understanding a machine learning dataset
* Splitting data into training and testing sets
* Supervised learning fundamentals
* Classification model training
* Model evaluation
* Making predictions with a trained model

## Internship

**Program:** DecodeLabs Artificial Intelligence Internship
**Project:** Project 2 - Data Classification Using AI
**Batch:** 2026
