import streamlit as st
from .personal import create_composite_image

# Create a title and sub-title
st.title("NFT Generator")
st.write("Create a new NFT with your own images!")

# Create upload buttons to upload images
faces = st.file_uploader(
    "Upload faces", 
    type=["png", "jpg", "jpeg"], 
    accept_multiple_files=True
)
hairs = st.file_uploader(
    "Upload hairs", 
    type=["png", "jpg", "jpeg"], 
    accept_multiple_files=True
)
ears = st.file_uploader(
    "Upload ears", 
    type=["png", "jpg", "jpeg"], 
    accept_multiple_files=True
)
eyes = st.file_uploader(
    "Upload eyes", 
    type=["png", "jpg", "jpeg"], 
    accept_multiple_files=True
)
noses = st.file_uploader(
    "Upload noses", 
    type=["png", "jpg", "jpeg"], 
    accept_multiple_files=True
)
mouths = st.file_uploader(
    "Upload mouths", 
    type=["png", "jpg", "jpeg"], 
    accept_multiple_files=True
)

# Create two columns for two buttons 
refresh_col, download_col = st.columns(2)

refresh = refresh_col.button('Click to generate a new image!')

# Generate NFT image if button clicked
if refresh:
    if faces and hairs and ears and eyes and noses and mouths:
        composite_image = create_composite_image(faces, hairs, ears, eyes, noses, mouths)
        st.image(composite_image)

        # Save image as png and provide download button to download NFT image
        composite_image.save('NFT.png')
        with open("NFT.png", "rb") as file:
            clicked = download_col.download_button("Download your NFT image", file, "NFT.png")
    else:
        st.write("Upload images for all components before generating!")