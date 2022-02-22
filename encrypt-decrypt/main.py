import streamlit as st
from cryptography.fernet import Fernet

selected = st.sidebar.radio("Encrypt or decrypt", ("Encrypt", "Decrypt"))

if selected == "Encrypt":
    user_input = st.text_area("Text to encrypt", "Hello World", height=200)
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(user_input.encode())
    st.write(encrypted_text.decode())
    st.write(key.decode())
else:
    user_input = st.text_area("Text to encrypt", "Hello World", height=200)
    key = st.text_area("Key")
    cipher_suite = Fernet(key.encode())
    decrypted_text = cipher_suite.decrypt(user_input.encode())
    st.write(decrypted_text.decode())
