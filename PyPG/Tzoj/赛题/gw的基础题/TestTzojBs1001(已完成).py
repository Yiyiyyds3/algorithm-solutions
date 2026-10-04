n,k=map(int,input().split())
l=[]
l=list(map(int,input().strip().split()))
l.sort()
for i in range(k):
    print(l[i],end=' ')
