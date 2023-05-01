import streamlit as st
from csv_agent import get_answer

st.header("CSVision")
st.write("Got data? Let's dive in! Upload your CSV file and I'll help you extract valuable insights.")
uploaded_file = st.file_uploader("Upload file", type=["csv"])

if uploaded_file is not None:
    query = st.text_area("Write your question ✍️")
    button = st.button("Submit")
    if button:
        st.write(get_answer(uploaded_file, query))
