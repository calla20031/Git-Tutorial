#include <stdio.h>

int main(void) 
{
    double km, mile;

    // 사용자로부터 킬로미터 값을 입력 받음
    printf("Please enter kilometers: ");
    scanf("%lf", &km);

    // 킬로미터를 마일로 변환
    mile = km / 1.609;

    // 결과를 소수점 첫째 자리까지 출력
    printf("%.1lf km is equal to %.1lf miles.\n", km, mile);

    return 0;
}

