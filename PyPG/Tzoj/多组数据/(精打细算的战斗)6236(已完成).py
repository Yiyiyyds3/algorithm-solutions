import sys
#使用独立概率计算公式
from math import log10,ceil
for i in sys.stdin:
    n,m=map(float,i.strip().split())
    if n==0:
        print(-1)
        continue
    elif n!=1 and  m==1:
        print(-1)
        continue
    elif (n==1 and m==1) or n>=m:
        print(1)
        continue
    k=ceil(log10(1-m)/log10(1-n))
    print(k)