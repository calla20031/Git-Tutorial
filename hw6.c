#include <stdio.h>

int main() {
    int numbers[5];
    int odd_numbers[5], even_numbers[5];
    int odd_count = 0, even_count = 0;

    printf("Please input five integers: ");

    for (int i = 0; i < 5; ++i) {
        scanf("%d", &numbers[i]);
    }

    for (int i = 0; i < 5; ++i) {
        if (numbers[i] % 2 == 0) {
            even_numbers[even_count] = numbers[i];
            even_count++;
        }
        else {
            odd_numbers[odd_count] = numbers[i];
            odd_count++;
        }
    }

    printf("Odd numbers:");
    for (int i = 0; i < odd_count; ++i) {
        printf(" %d", odd_numbers[i]);
    }

    printf("\nEven numbers:");
    for (int i = 0; i < even_count; ++i) {
        printf(" %d", even_numbers[i]);
    }

    return 0;
}
