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
