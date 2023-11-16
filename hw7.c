#include <stdio.h>

void swapArrays(int* ptr1, int* ptr2, int size) {
    for (int i = 0; i < size; i++) {
        int temp = *(ptr1 + i);
        *(ptr1 + i) = *(ptr2 + i);
        *(ptr2 + i) = temp;
    }
}

int main() {
    int arr1[] = { 1, 2, 3, 4, 5, 6 };
    int arr2[] = { 7, 8, 9, 10, 11, 12 };
    int size = sizeof(arr1) / sizeof(arr1[0]);

    printf("arr1: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\n");
    printf("arr2: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr2[i]);
    }
    printf("\n");
    printf("\n");

    swapArrays(arr1, arr2, size);

    printf("after swap\n");
    printf("arr1: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr1[i]);
    }
    printf("\n");
    printf("arr2: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", arr2[i]);
    }
    printf("\n");

    return 0;
}
