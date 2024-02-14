import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")
company_description = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nulla porta volutpat tortor eget suscipit. Nullam gravida ornare ex 
quis faucibus. Sed odio justo, tempus non bibendum rhoncus, feugiat quis 
purus. Nullam eget faucibus est. Phasellus a vulputate justo. Praesent ac 
orci consequat, elementum erat vitae, feugiat mauris.
"""
st.write(company_description)

st.subheader("Our Team")

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].capitalize()} "
                  f"{row['last name'].capitalize()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].capitalize()} "
                  f"{row['last name'].capitalize()}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name'].capitalize()} "
                  f"{row['last name'].capitalize()}")
        st.write(row["role"])
        st.image("images/" + row["image"])
