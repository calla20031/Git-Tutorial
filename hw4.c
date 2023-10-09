#include <stdio.h>
int main(void)
{
	int num,i, isPrime =1 ;

	printf("Please enter a number :");
	scanf("%d", &num);
	for (i = 2; i*i <= num; i++)
	{
		if (num % i == 0)
		{
			isPrime = 0;
			break;
		}
	}

	if (isPrime)
	{
		printf("It is a prime number.");
	}
	else
	{
		printf("It is not a prime number.");
	}
	return 0;
}