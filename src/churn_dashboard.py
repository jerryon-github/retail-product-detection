import streamlit as st
import pandas as pd
import joblib

# Load model and features
model = joblib.load('../model/churn_model.pkl')
feature_list = joblib.load('../model/feature_list.pkl')

st.title("📊 Customer Churn Predictor")

# Dynamic form based on feature list
input_data = {}
for feature in feature_list:
    if feature == 'gender':
        input_data[feature] = st.selectbox("Gender", ['Male', 'Female'])
    elif feature == 'contract_type':
        input_data[feature] = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
    else:
        input_data[feature] = st.number_input(f"{feature.capitalize()}", min_value=0.0, step=1.0)

if st.button("Predict Churn"):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]

    st.markdown(f"### 🔍 Prediction: {'Churn' if prediction else 'No Churn'}")
    st.markdown(f"**Confidence: {prob*100:.2f}%**")