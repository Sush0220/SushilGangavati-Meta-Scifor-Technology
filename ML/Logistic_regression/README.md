# Email Spam Classifier - Logistic Regression

This project aims to classify emails as either **spam** or **ham (non-spam)** using a **Logistic Regression** model. The model is trained on a dataset containing various email features (such as word counts or presence of specific terms) and predicts whether an email belongs to the spam category or not.

## Dataset

The dataset used in this project consists of two columns:
- **Category**: Indicates whether the email is spam or ham.
- **Message**: Contains the content of the email message.

The **Category** is the target variable, with `1` representing **spam** and `0` representing **ham** (non-spam).

## Key Steps in the Project

1. **Data Preprocessing**:
    - Load the dataset and clean the data (e.g., handle missing values if necessary).
    - Convert the text messages into numerical features using techniques such as **TF-IDF** or **CountVectorizer**.

2. **Logistic Regression**:
    - Train a Logistic Regression model using the processed features and corresponding labels.
    - Evaluate the model on test data.

3. **Evaluation**:
    - **Accuracy**: Measures the overall correctness of the model.
    - **Confusion Matrix**: Provides insights into false positives and false negatives, helping to assess classification performance.
    - **ROC Curve**: Used to evaluate the model's ability to distinguish between spam and ham.

4. **Feature Importance**:
    - The importance of different features (words/terms) is visualized based on the coefficients of the logistic regression model.

## How the Model Works

- The Logistic Regression model computes a probability that an email belongs to the **spam** class. The decision threshold is typically set to **0.5**: if the model's predicted probability for spam is above this threshold, the email is classified as **spam** (1); otherwise, it's classified as **ham** (0).
- Features (such as specific words or phrases) are used to predict the outcome, and the model assigns each feature a **coefficient** that indicates its importance. Positive coefficients mean the feature is more likely to classify an email as spam, while negative coefficients mean the feature is more likely to classify it as ham.

## Evaluation Metrics

- **Accuracy**: The proportion of correct predictions (both spam and ham).
- **Confusion Matrix**: Visualizes the performance of the classification model, showing the counts of true positives, false positives, true negatives, and false negatives.
- **ROC Curve**: Plots the **True Positive Rate** against the **False Positive Rate**, showing the trade-off between sensitivity and specificity at different thresholds.


