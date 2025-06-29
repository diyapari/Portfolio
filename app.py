import streamlit as st
import streamlit.components.v1 as components

# Read the HTML file
with open("pp.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Display the HTML in Streamlit
st.set_page_config(layout="wide")
components.html(html_data, height=3000, scrolling=True)
