//Обчислення членiв ряду i суми на рекурсивному поверненнi
#include <stdio.h>
#include <math.h>

typedef struct {
    double element;
    double sum;
} Result;

double calculateF1(double x) {
    return x / pow(0.525 + 0.5 * x, 2) - 1;
}

Result recReturn(int i, int n, double x, double F1) {
    Result result;
    
    if (i == 1) {
        result.element = F1;
        result.sum = F1;
        return result;
    }
    
    Result prev = recReturn(i - 1, n, x, F1);

    return result;
}

double sumSeries2(int n, double x) {
    double F1 = calculateF1(x); 
    Result result = recReturn(n, n, x, F1);
    return result.sum;
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
    double result = sumSeries2(n, x);
    printf("Result: %.10f\n", result);

    return 0;
}
