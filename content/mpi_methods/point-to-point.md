---
title: "Send & Recv"
weight: 1
---
* The Send and Recv methods carry out point-to-point communication.
* Point-to-point communication transfers data between a sender and a receiver.
* Both processes will not proceed until the data is transferred.
* This enforces synchronisation.
* Pitfall: If the two processes can not complete the transfer, they will deadlock, and the parallel program will never complete.

```python

from mpi4py import MPI
import numpy as np

COMM = MPI.COMM_WORLD
rank = COMM.Get_rank()

if rank == 0:
    send_array = np.array(2*[rank], dtype = int)
else:
    recv_array = np.empty(2, dtype = int)

if rank == 0:
    COMM.Send([send_array, MPI.INT], dest = 1)
else:
    COMM.Recv([recv_array, MPI.INT], source = 0)

    print(recv_array)
```

## Spot the Bug

* What will happens if we replace the last if-statement with the code block below?

```python
if rank == 0:
    COMM.Send([send_array, MPI.INT], dest = 1)
else:
    COMM.Recv([recv_array, MPI.INT], source = 1)
```



