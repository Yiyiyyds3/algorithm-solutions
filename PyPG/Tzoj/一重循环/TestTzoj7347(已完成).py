from math import *
n=int(input())
t=ceil((sqrt(8*n+1)-1)/2)
s=n-(t-1)*t//2-1
a=2**t+2**s
print(a)