#include <stdio.h>

int main() {
    double ft = 30.48;
    int mile = 160934;
    double nine = ft * 9.2;
    double one = 1.3 * mile;
    printf("9.2ft = %.1lfcm\n1.3mi = %.1lfcm", nine, one);
    return 0;
}