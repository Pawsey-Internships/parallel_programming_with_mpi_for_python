---
title: "John Conway's Game of Life"
weight: 3
---

![Animated GIF of the Game of Life](game_of_life.gif)

```python
import numpy as np
from scipy import signal
from PIL import Image

def game_step(u):

    kernel = np.ones((3,3), dtype = int)
    kernel[1,1] = 0


    m = u.shape[0]
    n = u.shape[1]

    u_old = u.copy()

    neighbours = signal.convolve(u, kernel, mode='same')
    
    for i in range(m):
        for j in range(n):
            if u_old[i,j] == 1:
                if neighbours[i,j] < 2:
                    u[i,j] = 0
                elif neighbours[i,j] > 3:
                    u[i,j] = 0
            else:
                if neighbours[i,j] == 3:
                    u[i,j] = 1

    return u, u.sum()

total_steps = 1000

rows = 128
columns = 128

game_board = np.random.choice(
        np.array([0,1], dtype = int),
        size=(rows,columns), p = [0.7,0.3])

current_population = game_board.sum()

current_step = 1

images = []

while (current_step < total_steps) or (current_population == 0):
    
    game_board, current_population = game_step(game_board)
    current_step += 1

    image = Image.fromarray(np.uint8(game_board*255))
    images.append(image)

images[0].save("animation.gif", save_all = True, append_images = images[1:])
```





