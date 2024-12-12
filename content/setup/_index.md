---
title:  "Setup for the Workshop"
chapter: true
weight:  1
pre: "<b>1. </b>"
---

# 1. Setup for the Workshop.

To follow along with the session, you'll need access to a computer with an MPI installation, Python 3 and, the python packages mpi4py, numpy, scipy, PIL and matplotlib. This could be through your allocation with Pawsey or your own PC.

## Setonix

```bash
module load python/3.11.6
module load py-numpy/1.26.1
module load py-mpi4py/3.1.5-py3.11.6
module load py-scipy/1.11.3
```

## MacOS 

With the homebrew package manager installed:

```bash
brew install open-mpi
pip3 install numpy scipy pillow
brew install mpi4py
```

## Windows

With the Window's Subsystem for Linux Installed and Ubuntu chosen as your Linux distribution, follow the instructions for Linux (Ubuntu) below.

## Linux (Ubuntu): 

Using the 'apt' package manager on which you have 'superuser' privileges (this will be the case if you are using your own laptop or an instance on Nimbus).

```bash
sudo apt install libopenmpi-dev python3-pip
python3 -m pip install setuptools cython 
python3 -m pip install numpy mpi4py scipy matplotlib
```


