
n=int(input())
m=int(input())
a=[i for i in range(1,n+1)]
f=0
while len(a)>1:
    f+=1
    if f==m:
        a.pop(0)
        f=0
    else:
        a.append(a.pop(0))
print(a[0])