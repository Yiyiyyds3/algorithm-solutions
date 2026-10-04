L,M=map(int,input().split())
n=[0]*(L+1)
for i in range(M):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        n[j]=1
print(L-n.count(1)+1)