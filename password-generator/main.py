import streamlit as st
import random

st.title("Password Generator")

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_chars = "!@#$%^&*()"

# Ask user for password information
num_characters = st.slider(
    "Password character length", min_value=8, max_value=100)
use_alphabets = st.checkbox("a-Z")
use_numbers = st.checkbox("0-9")
use_special_chars = st.checkbox("!@#")

# Create string of acceptable characters
acceptable_characters = ""
if use_alphabets:
    acceptable_characters += alphabets
if use_numbers:
    acceptable_characters += numbers
if use_special_chars:
    acceptable_characters += special_chars

# Generate password
st.write("## Generated Password:")
if use_alphabets or use_numbers or use_special_chars:
    generated_password = ""
    for i in range(num_characters):
        generated_password += random.choice(acceptable_characters)

    st.text(generated_password)
