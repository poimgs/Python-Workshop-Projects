import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def get_housing_prices(path="./HDB resale flat prices (1990-1999).csv"):
    df = pd.read_csv(path)

    # Transform data into a data frame for me to visualise
    df['month'] = pd.to_datetime(df['month'])
    df['resale_price'] = df['resale_price'].astype(float)

    return df


def flat_type_filter(df):
    flat_type_choices = ['All']
    flat_types = df['flat_type'].unique().tolist()
    flat_types_sorted = sorted(flat_types)
    flat_type_choices.extend(flat_types_sorted)

    chosen_flat_type = st.selectbox(
        "Choose a flat type to filter data frame", flat_type_choices)
    return chosen_flat_type


def transform_df(df, flat_type="All"):
    # Filter by selected flat type if selected
    if flat_type != "All":
        df = df[df['flat_type'] == flat_type]

    mean_resale_price_df = df.groupby(['month']).agg(
        {'resale_price': 'mean'}).reset_index()

    return mean_resale_price_df


def plot_year_to_resale_prices(mean_resale_price_df):
    # Create visualisation showing trend of resale prices
    x = mean_resale_price_df['month']
    y = mean_resale_price_df['resale_price']

    figure, ax = plt.subplots()
    ax.plot(x, y)

    st.pyplot(figure)
