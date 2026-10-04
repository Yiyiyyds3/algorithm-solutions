
n,m,x,y=map(int,input().split())
for i in range(1,n+1):
    if i!=1:
        m+=x
        m-=y
        x=y*2
        x=y//2
        y=y*2
    if m<28:
        print(i)
        break
    elif m>=28 and i==n:
        print(-1)
    