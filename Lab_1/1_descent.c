//Обчислення членiв ряду  i суми на рекурсивному спуску
#include <stdio.h>
#include <math.h>

double calculateF1(double x) {
    return x / pow(0.525 + 0.5 * x, 2) - 1;
}
double recDescend(int i, int n, double x, double *sum, double F1, double prev_F) {
    double F_i;
    
    if (i == 1) {
        F_i = F1;
    } else {
        F_i = prev_F * F1 * (3.0 - 2.0 * (i - 1)) / (2.0 * (i - 1));
    }
    
    *sum += F_i;
    
    if (i == n) {
        return F_i;
    }
    return recDescend(i + 1, n, x, sum, F1, F_i);
}

double sumSeries1(int n, double x) {
    double sum = 0;
    double F1 = calculateF1(x);
    recDescend(1, n, x, &sum, F1, 0); 
    return sum;
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

    double result = sumSeries1(n, x);
    printf("Result: %.10f\n", result);
    return 0;
}
