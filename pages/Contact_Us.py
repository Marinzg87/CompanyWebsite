import streamlit as st
import pandas
from send_email import send_email

st.header("Contact Us")

df = pandas.read_csv("topics.csv")

with st.form("contact_us", clear_on_submit=True):
    user_email = st.text_input("Your email address")
    topic = st.selectbox("What topic do you want to discuss?", df, key="topic")
    raw_message = st.text_area("Your message")

    message = f"""\
Subject: New email from Company Website

From: {user_email}
Topic: {topic}
{raw_message}
"""

    submitted = st.form_submit_button("Submit")
    if submitted:
        send_email(message)
        st.info("Message submitted")
