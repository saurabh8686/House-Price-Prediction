import pandas as pd
import pickle as pk
import streamlit as st

# Load the model
with open(r'C:\\Users\\userp\\Downloads\\House_Price_Prediction\\House_prediction_model.pkl', 'rb') as file:
    model = pk.load(file)

# App title and description
st.set_page_config(page_title=" House Price Predictor", layout="wide")
st.title("🏠  House Price Predictor")
st.markdown("Use this app to predict house prices based on various features.")

# Sidebar for user inputs
st.sidebar.header("Input Features")
st.sidebar.markdown("Provide the details below:")

# Load the data
data = pd.read_csv(r'C:\\Users\\userp\\Downloads\\House_Price_Prediction\\Cleaned_data.xls')

# Sidebar inputs
loc = st.sidebar.selectbox('Choose the location', data['location'].unique())
sqft = st.sidebar.number_input('Enter Total sqft', min_value=0.0, step=1.0)
beds = st.sidebar.number_input('Enter No of Bedrooms', min_value=0, step=1)
bath = st.sidebar.number_input('Enter No of Bathrooms', min_value=0, step=1)
balc = st.sidebar.number_input('Enter No of Balconies', min_value=0, step=1)

# Prepare input
input_data = pd.DataFrame([[loc, sqft, bath, balc, beds]], columns=['location', 'total_sqft', 'bath', 'balcony', 'bedrooms'])

# Prediction button
if st.sidebar.button("Predict Price"):
    output = model.predict(input_data)
    price = abs(output[0]) * 100000  # Ensure the price is positive

    # Display results in the main area
    st.subheader("Prediction Result")
    st.success(f"💰 Estimated Price of the House: ₹{price:,.2f}")
else:
    st.info("Enter the details in the sidebar and click 'Predict Price' to see the result.")