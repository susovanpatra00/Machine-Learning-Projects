# Machine Learning Model Comparison with Iris Dataset

This repository contains code for comparing the performance of various machine learning models on the Iris dataset. The objective is to classify iris flowers into three species based on four features: sepal length, sepal width, petal length, and petal width.

## Dataset
The dataset used in this project is the famous Iris dataset, which is often used as a beginner's dataset for classification tasks. It consists of 150 samples, each belonging to one of three species of iris flowers: setosa, versicolor, and virginica.

## Models
The following machine learning models are compared in this project:
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Classifier (SVC)
- Decision Tree Classifier
- Random Forest Classifier
- Gradient Boosting Classifier
- Gaussian Naive Bayes

## Methodology
1. The dataset is split into training and testing sets using a 75-25 split ratio.
2. Each model is trained on the training set using 5-fold cross-validation to find the best hyperparameters.
3. The performance of each model is evaluated based on accuracy score and classification report on the testing set.
4. The best models are identified based on their accuracy score and cross-validation score.

## Results
The best-performing models based on accuracy score are as follows:
1. Logistic Regression
2. K-Nearest Neighbors
3. Support Vector Classifier

