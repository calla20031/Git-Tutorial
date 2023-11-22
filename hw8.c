#include <stdio.h>
#include <math.h>

double pow(double a, double b)
{
	b = a * a;
	return a;
}

int main(void)
{
	int n1, n2, n3, n4, n5;
	double square_ave, ave, ave_square, var,sta;
	printf("Enter 5 real numbers: ");
	scanf("%d %d %d %d %d", &n1, &n2, &n3, &n4, &n5);

	//ºĞ»ê = (Á¦°öÀÇ Æò±Õ - Æò±ÕÀÇ Á¦°ö)¿¡ ·çÆ®

	//Á¦°öÀÇ Æò±Õ ±¸ÇÏ±â
	square_ave = (n1 * n1 + n2 * n2 + n3 * n3 + n4 * n4 + n5 * n5) / 5;

	ave = (n1 + n2 + n3 + n4 + n5) / 5;
	ave_square = ave * ave;

	var = square_ave - ave_square;

	sta = sqrt(var);
	printf("Standard Deviation = %.3f", sta);
	return 0;

}