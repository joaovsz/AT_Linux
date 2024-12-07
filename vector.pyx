# distutils: language = c++
# cython: boundscheck=False, wraparound=False, initializedcheck=False

from cython.parallel import prange
from libc.stdlib cimport malloc, free
from cython.parallel cimport parallel
from cython.parallel cimport threadid

def vector_by_scalar(double[:] vector, double scalar):
    """
    Multiplica um vetor por um escalar usando OpenMP.
    """
    cdef int n = vector.shape[0]
    cdef int i
    cdef double[:] result = vector[:]
    
    with nogil, parallel():
        for i in prange(n):
            result[i] = vector[i] * scalar
    return result

