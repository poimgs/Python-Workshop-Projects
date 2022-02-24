import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(layout="wide")

st.title("Singapore HDB Resale Prices Automated Analyser")
st.write("This app is designed to help you analyse the resale prices of HDB flats in Singapore.")
st.caption("Source: https://data.gov.sg/dataset/resale-flat-prices?resource_id=adbbddd3-30e2-445f-a123-29bee150a6fe")

df = pd.read_csv(
    "./resale-prices-automated-analyser/HDB resale flat prices (1990-1999).csv")
pr = df.profile_report()
st_profile_report(pr)
