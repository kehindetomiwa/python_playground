import time
import numpy as np
import multiprocessing
from joblib import delayed, Parallel, parallel_backend

cores = multiprocessing.cpu_count() - 1
# size = [101, 1001, 10001, 20001, 30001, 40001, 50001]
size = [20001, 30001, 40001, 50001]
rep = [0] * len(size)
z = 0


def Prim(i):
    chech_vec = list(range(2, (i)))
    P = np.mod(i, chech_vec)
    if any(P == 0):
        return "n"
    else:
        return "y"


# Changing the inner_max_num_threads does not matter. Furthermore, for this task a backend ="threading" is even slower.
for j in size:
    start = time.time()
    if __name__ == "__main__":
        # with parallel_backend("loky", inner_max_num_threads=2):
        with parallel_backend('threading'):
            PrimNum = Parallel(n_jobs=cores)(delayed(Prim)(i) for i in range(3, j))
    end = time.time()
    rep[z] = end - start
    z += 1

z = 0
for j in size:
    PrimNum = [0] * j
    start = time.time()
    for i in range(3, j):
        PrimNum[i] = Prim(i)
    end = time.time()
    rep[z] = end - start
    z += 1
