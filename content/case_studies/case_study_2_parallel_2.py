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

N_images = len(image_paths)//size

start_index = rank*N_images
end_index = (rank + 1) * N_images + 1

end_index = len(image_paths) if (rank == size - 1) else end_index

for path in image_paths[start_index:end_index]:
    image = Image.open(path)
    resized_image = image.resize((64, 64))
    resized_image.save(f'resized_images/{os.path.basename(path[:-4])}.png')

