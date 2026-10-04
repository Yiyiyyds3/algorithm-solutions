x,n=map(int,input().split())
if n%2==0:
    print(0,x*2**(n//2))
else:
    print(1,x*2**((n-1)//2))