import streamlit as st
from personal import *

st.title("Visualise Housing prices")

df = get_housing_prices()
chosen_flat_type = flat_type_filter(df)
mean_resale_price_df = transform_df(df, chosen_flat_type)
plot_year_to_resale_prices(mean_resale_price_df)

with st.expander("See the data that was used to create this!"):
    st.write("Note: Only the first 100 rows is shown, there is actually 709050 rows")
    st.write("Link: https://data.gov.sg/dataset/resale-flat-prices")
    st.write(df.iloc[:100])
