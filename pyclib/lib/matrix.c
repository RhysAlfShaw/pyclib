#include "matrix.h"
#include <math.h>
#include <stdlib.h>

// dot product of two arrays of doubles of any length
EXPORT double dot_product(double *a, double *b, int n) {
    double result = 0;
    for (int i = 0; i < n; i++) {
        result += a[i] * b[i];
    }
    return result;
}

// length of an array of doubles of any length
EXPORT double vector_length(double *a, int n) {
    double result = 0;
    for (int i = 0; i < n; i++) {
        result += a[i] * a[i];
    }
    return sqrt(result);
}

// Matrix multiplication function
// A[m x n] * B[n x p] = C[m x p]
// Assumes that A, B, and C are flat 1D arrays stored in row-major order.
void mat_mult(double *A, double *B, double *C, int m, int n, int p) {
    // Initialize matrix C to zero
    for (int i = 0; i < m * p; i++) {
        C[i] = 0.0;
    }

    // Perform matrix multiplication
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            for (int k = 0; k < n; k++) {
                C[i * p + j] += A[i * n + k] * B[k * p + j];
            }
        }
    }
}

