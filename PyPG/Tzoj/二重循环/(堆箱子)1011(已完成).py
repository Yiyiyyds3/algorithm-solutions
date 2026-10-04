f=1
while 1:
    n=int(input())
    if n==0:
        break
    nums=list(map(int,input().split()))
    average=sum(nums)//n
    op=0
    for i in range(n):
        if nums[i]>average:
            op+=nums[i]-average
    print(f"Set #{f}")
    print(f"The minimum number of moves is {op}.")
    print()
    f+=1