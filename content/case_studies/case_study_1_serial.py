import numpy as np


def mc_pi(N):
    hits = 0
    for i in range(N):
        point = np.random.uniform(low=-1, high=1, size=2)
        if np.sqrt((point**2).sum()) < 1:
            hits += 1
    return 4 * hits / N


print(mc_pi(1000000))
