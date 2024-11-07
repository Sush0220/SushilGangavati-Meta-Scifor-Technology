# CGPA to Package Prediction
This project implements a simple linear regression model to predict the salary package (in LPA - Lakhs Per Annum) based on a student's CGPA. 
The model is trained on a synthetic dataset of 200 students, where each record contains a student's CGPA and their associated salary package.

## Overview
This project demonstrates how to build a simple linear regression model to predict a student's potential salary package based on their CGPA (Cumulative Grade Point Average). 
The model uses scikit-learn to train on a dataset of 200 synthetic student records, where each record contains the student's CGPA and corresponding salary package (in Lakhs Per Annum, or LPA). 
This project highlights a practical use of machine learning for educational and hiring contexts, where there is often a positive correlation between academic performance and expected salary.

Linear regression is a statistical technique that models the relationship between two variables by fitting a linear equation to the observed data. In this project:

- Input Feature (X): The CGPA of the student.
- Output/Target (y): The expected salary package (in LPA).

The model learns from the data to determine a linear relationship between CGPA and salary package, enabling it to make predictions on new CGPA values.

## Dataset
The dataset (student_data.csv) consists of two columns:
- CGPA: Represents a student's CGPA, ranging from 5.0 to 10.0.
- Package (LPA): Represents the expected salary package in LPA (Lakhs Per Annum). The values are generated with slight variation to simulate real-world data, where students with higher CGPAs generally tend to secure better packages.

- ## How it Works
1. Data Visualization:
- The first step in the code visualizes the relationship between CGPA and Package using a scatter plot. This helps us see the trend and assess if a linear relationship exists, which is essential for linear regression.

2. Model Training:
- The dataset is split into training and testing sets.
- We use the training data to fit a linear regression model.
- The model tries to find the best-fitting line by minimizing the difference between actual and predicted values.

3. Making Predictions:
- After training, the model can predict the salary package for a new CGPA value.
- The model equation 
y=m⋅x+b (where m is the slope and b is the intercept) helps calculate the salary package based on the input CGPA.

4. Evaluation:
- The model is evaluated using metrics like Mean Squared Error (MSE) and R-squared (R²) to determine its accuracy. A lower MSE and a higher R² value indicate a better fit of the model to the data.
