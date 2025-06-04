//Обчислення членiв ряду на рекурсивному спуску, а обчислення суми - на рекурсивному поверненні.
#include <stdio.h>
#include <math.h>

double calculateF1(double x) {
    return x / pow(0.525 + 0.5 * x, 2) - 1;
}

double recMixed(int i, int n, double x, double F1, double prev_element) {
    double F_i;
    
    if (i == 1) {
        F_i = F1;
    } else {
        F_i = prev_element * F1 * (3.0 - 2.0 * (i - 1)) / (2.0 * (i - 1));
    }
    
    if (i == n) {
        return F_i;
    }
    
    return F_i + recMixed(i + 1, n, x, F1, F_i);
}

double sumSeries3(int n, double x) {
    double F1 = calculateF1(x);
    return recMixed(1, n, x, F1, 0);
}

int main() {
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    double x;
    printf("Enter x: ");
    scanf("%lf", &x);

    if (n < 1 || x >= 1 || x <= 0.5) {
        printf("Incorrect input (n >= 1, 0.5 < x < 1)\n");
        return 1;
    }
    double result = sumSeries3(n, x);
    printf("Result: %.10f\n", result);

    return 0;
}
