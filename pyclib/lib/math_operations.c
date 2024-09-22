#include "math_operations.h"
#include <errno.h>
#include <math.h>

EXPORT double add_doubles(double a, double b) {
    return a + b;
}

EXPORT double subtract_doubles(double a, double b) {
    return a - b;
}

EXPORT double multiply_doubles(double a, double b) {
    return a * b;
}

EXPORT double divide_doubles(double a, double b) {
    if (b == 0) {
        errno = EDOM;  // Set error number for domain error
        return INFINITY;  // Return infinity for division by zero
    }
    return a / b;
}
