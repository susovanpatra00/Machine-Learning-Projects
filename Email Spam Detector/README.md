# Email Spam Detector

This project is an Email Spam Detector that predicts whether an email is spam or not. It utilizes machine learning techniques to classify emails based on their content.

## Libraries Used

The project utilizes the following Python libraries:

- **numpy**: For numerical computations.
- **pandas**: For data manipulation and analysis.
- **matplotlib**: For data visualization.
- **seaborn**: For statistical data visualization.
- **sklearn**: For machine learning algorithms and tools.
- **flask**: For creating the web application.
- **os**: For making directory.

## Key Components

### Data Processing and Feature Extraction
- **CountVectorizer**: Used for transforming text data into numerical features.

### Machine Learning Model
- **MultinomialNB**: Naive Bayes classifier used for text classification.

### Pipeline Construction
- **make_pipeline**: Used to construct a pipeline consisting of CountVectorizer followed by MultinomialNB.

### Model Serialization
- **pickle**: Used for saving and loading the trained machine learning model.

## Model Performance
The model achieved a test accuracy of 99.1%, indicating high performance in classifying emails.

## Web Application
The project includes a Flask-based web application that allows users to input an email and get a prediction of whether it is spam or not.

## Usage
To run the web application:
1. Install the required libraries by running `pip install -r requirements.txt`.
2. Run the Flask application using `python app.py`.
3. Access the web application through your browser.
