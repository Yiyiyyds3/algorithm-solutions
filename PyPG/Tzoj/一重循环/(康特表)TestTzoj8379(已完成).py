from math import sqrt
#提高精度使用整数除法实现向下取整
def get_k_robust(n):
    k = int(sqrt(2 * n))
    while (k - 1) * k // 2 >= n:
        k -= 1
    while k * (k + 1) // 2 < n:
        k += 1
    return k
n=int(input())
k=get_k_robust(n)
s=t_1=(k*(k-1))//2
# t_2=(n*(n=1))/2
offset=n-s
if k%2==1:
    a=int(k+1-offset)
    b=int(offset)
    print(f"{a}/{b}")
else:
    a=int(offset)
    b=int(k+1-offset)
    print(f"{a}/{b}")