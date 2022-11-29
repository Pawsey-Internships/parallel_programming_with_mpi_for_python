---
title: "Using MPI for Python"
chapter: true
weight: 4
pre: "<b>4. </b>"
---

# 4. Using MPI for Python

* MPI is a very rich API, and MPI for Python provides access to almost all of its features.
* It's easy to write a semester's worth of material on MPI, but it doesn't take much to get started.
* MPI methods (or directives) for message passing are either:
    * Point-to-Point: One MPI rank sends, and another receives. Only two processes are involved.
    * Collective: The entire MPI communicator is involved in the communication.
* These operations can be:
    * Blocking: The MPI processes pause until the communication is complete.
    * Non-Blocking: The MPI processes continue executing program instructions without waiting for communication to complete.
* Most of these methods send data between MPI processes. However, there are special *reduction* methods for performing simple mathematical or logical operations (e.g. summing array elements).
* This workshop introduces the most common blocking point-to-point and collective MPI methods.
