---
title: "Gather"
weight: 5
---

* Gather is the 'inverse' of Scatter.
* It collects smaller arrays at each MPI process into a larger array at a designated root process.
* Gather assumes that the sending arrays are the same size at each MPI process.

```python
from mpi4py import MPI
import numpy as np

COMM = MPI.COMM_WORLD
rank = COMM.Get_rank()
size = COMM.Get_size()

send_array = np.array(2*[rank], dtype = np.float64)
print(f'Gathering {send_array} from {rank}.', flush = True)

if rank == 0:
    recv_array = np.empty(2 * size, dtype = np.float64)
else:
    recv_array = None

COMM.Gather(
    [send_array, MPI.DOUBLE],
    [recv_array, MPI.DOUBLE],
    root = 0)

if rank == 0:
    print(f'Received {recv_array} at rank {rank}.')
```

