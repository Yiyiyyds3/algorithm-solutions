
#调和级数，模拟求和即可范围1-1000
m=int(input())
n=input().split()
sum_n=0
for i in range(m):
    new_n=int(n[i])
    sum_n=sum((-1)**(k-1)/k for k in range(1,new_n+1))
    print(f"{sum_n:.2f}")
