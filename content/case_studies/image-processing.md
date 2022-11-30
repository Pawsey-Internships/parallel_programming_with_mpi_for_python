---
title: "Image Processing"
weight: 2
---

For this case-study we'll use [a subset of the Oxford-IIIT Pet dataset](./../images.zip) [1].

```python
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
```

```python
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
```

```python
from glob import glob
from os import mkdir
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

end_index = len(image_paths) if rank == size - 1 else end_index

for path in image_paths[start_index:end_index]:
    image = Image.open(path)
    resized_image = image.resize((64, 64))
    resized_image.save(f'resized_images/{os.path.basename(path[:-4])}.png')
```

[1] [The Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)
