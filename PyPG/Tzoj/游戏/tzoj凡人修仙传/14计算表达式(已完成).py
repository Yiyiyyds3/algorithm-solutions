from math import sqrt
def integral(x,n):
    if n==1:
        return sqrt(1+x)
    return sqrt(n+integral(x,n-1))

s=input().split()
x=float(s[0])
n=int(s[1])
print(f"{integral(x,n):.2f}")
