
n=int(input())
for i in range(n):
    nums=list(map(int,input().split()))
    n=nums[0]
    count=0
    for j in range(1,n+1):
        count+=nums[j]
    print(count-n+1)
