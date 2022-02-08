import streamlit as st
from PIL import Image
from itertools import product
from zipfile import ZipFile
import random
import os
import shutil


def create_random_composite_image(layer_images):
    composite_image = Image.new("RGBA", (500, 500))

    for layer in layer_images:
        random_choice = Image.open(random.choice(layer))
        composite_image.paste(random_choice, (0, 0), random_choice)

    st.image(composite_image)


def create_NFT_folder():
    if os.path.exists("NFT-collection"):
        shutil.rmtree("NFT-collection")
    os.mkdir("NFT-collection")


def create_all_composite_iamges(layer_images):
    all_combinations = [p for p in product(*layer_images)]
    # st.write(all_combinations)
    for i, combinations in enumerate(all_combinations):
        composite_image = Image.new("RGBA", (500, 500))

        for layer in combinations:
            image = Image.open(layer)
            composite_image.paste(image, (0, 0), image)

            composite_image.save(f"NFT-collection/{i+1}.png")


def zip_NFT_collection():
    with ZipFile("NFT-collection.zip", "w") as zip:
        for root, dirs, files in os.walk("NFT-collection"):
            for file in files:
                zip.write(os.path.join(root, file))
