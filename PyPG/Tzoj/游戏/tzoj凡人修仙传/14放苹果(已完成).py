

#核心逻辑是整数划分
def put_apple(m,n):
    if m==0 or n==1:
        return 1
    if m<n:
        return put_apple(m,m)
    else:
        return put_apple(m-n,n)+put_apple(m,n-1)


t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    print(put_apple(m,n))
#递归实现