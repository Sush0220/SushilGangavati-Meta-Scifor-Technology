import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
import plotly.express as px


st.set_page_config(page_title="Loan Approval Prediction", page_icon=":moneybag:", layout="centered")
st.title('🏦 Loan Approval Prediction')
st.markdown("""
    Welcome to the **Loan Approval Prediction System**!  
    Fill out the form below to check the likelihood of loan approval.  
    📝 *Make sure to provide accurate information.*
""")

@st.cache_data
def generate_dataset():
    np.random.seed(42)

    # Generating synthetic data
    data = {
        'no_of_dependents': np.random.randint(0, 5, 1000),
        'education': np.random.choice(['Graduate', 'Not Graduate'], 1000),
        'self_employed': np.random.choice(['Yes', 'No'], 1000),
        'income_annum': np.random.randint(100000, 1000000, 1000),
        'loan_amount': np.random.randint(50000, 1000000, 1000),
        'loan_term': np.random.choice([12, 24, 36, 48, 60], 1000),
        'cibil_score': np.random.randint(300, 900, 1000),
        'residential_assets_value': np.random.randint(100000, 5000000, 1000),
        'commercial_assets_value': np.random.randint(100000, 5000000, 1000),
        'luxury_assets_value': np.random.randint(50000, 2000000, 1000),
        'bank_assets_value': np.random.randint(100000, 5000000, 1000),
        'loan_status': np.random.choice([0, 1], 1000)
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Generate synthetic target variable (loan_status)
    df['loan_status'] = np.random.choice([0, 1], size=1000, p=[0.3, 0.7])  # 70% approved, 30% rejected

    # Encode categorical variables
    df['education'].replace(['Graduate', 'Not Graduate'], [1, 0], inplace=True)
    df['self_employed'].replace(['No', 'Yes'], [0, 1], inplace=True)

    return df

df = generate_dataset()

#Sidebar Charts
st.sidebar.markdown("### 📊 Dataset Insights")
loan_status_counts = df['loan_status'].value_counts()
st.sidebar.write("Loan Status Counts: ")
st.sidebar.write(loan_status_counts)
loan_status_labels = ['Approved', 'Not Approved']

pie_chart_data = pd.DataFrame({
    'Loan Status': loan_status_labels,
    'Count': loan_status_counts.values
})
fig = px.pie(
    pie_chart_data,
    values='Count',
    names='Loan Status',
    title='Loan Status Distribution',
    hover_data=['Count'],
    labels={'Loan Status': 'Loan Status', 'Count': 'Count'},
    color_discrete_sequence=['#4CAF50', '#FF5252']
)

fig.update_traces(
    textinfo='percent+label',
    hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent}"
)

st.sidebar.plotly_chart(fig)

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
    x = df[[
        'no_of_dependents',
        'education',
        'self_employed',
        'income_annum',
        'loan_amount', 
        'loan_term',
        'cibil_score',
        'residential_assets_value',
        'commercial_assets_value',
        'luxury_assets_value',
        'bank_assets_value'
    ]]

    y = df['loan_status']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=12)

    model = RandomForestClassifier(random_state=12)
    model.fit(x_train, y_train)

    return model


model = train_model()
input_data, submitted = user_input_features()

if submitted:
    probabilities = model.predict_proba(input_data)[0]
    prediction = 1 if probabilities[1] > 0.7 else 0
    st.write(prediction)
    result = "✅ Approved" if prediction == 1 else "❌ Not Approved"
    st.markdown("### 🎯 Prediction Result")
    st.subheader(result)

    
    st.markdown("""
    **Key Notes:**  
    - Loan approval depends on several factors, including CIBIL score, income, and loan amount.  
    - This prediction is indicative and not final. Please contact your bank for more information.  
    """)
