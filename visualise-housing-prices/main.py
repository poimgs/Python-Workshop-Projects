import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests


@st.cache
def get_housing_prices():
    # Transform data into a data frame for me to visualise
    resale_prices_resource_ids = [
        "adbbddd3-30e2-445f-a123-29bee150a6fe",  # 1990 - 1999
        "8c00bf08-9124-479e-aeca-7cc411d884c4",  # 2000 - 2012
        "83b2fc37-ce8c-4df4-968b-370fd818138b",  # 2012 - 2014
        "1b702208-44bf-4829-b620-4615ee19b57c",  # 2015 - 2016
        "f1765b54-a209-4718-8d38-a39237f502b3",  # 2017 - now
    ]

    # Get data from API
    dataframes = []

    for resource_id in resale_prices_resource_ids:
        url = f"https://data.gov.sg/api/action/datastore_search?resource_id={resource_id}&limit=10000000000"
        res = requests.get(url)
        data = res.json()['result']['records']
        df = pd.DataFrame(data)
        dataframes.append(df)

    # Combine dataframes into one
    df = pd.concat(dataframes)

    # Transform column data type into appropriate data type for analysis
    df['month'] = pd.to_datetime(df['month'])
    df['resale_price'] = df['resale_price'].astype(float)
    df['flat_type'] = df['flat_type'].str.replace('MULTI GENERATION', 'MULTI-GENERATION')

    return df


def flat_type_filter(df, column):
    flat_type_choices = ['All']
    flat_types = df['flat_type'].unique().tolist()
    flat_types_sorted = sorted(flat_types)
    flat_type_choices.extend(flat_types_sorted)

    chosen_flat_type = column.selectbox(
        "Choose a flat type to filter data frame", flat_type_choices)
    return chosen_flat_type


def town_filter(df, column):
    town_choices = ['All']
    towns = df['town'].unique().tolist()
    towns_sorted = sorted(towns)
    town_choices.extend(towns_sorted)

    chosen_town = column.selectbox(
        "Choose a town to filter data frame", town_choices)
    return chosen_town


def transform_df(df, flat_type, town):
    # Filter by selected flat type
    if flat_type != "All":
        df = df[df['flat_type'] == flat_type]

    if town != "All":
        df = df[df['town'] == town]

    mean_resale_price_df = df.groupby(['month']).agg(
        {'resale_price': 'mean'}
    ).reset_index()

    return mean_resale_price_df


def plot_year_to_resale_prices(mean_resale_price_df):
    # Create visualisation showing trend of resale prices
    x = mean_resale_price_df['month']
    y = mean_resale_price_df['resale_price']

    # Create figure and axes objects to plot on
    fig, ax = plt.subplots()

    # Create simple line plot
    ax.plot(x, y)

    # Set title and labels
    ax.set_title("Resale Price Trend")
    ax.set_xlabel("Year")
    ax.set_ylabel("Resale Price")

    # Show the plot
    st.pyplot(fig)


st.title("Visualise Housing prices")

df = get_housing_prices()

left_filter, right_filter = st.columns(2)
chosen_flat_type = flat_type_filter(df, left_filter)
chosen_town = town_filter(df, right_filter)

mean_resale_price_df = transform_df(df, chosen_flat_type, chosen_town)
plot_year_to_resale_prices(mean_resale_price_df)

with st.expander("See the data that was used to create this!"):
    st.write("Note: Only the first 100 rows is shown, there is actually 709050 rows")
    st.write("Link: https://data.gov.sg/dataset/resale-flat-prices")
    st.write(df.iloc[:100])
