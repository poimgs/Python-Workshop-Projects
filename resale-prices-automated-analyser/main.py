import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout="wide")

st.title("Resale  Analyser")

df = pd.read_csv(
    "./resale-prices-automated-analyser/HDB resale flat prices (1990-1999).csv")
pr = df.profile_report()
st_profile_report(pr)
