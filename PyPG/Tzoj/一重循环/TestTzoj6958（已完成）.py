# 希尔增量
n=int(input())
a=[]
while n!=1:
    n=n//2
    a.append(n)
a=a[::-1]
while len(a)!=0:
    print(a.pop(),end=" ")