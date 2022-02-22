import streamlit as st
import datetime
import time
import pytz

# THE TIME
THE_TIME = datetime.datetime(2022, 2, 22, 22, 22).strftime("%D %H:%M")
st.title(f"Is it {THE_TIME}?")

# Get current time in Singapore
timezone = pytz.timezone("Asia/Singapore")
current_time = datetime.datetime.now(timezone).strftime("%D %H:%M")
st.header(f"The time is: {current_time}")

# Check if current time is equal to THE TIME
if current_time == THE_TIME:
    st.subheader("It's time!")
    st.balloons()
elif current_time > THE_TIME:
    st.subheader("It's too late!")
else:
    st.subheader("Not yet...")

# Keep checking every second
while True:
    if current_time == THE_TIME:
        break

    time.sleep(1)
    st.experimental_rerun()
