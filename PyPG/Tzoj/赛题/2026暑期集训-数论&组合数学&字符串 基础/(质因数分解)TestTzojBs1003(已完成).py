from math import *  

#判断素数 （埃拉托斯特尼筛法）
def IsP(n):
    is_p=[True]*(n+1)
    is_p[0]=is_p[1]=False
    for i in range(2,isqrt(n)+1):
        if is_p[i]:
            for j in range(i*i,n+1,i):
                is_p[j]=False
    return [i  for i,prime in enumerate(is_p) if prime]

#运用勒让德原理求阶乘质因数分解
def factorial_prime_factors(n):
    factors={}
    for p in IsP(n):
        count=0
        p_2=p
        while p_2<=n:
            count+=n//p_2
            p_2*=p
        factors[p]=count    
    return factors

n=int(input())
result=factorial_prime_factors(n)
for p,c in result.items():
    print(p,c)