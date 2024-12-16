# vector.pyx
# cython: boundscheck=False, wraparound=False, cdivision=True
import cython
from cython.parallel import prange
import numpy as np
cimport numpy as cnp

@cython.boundscheck(False)
@cython.wraparound(False)
def vector_by_scalar(cnp.ndarray[cnp.double_t, ndim=1] vector, cnp.double_t scalar):
    cdef Py_ssize_t n = vector.shape[0]
    cdef cnp.ndarray[cnp.double_t, ndim=1] out = np.empty(n, dtype=np.float64)

    cdef double[:] v_mem = vector
    cdef double[:] o_mem = out

    cdef Py_ssize_t i

    # Loop paralelo
    # O nogil e o parallel já estão no contexto, não use nogil=True no prange
    with cython.nogil, cython.parallel.parallel():
        for i in prange(n, schedule='static'):
            o_mem[i] = v_mem[i] * scalar

    return out
