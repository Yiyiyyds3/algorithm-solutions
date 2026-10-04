from math import *
n=int(input())
for i in range(n):
    nums=0
    p,t,m=map(int,input().split())
    nums+=p*15+t*20+m*25
    proportion=9000-nums
    f=(proportion+39)//40
    if f>100:
        print("impossible")
    else:
        print(f)