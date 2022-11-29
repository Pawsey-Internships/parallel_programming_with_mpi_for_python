---
title: "Scatter"
weight: 4
---

* Scatter is a collective method that distributes an array equally over all of the processes in an MPI communicator.
* The number of processes (the communicator size) must be a divisor of the array's length; otherwise, some of the ranks will receive zero elements.

```python
from mpi4py import MPI
import numpy as np

COMM = MPI.COMM_WORLD
rank = COMM.Get_rank()
size = COMM.Get_size()

recv_array = np.empty(2, dtype = np.float64)

if rank == 0:
    send_array = np.linspace(0, 2 * size, num = 2 * size, dtype = np.float64) 
else:
    send_array = None

COMM.Scatter(
    [send_array, MPI.DOUBLE],
    [recv_array, MPI.DOUBLE],
    root = 0)

print(f'Received {recv_array} at rank {rank}.')
```
