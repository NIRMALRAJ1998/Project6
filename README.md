# Project6
**DS_Singapore Resale Flat Prices Predicting**

**Project Overview**
This project aims to develop a machine learning model that predicts the resale prices of flats in Singapore. The model is built on historical transaction data provided by the Singapore Housing and Development Board (HDB). It helps potential buyers and sellers estimate the resale value of a flat based on various factors like location, flat type, floor area, and lease duration. The solution includes data preprocessing, feature engineering, model training, evaluation, and deployment as a web application.

**Key Objectives**
Data Collection and Preprocessing:
Collect resale flat transaction data from the Singapore Housing and Development Board (HDB) for the years 1990 to the present.
Clean and preprocess the data for machine learning, handling missing values and ensuring consistency.
Feature Engineering:
Extract key features from the dataset, such as town, flat type, storey range, floor area, flat model, and lease commence date.
Enhance features for improved prediction accuracy.
Model Selection and Training:
Select appropriate regression models such as Linear Regression, Decision Trees, or Random Forest.
Train the model using the historical data and evaluate it using a portion of the dataset.
Model Evaluation:
Evaluate model performance using regression metrics like MAE (Mean Absolute Error), MSE (Mean Squared Error), RMSE (Root Mean Squared Error), and R² Score.
Streamlit Web Application:
Develop a user-friendly web application using Streamlit that allows users to input details of a flat and get resale price predictions from the trained model.
Deployment on Render:
Deploy the application on Render platform for online access.
Testing and Validation:
Test the application thoroughly to ensure its correctness and reliability.

**Technologies Used**
Python: Programming language for machine learning, data preprocessing, and application development.
Pandas & NumPy: Data manipulation and numerical computations.
Scikit-learn: Machine learning library for building and evaluating predictive models.
Streamlit: Framework for creating interactive web applications to deploy machine learning models.
Render: Platform for deploying web applications.
Matplotlib & Seaborn: Data visualization libraries for evaluating model performance and feature analysis.

**Model Overview**
Data Preprocessing:
Handle missing values, duplicate entries, and data normalization.
Feature Engineering:
Transform raw data into meaningful features that help improve model performance.
Regression Model:
Train a model (e.g., Random Forest, Linear Regression) to predict flat resale prices based on various input features.
Evaluation:
Use metrics like MAE, MSE, RMSE, and R² to evaluate the model's prediction accuracy.
Streamlit Application:
Create a simple web interface that allows users to input flat details and receive a predicted resale price.
Deployment:
Deploy the Streamlit app on Render to make the model accessible to end-users.

**How to Use**
Input Flat Details: Enter the details of a flat including town, flat type, storey range, floor area, and lease commence date.
Predict Resale Price: The trained model will predict the resale price based on the entered data.
Explore Results: Visualize model accuracy and the distribution of predicted values for deeper insights.

**Conclusion**
This project helps individuals in Singapore estimate resale flat prices more accurately by using a predictive machine learning model. The user-friendly web application enables easy access to predictions, and its deployment ensures it is accessible over the internet. The solution is highly useful for both buyers and sellers looking to make informed decisions in a competitive real estate market.

