import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st


st.set_page_config(
    page_title="API데이터솔루션을 활용한 대시보드 만들기",
    layout="wide"
)

# Add Title
st.title("판매성과")
 
# Import your data
df = pd.read_excel('/Users/user/Desktop/pywalker/판매성과.xlsx')
 
# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)

