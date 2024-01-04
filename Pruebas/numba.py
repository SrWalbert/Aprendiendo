from numba import jit


@jit(nopython=True)
def func():
    pass
