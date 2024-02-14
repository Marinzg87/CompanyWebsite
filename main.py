import streamlit as st
import pandas

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some other text (description)
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

# Prepare the columns
col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

# Make a dataframe with the company members
df = pandas.read_csv("data.csv")

# Add content to the first column
with col1:
    # Iterate over only the first four rows
    for index, row in df[:4].iterrows():
        # Add member's first and last name
        st.header(f"{row['first name'].capitalize()} "
                  f"{row['last name'].capitalize()}")
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the second column
with col2:
    # Iterate over rows 4 to 7
    for index, row in df[4:8].iterrows():
        # Add member's first and last name
        st.header(f"{row['first name'].capitalize()} "
                  f"{row['last name'].capitalize()}")
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])

# Add content to the third column
with col3:
    # Iterate over rows 7 to 12
    for index, row in df[8:].iterrows():
        # Add member's first and last name
        st.header(f"{row['first name'].capitalize()} "
                  f"{row['last name'].capitalize()}")
        # Add member's role in the company
        st.write(row["role"])
        # Add member's photo
        st.image("images/" + row["image"])
