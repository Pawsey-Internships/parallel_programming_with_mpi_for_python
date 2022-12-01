---
title: "Case Studies"
chapter": true
weight: 5
pre: "<b>5. </b>"
katex: true
math: 'mmark'
---

* In this section, we'll explore how MPI for Python can be used to parallel pre-existing projects.
* I'd like to hear your suggestions!

## Parallel Speedup

For a program working on a problem of fixed size, the parallel **speedup** is defined as:

$$ \text{speedup} = \frac{\text{time}_1}{\text{time}_N}$$

Where $\text{time}_1$ is the program wall time with one MPI process and $\text{N}_N$ is the program wall time with $N$ MPI processes.

The `time` command gives a measure of the program wall time, for instance:

    time mpiexec -N 4 python my_mpi_program.py

The wall time will be reported as the `real` time.

The wall time of a program will vary slightly. To get a good measure of the speedup, it's best to take the average of several repeats. In the following three case studies, the reported wall time and speedup is the average of 10 repeats (run on a desktop PC with 3.2 GHz CPU cores).
