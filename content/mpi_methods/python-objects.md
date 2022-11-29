---
title: "Communicating Python Objects"
weight: 6
---

* MPI for Python has specific methods for sending a receiving Python objects (i.e. stuff that is not data in a NumPy array).
* These commands are handy but much slower than working with NumPy arrays.
* A common use case for these methods is the communication of scalar values:

```python
from mpi4py import MPI
import numpy as np

COMM = MPI.COMM_WORLD
rank = COMM.Get_rank()

if rank == 0:
    x = 3.14
else:
    x = None

x = COMM.bcast(x, root = 0)

print('Broadcst {x} to rank {rank}.')

```

* Note that `bcast` starts with a lowercase letter and returns the value of `x` like a 'normal' Python function.
* Lowercase methods are passed the python objects directly, not as a [buffer, datatype] pair.



