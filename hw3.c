#include <stdio.h>
int main(void)
{
	int i,j,k;
    for (int i = 0; i < 5; i++) 
    {
        for (int j = 0; j < 5 - i - 1; j++) 
        {
            printf(" ");
        }
        for (int k = 0; k < 2 * i + 1; k++) 
        {
            printf("*");
        }
        printf("\n");
	}
	return 0;

}