"""
# Visualise housing prices using streamlit
1. Get housing prices from HDB resale flat prices (1990-2014).csv
Columns: town,flat_type,flat_model,floor_area_sqm,street_name,resale_price,month,lease_commence_date,storey_range,_id,block
2. Save housing prices into a dataframe
3. Plot resale prices over month
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Get data
df = pd.read_csv('HDB resale flat prices (1990-2014).csv')

# Plot resale prices over month
st.title('Resale Prices of HDB Flats')
st.markdown(
    'This is a Streamlit app to visualise the resale prices of HDB flats over time.')
st.markdown(
    'Data source: [data.gov.sg](https://data.gov.sg/dataset/resale-flat-prices)')
st.markdown('---')

# Filter data
df = df[df['town'] == 'ANG MO KIO']
df = df[df['flat_model'] == '4 ROOM']

# Plot
sns.lineplot(x='month', y='resale_price', data=df)
plt.title('Resale Prices of 4-Room HDB Flats in Ang Mo Kio')
st.pyplot()
