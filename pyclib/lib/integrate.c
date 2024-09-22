#include <stdio.h>
#include "integrate.h"

// Function prototypes

// Example function to integrate

double example_function(double x) {
    return x * x; // f(x) = x^2
}

int test_integrate() {
    double a = 0.0;
    double b = 1.0;
    int n = 1000;

    double result_trapezoidal = trapezoidal_rule(example_function, a, b, n);
    double result_simpsons = simpsons_rule(example_function, a, b, n);

    printf("Trapezoidal Rule: %f\n", result_trapezoidal);
    printf("Simpson's Rule: %f\n", result_simpsons);

    return 0;
}

// Trapezoidal Rule
double trapezoidal_rule(double (*f)(double), double a, double b, int n) {
    double h = (b - a) / n;
    double sum = 0.5 * (f(a) + f(b));

    for (int i = 1; i < n; i++) {
        double x = a + i * h;
        sum += f(x);
    }

    return sum * h;
}

// Simpson's Rule
double simpsons_rule(double (*f)(double), double a, double b, int n) {
    if (n % 2 != 0) {
        n++; // Simpson's rule requires an even number of intervals
    }

    double h = (b - a) / n;
    double sum = f(a) + f(b);

    for (int i = 1; i < n; i++) {
        double x = a + i * h;
        if (i % 2 == 0) {
            sum += 2 * f(x);
        } else {
            sum += 4 * f(x);
        }
    }

    return sum * h / 3.0;
}