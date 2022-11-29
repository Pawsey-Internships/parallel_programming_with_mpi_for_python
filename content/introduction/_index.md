---
title: "What is MPI?"
chapter: true
weight: 2
pre: "<b>2. </b>"
---
# 2. What is MPI?

* The Message Passing Interface (MPI) API provides a framework for writing parallel programs following a Multiple Instruction Multiple Data (MIMD) model.
* It is the defacto-standard for distributed memory computing.
* There are several open-source implementations of MPI, the most popular are OpenMPI and MPICH.
* Multiple programs run simultaneously and send information to each other by message passing.
* Each program has a separate name space (no shared variables) and memory allocation (no shared memory).
* This allows MPI programs to run on distributed systems (i.e. supercomputers).

