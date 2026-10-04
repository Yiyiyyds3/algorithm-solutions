#求need与人数的最小倍数，向上取余
t=int(input())
for i in range(t):
    n,m,k,l=map(int,input().split())
    need=k+l
    nums=(need+m-1)//m
    if n<m or n<m*nums or n<need:
        print(-1)
    else:
        print(nums)