# Import libraries
import streamlit as st
import qrcode

st.title("QR Code Generator")

url = st.text_input("Enter the URL to be encoded in QR code")

if url:
    qr = qrcode.make(url)
    qr.save("qr.png")

    st.image("qr.png", use_column_width=True)

    with open("qr.png", "rb") as f:
        st.download_button(
            data=f,
            label="Download QR Code",
            file_name="qr.png",
            mime="image/png",
        )
else:
    st.text("QR Code will be generated here!")
