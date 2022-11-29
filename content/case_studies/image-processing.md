---
title: "Image Processing"
weight: 2
---

For this case-study we'll use [a subset of the Oxford-IIIT Pet dataset](./../images.zip) [1].

```python
from glob import glob
import os
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

[1] [The Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)
