import numpy as np
from mpi4py import MPI


def mc_pi(N, COMM):

    hits = 0
    N_local = N // COMM.Get_size()
    for i in range(N_local):
        point = np.random.uniform(low=-1, high=1, size=2)
        if np.sqrt((point**2).sum()) < 1:
            hits += 1

    if COMM.Get_rank() == 0:
        Ns_array = np.empty(COMM.Get_size(), dtype=int)
    else:
        Ns_array = None

    hits = np.array([hits], dtype=int)

    COMM.Gather([hits, MPI.INT], [Ns_array, MPI.INT], root=0)

    if COMM.Get_rank() == 0:
        hits_global = np.sum(Ns_array)
        area = 4 * hits_global / N
    else:
        area = None

    return area


COMM = MPI.COMM_WORLD
rank = COMM.Get_rank()

np.random.seed(rank)

print(mc_pi(500000, COMM))
