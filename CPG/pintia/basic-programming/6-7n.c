#include <stdio.h>
#include <math.h>

int IsTheNumber ( const int N );

int main()
{
    int n1, n2, i, cnt;
    
    scanf("%d %d", &n1, &n2);
    cnt = 0;
    for ( i=n1; i<=n2; i++ ) {
        if ( IsTheNumber(i) )
            cnt++;
    }
    printf("cnt = %d\n", cnt);

    return 0;
}

/* 你的代码将被嵌在这里 */
int IsTheNumber ( const int N )
{
    int sum=0;
    for(int i=1;i<=sqrt(N);i++)
    {
        if(N%i==0)
        {
            sum+=i;
            if(i!=N/i)
            {
                sum+=N/i;
            }
        }
    }
    if(sum==2*N)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}