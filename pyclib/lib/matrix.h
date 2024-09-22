#ifndef MATRIX_H
#define MATRIX_H

#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT
#endif

// dot product of two vectors
EXPORT double dot_product(double *a, double *b, int n);

// length of a vector
EXPORT double vector_length(double *a, int n);

// matrix multiplication
EXPORT void mat_mult(double *A, double *B, double *C, int m, int n, int p);

#endif // MATRIX_H