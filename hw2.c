#include <stdio.h>

int main(void) 
{
    double km, mile;

    // ����ڷκ��� ų�ι��� ���� �Է� ����
    printf("Please enter kilometers: ");
    scanf("%lf", &km);

    // ų�ι��͸� ���Ϸ� ��ȯ
    mile = km / 1.609;

    // ����� �Ҽ��� ù° �ڸ����� ���
    printf("%.1lf km is equal to %.1lf miles.\n", km, mile);

    return 0;
}

