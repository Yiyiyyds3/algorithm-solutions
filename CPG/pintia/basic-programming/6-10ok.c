#include <stdio.h>

void Print_Factorial ( const int N );

int main()
{
    int N;
    
    scanf("%d", &N);
    Print_Factorial(N);
    return 0;
}

/* 你的代码将被嵌在这里 */
void Print_Factorial ( const int N )
{
    if (N < 0) {
        printf("Invalid input");
        return;
    }
    if (N == 0 || N == 1) {
        printf("1");
        return;
    }

    int digits[3000] = {0};  // 足够存储1000!
    digits[0] = 1;
    int len = 1;

    for (int i = 2; i <= N; i++) {
        int carry = 0;
        for (int j = 0; j < len; j++) {
            int product = digits[j] * i + carry;
            digits[j] = product % 10;
            carry = product / 10;
        }
        while (carry > 0) {
            digits[len] = carry % 10;
            carry /= 10;
            len++;
        }
    }
    for (int i = len - 1; i >= 0; i--) {
        printf("%d", digits[i]);
    }
    printf("\n");
    return;
}