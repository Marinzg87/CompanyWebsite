import streamlit as st
import pandas

st.header("Contact Us")

df = pandas.read_csv("topics.csv")

with st.form("contact_us", clear_on_submit=True):
    user_email = st.text_input("Your email address")
    topic = st.selectbox("What topic do you want to discuss?", df, key="topic")
    message = st.text_area("Your message")

    submitted = st.form_submit_button("Submit")
    if submitted:
        print(topic)
        st.info("Message submitted")
