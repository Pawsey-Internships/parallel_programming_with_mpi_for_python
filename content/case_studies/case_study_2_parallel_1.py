from glob import glob
import os
from PIL import Image
from mpi4py import MPI
import numpy as np

COMM = MPI.COMM_WORLD
rank = COMM.Get_rank()
size = COMM.Get_size()

output_path = "resized_images"

if rank == 0:
        if not os.path.exists(output_path):
            os.mkdir("resized_images")

        image_paths = glob("images/*.jpg")
        paths_to_scatter = [image_paths[i::size] for i in range(size)]
else: 
        paths_to_scatter = None

scattered_image_paths = COMM.scatter(paths_to_scatter, root = 0)


for path in scattered_image_paths:
    image = Image.open(path)
    resized_image = image.resize((64, 64))
    resized_image.save(f'resized_images/{os.path.basename(path[:-4])}.png')

