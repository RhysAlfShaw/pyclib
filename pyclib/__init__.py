import ctypes
import os
import sys
import numpy as np


# Add the bin directory to the system path
bin_dir = os.path.join(os.path.dirname(__file__), "bin")
sys.path.append(bin_dir)

# Load the shared library
if os.name == "posix":
    if sys.platform == "darwin":
        lib = ctypes.CDLL(
            os.path.join(bin_dir, "libmath_operations.dylib")
        )  # For macOS
    else:
        lib = ctypes.CDLL(os.path.join(bin_dir, "libmath_operations.so"))  # For Linux
elif os.name == "nt":
    lib = ctypes.CDLL(os.path.join(bin_dir, "math_operations.dll"))  # For Windows
else:
    raise OSError("Unsupported operating system")

# Define the argument and return types of the functions
lib.add_doubles.argtypes = [ctypes.c_double, ctypes.c_double]
lib.add_doubles.restype = ctypes.c_double

lib.subtract_doubles.argtypes = [ctypes.c_double, ctypes.c_double]
lib.subtract_doubles.restype = ctypes.c_double

lib.multiply_doubles.argtypes = [ctypes.c_double, ctypes.c_double]
lib.multiply_doubles.restype = ctypes.c_double

lib.divide_doubles.argtypes = [ctypes.c_double, ctypes.c_double]
lib.divide_doubles.restype = ctypes.c_double

lib.dot_product.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
]
lib.dot_product.restype = ctypes.c_double

lib.vector_length.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.vector_length.restype = ctypes.c_double

lib.mat_mult.argtypes = [
    ctypes.POINTER(ctypes.c_double),  # A
    ctypes.POINTER(ctypes.c_double),  # B
    ctypes.POINTER(ctypes.c_double),  # C
    ctypes.c_int,  # m (rows of A)
    ctypes.c_int,  # n (columns of A / rows of B)
    ctypes.c_int,  # p (columns of B)
]

lib.mat_mult.restype = None  # No return value (void)


class cmath:
    """
    Python wrapper for the C math_operations library.
    """

    def add(a, b):
        # check if the input is float
        if not isinstance(a, float) or not isinstance(b, float):
            # convert the input to float
            a = float(a)
            b = float(b)
        # call the C function
        return lib.add_doubles(a, b)

    def subtract(a, b):
        # check if the input is float
        if not isinstance(a, float) or not isinstance(b, float):
            # convert the input to float
            a = float(a)
            b = float(b)
        # call the C function
        return lib.subtract_doubles(a, b)

    def multiply(a, b):
        # check if the input is float
        if not isinstance(a, float) or not isinstance(b, float):
            # convert the input to float
            a = float(a)
            b = float(b)
        # call the C function
        return lib.multiply_doubles(a, b)

    def divide(a, b):
        # check if the input is float
        if not isinstance(a, float) or not isinstance(b, float):
            # convert the input to float
            a = float(a)
            b = float(b)
        # call the C function
        return lib.divide_doubles(a, b)

    # Python wrapper function
    def dot_1d(a, b):
        """
        Wrapper for the C dot_product function.

        Args:
            a (numpy.ndarray): First array of doubles.
            b (numpy.ndarray): Second array of doubles.

        Returns:
            float: Dot product of arrays a and b.
        """
        if len(a) != len(b):
            raise ValueError("Arrays must have the same length")

        n = len(a)

        # Call the C function using ctypes
        result = lib.dot_product(
            a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            ctypes.c_int(n),
        )

        return result

    def vector_length(a):
        n = len(a)
        a = a.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
        return lib.vector_length(a, ctypes.c_int(n))

    def mat_mul(a, b):

        if a.shape[1] != b.shape[0]:
            raise ValueError("Matrix A's columns must be equal to Matrix B's rows")

        # Get the dimensions of the matrices
        m, n = a.shape
        p, q = b.shape

        # Convert the matrices to 1D arrays
        a = np.ascontiguousarray(a, dtype=np.float64)
        b = np.ascontiguousarray(b, dtype=np.float64)
        c = np.zeros((m, q), dtype=np.float64)
        # Call the C function using ctypes
        lib.mat_mult(
            a.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            b.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            c.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            ctypes.c_int(m),
            ctypes.c_int(n),
            ctypes.c_int(p),
        )

        return c
