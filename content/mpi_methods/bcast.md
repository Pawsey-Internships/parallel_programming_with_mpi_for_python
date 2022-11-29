---
title: "Bcast"
weight: 3
---

* Bcast (broadcast) sends data at a root process to all other processes in the MPI communicator.
* It is an example of collective communication as it involves all processes in a communicator.

```python
from mpi4py import MPI
import numpy as np

COMM = MPI.COMM_WORLD
rank = COMM.Get_rank()

array = np.empty(2, dtype = np.float64)

if rank == 0:
    array = np.array([1, 2], dtype = np.float64)
    print(array, flush = True)

COMM.Bcast([array, MPI.DOUBLE], root = 0)

print(f'Received {array} at rank {rank}.')
```
