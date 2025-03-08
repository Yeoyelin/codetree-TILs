#include <stdio.h>

int main() {
    int a = 5, b = 6, c =7;
    int temp1;
    int temp2;
    temp1 = b;
    temp2 = c;
    b = a;
    c = temp1;
    a = temp2;

    printf("%d\n%d\n%d", a, b, c);

    return 0;
}