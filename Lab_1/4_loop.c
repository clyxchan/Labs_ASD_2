//Циклічна програма вирішення задачі 
#include <stdio.h>
#include <math.h>

double calculateF1(double x) {
    return x / pow(0.525 + 0.5 * x, 2) - 1;
}
double sumSeriesLoop(int n, double x) {
    double sum = 0;
    double F1 = calculateF1(x);
    double F_i = F1;
    
    sum += F_i; 
    
    for (int i = 2; i <= n; i++) {
        F_i = F_i * F1 * (3 - 2 * (i - 1)) / (2 * (i - 1));
        sum += F_i;
    }
    
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

    double result = sumSeriesLoop(n, x);
    printf("Result: %.10f\n", result);
    return 0;
}
