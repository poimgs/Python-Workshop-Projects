from distutils.command.upload import upload
import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

# Import resale housing prices into a data frame
# df = pd.read_csv("HDB resale flat prices (1990-1999).csv")

st.title("Data Analyser")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    pr = df.profile_report()
    st_profile_report(pr)
