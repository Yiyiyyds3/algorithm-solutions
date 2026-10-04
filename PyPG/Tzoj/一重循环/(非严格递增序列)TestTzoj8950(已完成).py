#总后往前比较插值并把差值为一的数向前覆盖
n=int(input())
nums=list(map(int,input().split()))
nums=nums[::-1]

for i in range(len(nums)-1):
    gap=int(nums[i+1])-int(nums[i])
    if gap>1:
        print("No")
        break
    elif gap==1:
        nums[i+1]=nums[i]
else:
    print("Yes")