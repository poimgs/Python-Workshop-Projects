import streamlit as st
from PIL import Image
from itertools import product
from zipfile import ZipFile
import random
import os
import shutil

# Create a title and sub-title
st.title("NFT Generator")

# Check how many layers the user wants
layers = st.slider(
    "How many layers will each NFT image have?", 1, 10, 1,
    help="take note that subsequent layers will be layered over the previous ones!"
)

layer_images = []

for i in range(layers):
    images = st.file_uploader(
        f"Layer {i+1}",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
    )
    layer_images.append(images)

col1, col2 = st.columns(2)

random_clicked = col1.button("Generate a random NFT image")
collection_clicked = col2.button("Generate NFT collection")

if random_clicked:
    composite_image = Image.new("RGBA", (500, 500))

    for layer in layer_images:
        random_choice = Image.open(random.choice(layer))
        composite_image.paste(random_choice, (0, 0), random_choice)

    st.image(composite_image)

if collection_clicked:
    with st.spinner("Generating NFT collection..."):
        if os.path.exists("NFT-collection"):
            shutil.rmtree("NFT-collection")
        os.mkdir("NFT-collection")

        all_combinations = [p for p in product(*layer_images)]
        for i, combinations in enumerate(all_combinations):
            composite_image = Image.new("RGBA", (500, 500))

            for layer in combinations:
                image = Image.open(layer)
                composite_image.paste(image, (0, 0), image)

                composite_image.save(f"NFT-collection/{i+1}.png")

        with ZipFile("NFT-collection.zip", "w") as zip:
            for root, dirs, files in os.walk("NFT-collection"):
                for file in files:
                    zip.write(os.path.join(root, file))

        with open("NFT-collection.zip", "rb") as f:
            col2.download_button(
                data=f,
                label="Download NFT-collection.zip",
                file_name="NFT-collection.zip",
                mime="application/zip",
            )
