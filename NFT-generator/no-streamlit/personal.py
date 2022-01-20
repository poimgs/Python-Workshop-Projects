import os
import random
from PIL import Image


def get_face_parts(face_parts_dir):
    """
    Get all face parts from face_parts_dir
    """
    # Instantiate dictionary to store key-value pair of face parts to list of paths of images for face part
    face_parts = {}

    # Get path to directories of face parts (ears, mouths, etc)
    for face_part in os.listdir(face_parts_dir):
        face_part_path = os.path.join(face_parts_dir, face_part)

        # Get paths to all images in each directory
        face_part_images = []
        for face_part_image in os.listdir(face_part_path):
            face_part_image_path = os.path.join(face_part_path, face_part_image)
            face_part_images.append(face_part_image_path)
        
        # Update dictionary so that each face part points to a list of paths of images
        face_parts[face_part] = face_part_images

    return face_parts


def create_composite_image(face_parts, composite_image_dir, num):
    """
    Create a composite image from face_parts
    """
    # Path to save composite image
    composite_image_name = f'composite_image_{num}.png'
    composite_image_path = os.path.join(composite_image_dir, composite_image_name)

    # Create a new image 
    composite_image = Image.new('RGBA', (500, 500))

    # Take a random choice for each face part and "paste" them onto the new composite image
    random_face = Image.open(random.choice(face_parts['face']))
    random_hair = Image.open(random.choice(face_parts['hair']))
    random_ears = Image.open(random.choice(face_parts['ears']))
    random_eyes = Image.open(random.choice(face_parts['eyes']))
    random_nose = Image.open(random.choice(face_parts['nose']))
    random_mouth = Image.open(random.choice(face_parts['mouth']))

    composite_image.paste(random_face, (0, 0), random_face)
    composite_image.paste(random_hair, (0, 0), random_hair)
    composite_image.paste(random_ears, (0, 0), random_ears)
    composite_image.paste(random_eyes, (0, 0), random_eyes)
    composite_image.paste(random_nose, (0, 0), random_nose)
    composite_image.paste(random_mouth, (0, 0), random_mouth)

    # Save image
    composite_image.save(composite_image_path)


def main():
    """
    Main function
    """
    face_parts_dir = 'face_parts'
    composite_image_dir = 'composite_images'

    if not os.path.exists(composite_image_dir):
        os.mkdir(composite_image_dir)

    face_parts = get_face_parts(face_parts_dir)

    for i in range(1, 101):
        create_composite_image(face_parts, composite_image_dir, i)


if __name__ == '__main__':
    main()
