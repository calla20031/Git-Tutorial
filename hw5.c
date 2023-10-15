#include <stdio.h>

void solve(int n) {
    if (n > 1) {
        solve(n / 2);
    }
    printf("%d", n % 2);
}

int main() {
    int num;
    printf("Please enter a number: ");
    scanf("%d", &num);

    if (num == 0) {
        printf("0\n");
    }
    else 
    {
        solve(num);
        printf("\n");
    }

    return 0;
}
