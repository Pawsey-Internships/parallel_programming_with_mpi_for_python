from glob import glob
from os import mkdir
from PIL import Image

output_path = "resized_images"
image_paths = glob("images/*.jpg")


if not os.path.exists(output_path):
    os.mkdir("resized_images")

for path in image_paths:
    image = Image.open(path)
    resized_image = image.resize((64, 64))
    resized_image.save(f'resized_images/{os.path.basename(path[:-4])}.png')

