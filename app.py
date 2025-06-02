import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("house_price_rf_model.pkl")

st.set_page_config(page_title="🏠 House Price Predictor")
st.title("🏠 House Price Prediction App")

st.write("Enter the house details below to get the predicted price:")

# User inputs
grliv = st.number_input("Above Ground Living Area (GrLivArea) in sq ft", value=1500)
qual = st.slider("Overall Quality (OverallQual)", 1, 10, 5)
garage = st.slider("Garage Capacity (GarageCars)", 0, 4, 2)
bsmt = st.number_input("Total Basement Area (TotalBsmtSF) in sq ft", value=800)
firstflr = st.number_input("1st Floor Area (1stFlrSF) in sq ft", value=1000)

# Prediction
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        'GrLivArea': grliv,
        'OverallQual': qual,
        'GarageCars': garage,
        'TotalBsmtSF': bsmt,
        '1stFlrSF': firstflr
    }])
    
    prediction = model.predict(input_df)[0]
    st.success(f"🏷️ Estimated House Price: **${prediction:,.2f}**")
