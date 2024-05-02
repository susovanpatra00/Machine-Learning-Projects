# Loan Prediction

This repository contains code for predicting loan approval based on various features of loan applicants. The dataset used for this analysis is `Loan_train.csv`.

## Problem Statement

The goal of this project is to predict whether a loan application will be approved or not based on features such as gender, marital status, income, loan amount, credit history, etc.

## Approach

1. **Data Preprocessing**: 
   - Handling missing values by imputation.
   - Encoding categorical variables using Label Encoding.
   - Feature engineering: Creating a new feature `TotalIncome` by combining `ApplicantIncome` and `CoapplicantIncome`.
   - Splitting the data into training and testing sets.

2. **Model Selection**:
   - Logistic Regression
   - K-Nearest Neighbors
   - Support Vector Classifier
   - Decision Tree Classifier
   - Random Forest Classifier
   - Gradient Boosting Classifier
   - Gaussian Naive Bayes

3. **Hyperparameter Tuning**:
   - Using GridSearchCV to find the best hyperparameters for each model.

4. **Model Evaluation**:
   - Evaluating models based on accuracy score and cross-validation score.
   - Selecting the best-performing models based on accuracy.

## Results

The best models based on accuracy score are:
- Logistic Regression
- Random Forest Classifier

Both models achieved an accuracy score of 79.8% with a cross-validation score of 81.5%.

