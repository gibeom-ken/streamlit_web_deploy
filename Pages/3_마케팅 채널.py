import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st


 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="마케팅 채널",
    layout="wide"
)
 
# Add Title
st.title("마케팅 채널")
 
# Import your data
df = pd.read_excel("마케팅 채널.xlsx")
 
# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)