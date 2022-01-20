import random
from PIL import Image


def create_composite_image(faces, hairs, ears, eyes, noses, mouths):
    """
    Create a composite image from face_parts
    """
    # Create a new image
    composite_image = Image.new('RGBA', (500, 500))

    # Take a random choice for each face part and "paste" them onto the new composite image
    random_face = Image.open(random.choice(faces))
    random_hair = Image.open(random.choice(hairs))
    random_ears = Image.open(random.choice(ears))
    random_eyes = Image.open(random.choice(eyes))
    random_nose = Image.open(random.choice(noses))
    random_mouth = Image.open(random.choice(mouths))

    composite_image.paste(random_face, (0, 0), random_face)
    composite_image.paste(random_hair, (0, 0), random_hair)
    composite_image.paste(random_ears, (0, 0), random_ears)
    composite_image.paste(random_eyes, (0, 0), random_eyes)
    composite_image.paste(random_nose, (0, 0), random_nose)
    composite_image.paste(random_mouth, (0, 0), random_mouth)

    # Save image
    return composite_image
