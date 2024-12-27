import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split


st.set_page_config(page_title="Loan Approval Prediction", page_icon=":moneybag:", layout="centered")
st.title('🏦 Loan Approval Prediction')
st.markdown("""
    Welcome to the **Loan Approval Prediction System**!  
    Fill out the form below to check the likelihood of loan approval.  
    📝 *Make sure to provide accurate information.*
""")

#Collect user Input
st.markdown("### 📋 Applicant Details")

def user_input_features():
    with st.form("loan_form"):
        no_of_dependents = st.number_input("No of Depenedents: ", min_value=0, step=1)
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        income_annum = st.number_input("Annual Income(in Rs.)", min_value=0, step=1000)
        loan_amount = st.number_input("Loan Amount(in Rs.)", min_value=0, step=1000)
        loan_term = st.number_input("Loan Term(in months)", min_value=1, step=1)
        cibil_score = st.number_input("Cibil Score", min_value=0, step=1)
        residential_assets_value = st.number_input("Residential Assets Value(in Rs.)", min_value=0, step=1000)
        commercial_assets_value = st.number_input("Commercial Assets Value(in Rs.)", min_value=0, step=1000)
        luxury_assets_value = st.number_input("Luxury Assets Value(in Rs.)", min_value=0, step=1000)
        bank_assets_value = st.number_input("Bank Assets Value(in Rs.)", min_value=0, step=1000)

        submitted = st.form_submit_button("Predict Loan Approval 🚀")

    education_encoded = 1 if education == "Graduate" else 0
    self_employed_encoded = 1 if self_employed == "Yes" else 0

    input_array = np.array([
        no_of_dependents,
        education_encoded,
        self_employed_encoded,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_assets_value
    ]).reshape(1, -1)

    return input_array, submitted

@st.cache_resource
def train_model():
   #Sample dataset and preprocessing
    df = pd.read_csv('loan_approval_dataset.csv')

    #Data Preprocessing
    df[' education'].replace([' Graduate', ' Not Graduate'], [1, 0], inplace=True)
    df[' self_employed'].replace([' Yes', ' No'], [1, 0], inplace=True)
    df[' loan_status'].replace([' Approved', ' Rejected'], [1, 0], inplace=True)
    df = df.drop(['loan_id'], axis=1)

    x = df[[
        ' no_of_dependents',
        ' education',
        ' self_employed',
        ' income_annum',
        ' loan_amount', 
        ' loan_term',
        ' cibil_score',
        ' residential_assets_value',
        ' commercial_assets_value',
        ' luxury_assets_value',
        ' bank_asset_value'
    ]]

    y = df[' loan_status']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=12)

    model = RandomForestClassifier(random_state=12)
    model.fit(x_train, y_train)

    return model


model = train_model()
input_data, submitted = user_input_features()

if submitted:
    prediction = model.predict(input_data)[0]
    result = "✅ Approved" if prediction == 1 else "❌ Not Approved"
    st.markdown("### 🎯 Prediction Result")
    st.subheader(result)

    st.markdown("""
    **Key Notes:**  
    - Loan approval depends on several factors, including CIBIL score, income, and loan amount.  
    - This prediction is indicative and not final. Please contact your bank for more information.  
    """)