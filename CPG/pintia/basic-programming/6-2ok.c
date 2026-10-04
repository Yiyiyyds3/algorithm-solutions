#include <stdio.h>
#define MAXN 10

double f( int n, double a[], double x );

int main()
{
    int n, i;
    double a[MAXN], x;
    
    scanf("%d %lf", &n, &x);
    for ( i=0; i<=n; i++ )
        scanf("%lf", &a[i]);
    printf("%.1f\n", f(n, a, x));
    return 0;
}

/* 你的代码将被嵌在这里 */
/*精度不够
double pow(double x, int i)
{
    int flag=1;
    while(flag<i)
    {
        x*=x;
        flag++;
    }
    return x;
}
double f( int n, double a[], double x )
{
    int count=0;
    for(int i=0; i<=n; i++)
    {
        count += a[i]*pow(x,i);
    }
    return count;
}*/

/*太慢了
double f( int n, double a[], double x )
{
    double sum=0;
    for(int i=0; i<=n; i++)
    {
        double temp=1;
        for(int j=1; j<=i; j++)
        {
            temp*=x;
        }
        sum += a[i]*temp;
    }
    return sum;
}*/

double fast_pow(double x, int i)
{
    if(i==0)return 1.0;
    if(i==1)return x;
    double half=fast_pow(x,i/2);
    if(i%2==0){
        return half*half;
    }
    else{
        return half*half*x;
    }
}
double f( int n, double a[], double x )
{
    double sum=0;
    for(int i=0; i<=n; i++)
    {
        sum += a[i]*fast_pow(x,i);
    }
    return sum;
}