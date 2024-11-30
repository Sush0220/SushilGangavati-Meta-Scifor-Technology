import streamlit as st
import datetime
import time
st.title("Register")


name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
password = st.text_input("Enter your password", type="password")
confirm_password = st.text_input("Confirm your password", type="password")

dob = st.date_input("Enter your date of birth", min_value=datetime.date(1900, 1, 1))
choices = st.multiselect("Hobbies",["Cricket","Football","Chess","Tennis","Badminton","Hockey","Table Tennis"])
gender = st.radio("Gender",["Male","Female","Others"],index=None)
if st.button("Register"):
    if password == confirm_password:
        with st.spinner("Registering..."):
            time.sleep(2)
            st.success("Welcome! Registration successful!")
            st.balloons()
    elif password == "" or confirm_password == "":
        st.warning("Please enter both passwords!")
    else:
        st.error("Passwords do not match!")

