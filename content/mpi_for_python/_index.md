---
title: "MPI for Python"
chapter: true
weight: 3
pre: "<b>2. </b>"
---
# 3. MPI For Python

* The MPI standard specifies a C and Fortran Interface.
* But there are bindings to other languages, including Julia, Python, C++ R...
* MPI for Python (`mpi4py`) provides python bindings to an underlying MPI library (such as OpenMPI or MPICH).
* Designed to work efficiently with NumPy arrays (it can also send Python objects).

## Hello MPI

```python
from mpi4py import MPI
COMM = MPI.COMM_WORLD

size = COMM.Get_size()
rank = COMM.Get_rank()

print(f'Hello from rank {rank} of {size}.')
```

* `MPI.COMM_WORLD` is the default **MPI communicator**.
* An **MPI communicator** is a collection of processes that can communicate with each other by message passing.
* `COMM.Get_size()` and `COMM.Get_rank()` methods give the number of processes in the communicator and the labelling of each process in that communicator.

## Running MPI Programs

* The standard command to launch an MPI program is `mpiexec` or `mpirun`, for instance:

```bash
mpiexec -N 4 python my_program.py
```

* Where `-N 4` specifies the number of MPI processes.
* On systems using Slurm  (like Setonix or Topaz), the equivalent command is:

```bash
srun -N 1 -n 4 python my_program.py
```

* Where `-N 1` specifies the number of compute nodes and `-n 4` specifies the number of MPI processes.
* Try running the above code with more than one MPI process a few times. What do you observe? 
