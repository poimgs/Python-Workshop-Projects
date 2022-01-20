"""
# NFT generator: Generate images from smaller image components
face_parts:
- ears: 
    - ears/ears1.png
    - ears/ears2.png
- eyes:
    - eyes/eyes1.png
    - eyes/eyes2.png
- face:
    - face/face1.png
    - face/face2.png
- hair:
    - hair/hair1.png
    - hair/hair2.png
- mouth:
    - mouth/mouth1.png
    - mouth/mouth2.png
- nose:
    - nose/nose1.png
    - nose/nose2.png

1. Randomly choose from face_parts, one face part
2. Using chosen face parts, create one composite image
3. Save composite image
"""

import os
import random
import shutil

from PIL import Image


def get_face_parts(face_parts_dir):
    """
    Get all face parts from face_parts_dir
    """
    face_parts = {}
    for face_part in os.listdir(face_parts_dir):
        face_part_path = os.path.join(face_parts_dir, face_part)
        face_part_images = []
        for face_part_image in os.listdir(face_part_path):
            face_part_image_path = os.path.join(
                face_part_path, face_part_image)
            face_part_images.append(face_part_image_path)
        face_parts[face_part] = face_part_images
    return face_parts


def create_composite_image(face_parts, face_parts_dir, composite_image_dir):
    """
    Create a composite image from face_parts
    """
    composite_image_name = 'composite_image.png'
    composite_image_path = os.path.join(
        composite_image_dir, composite_image_name)
    composite_image = Image.new('RGBA', (500, 500))
    for face_part in face_parts:
        face_part_image_path = random.choice(face_parts[face_part])
        face_part_image = Image.open(face_part_image_path)
        composite_image.paste(face_part_image, (0, 0), face_part_image)
    composite_image.save(composite_image_path)


def main():
    """
    Main function
    """
    face_parts_dir = 'face_parts'
    composite_image_dir = 'composite_images'
    if os.path.exists(composite_image_dir):
        shutil.rmtree(composite_image_dir)
    os.mkdir(composite_image_dir)
    face_parts = get_face_parts(face_parts_dir)
    create_composite_image(face_parts, face_parts_dir, composite_image_dir)


if __name__ == '__main__':
    main()
