#ifndef MATH_OPERATIONS_H
#define MATH_OPERATIONS_H

#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#else
    #define EXPORT
#endif

// Function to add two double precision floats
EXPORT double add_doubles(double a, double b);

// Function to subtract two double precision floats
EXPORT double subtract_doubles(double a, double b);

// Function to multiply two double precision floats
EXPORT double multiply_doubles(double a, double b);

// Function to divide two double precision floats
EXPORT double divide_doubles(double a, double b);

#endif // MATH_OPERATIONS_H