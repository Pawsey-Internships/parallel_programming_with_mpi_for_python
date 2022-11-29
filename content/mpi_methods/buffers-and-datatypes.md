---
title: "Buffers and Data Types"
weight: 2
---

* Let's take a close look at the `Recv` method.

```python
COMM.Recv([recv_array, MPI.INT], source = 0)
```

* The `[recv_array, MPI.INT]` specifies an MPI 'buffer' and its datatype.
* It's important to pick the right data type. Otherwise, your data will become scrambled!
* For all MPI for Methods starting with a capital letter, the buffer is expected to be a NumPy array.

## An Incomplete Table of MPI for Python Datatypes

With `from mpi4py import MPI` and `import numpy as np`.

| **mpi4py Data Type** | **NumPy Data Type** | **Description**                        |
|----------------------|---------------------|----------------------------------------|
| MPI.REAL             | np.float32          | single-precision float point number    |
| MPI.DOUBLE           | np.float64          | double-precision floating point number |
| MPI.INT              | np.intc             | single-precision integer               |
| MPI.COMPLEX          | np.complex64        | single-precision complex number        |
| MPI.DOUBLE_COMPLEX   | np.complex128       | double-precision complex number        |
