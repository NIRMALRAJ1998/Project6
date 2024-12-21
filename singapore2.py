import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

# Load trained model
model = load(r"C:\Users\R.Nirmalraj\Desktop\New folder (3)\RandomFRegressor_model.joblib")


# Load your data
                               
df1=pd.read_csv(r"C:\Users\R.Nirmalraj\Desktop\New folder (3)\Singapore\Resale Flat Prices (Based on Approval Date), 1990 - 1999.csv")
df2=pd.read_csv(r"C:\Users\R.Nirmalraj\Desktop\New folder (3)\Singapore\Resale Flat Prices (Based on Approval Date), 2000 - Feb 2012.csv")
df3=pd.read_csv(r"C:\Users\R.Nirmalraj\Desktop\New folder (3)\Singapore\Resale Flat Prices (Based on Registration Date), From Jan 2015 to Dec 2016.csv")
df4=pd.read_csv(r"C:\Users\R.Nirmalraj\Desktop\New folder (3)\Singapore\Resale Flat Prices (Based on Registration Date), From Mar 2012 to Dec 2014.csv")
df5=pd.read_csv(r"C:\Users\R.Nirmalraj\Desktop\New folder (3)\Singapore\Resale flat prices based on registration date from Jan-2017 onwards.csv")

data=pd.concat([df1,df2,df3,df4,df5], ignore_index=True)


# Define preprocess_input function if needed
def preprocess_input(selected_town, selected_flat_type, floor_area_sqm, flat_model, lease_commence_date, remaining_lease):
    # Your preprocessing code here
    # Example:
    town_mapping = {
        'ANG MO KIO': 1,
        'BEDOK': 2,
        # Add mappings for other towns...
    }
    flat_type_mapping = {
        '3 ROOM': 3,
        '4 ROOM': 4,
        # Add mappings for other flat types...
    }
    flat_model_mapping = {
        'Improved': 1,
        'New Generation': 2,
        # Add mappings for other flat models...
    }
    town_numeric = town_mapping.get(selected_town, 0)
    flat_type_numeric = flat_type_mapping.get(selected_flat_type, 0)
    flat_model_numeric = flat_model_mapping.get(flat_model, 0)
    
    # You'll need to add preprocessing for other features as well
    
    # Create a list or array of preprocessed input data
    input_data = [town_numeric, flat_type_numeric, floor_area_sqm, flat_model_numeric, lease_commence_date, remaining_lease]
    
    # Add placeholders for missing features (if any)
    input_data += [0] * (12 - len(input_data))  # Add zeros for missing features
    
    return input_data

# Input interface
st.title('Singapore Flat Resale Price Prediction')

# Dropdowns for user input
selected_town = st.selectbox('Select Town', data['town'].unique())  # Load unique values from your dataset
selected_flat_type = st.selectbox('Select Flat Type', data['flat_type'].unique())  # Load unique values from your dataset
floor_area_sqm = st.number_input('Enter Floor Area (sqm)', min_value=0.0, step=1.0)
flat_model = st.selectbox('Select Flat Model', data['flat_model'].unique())  # Load unique values from your dataset
lease_commence_date = st.number_input('Enter Lease Commence Date', min_value=1960, max_value=2022, step=1)
remaining_lease = st.number_input('Enter Remaining Lease', min_value=0, max_value=99, step=1)

# Button to trigger prediction
if st.button('Predict'):
    # Preprocess input data
    input_data = preprocess_input(selected_town, selected_flat_type, floor_area_sqm, flat_model, lease_commence_date, remaining_lease)
    
    # Ensure input_data is not None
    if input_data is not None:
        # Convert input_data to a 2D array
        input_data = np.array(input_data).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display prediction with currency format
        st.write('Predicted Resale Price: $', '{:,.2f}'.format(prediction[0]))
    else:
        st.write('Please fill in all input fields.')