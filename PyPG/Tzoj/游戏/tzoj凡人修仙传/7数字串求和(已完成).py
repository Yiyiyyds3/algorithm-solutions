import sys
for i in sys.stdin:
    a,n=map(int,i.split())
    count=0
    while i:
        for i in range(n):
            count+=a*10**i
        n-=1
    print(count)