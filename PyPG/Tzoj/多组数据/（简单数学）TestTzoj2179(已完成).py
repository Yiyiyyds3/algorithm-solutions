import sys
from math import ceil
for i in sys.stdin:
    b,n=map(int,i.split())
    if b==0 and n==0:
        break
    a=b**(1/n)   
    a_c=ceil(a)
    a_f=a_c-1
    if a_c**n-b<=b-a_f**n:
        print(a_c)
    else:
        print(a_f)