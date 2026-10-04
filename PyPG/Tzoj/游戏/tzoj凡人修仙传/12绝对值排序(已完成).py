import sys
for i in  sys.stdin:
    s=i.split()
    n=int(s[0])
    nums=s[1:]
    if n==0:
        break
    nums.sort(key=lambda x:abs(int(x)),reverse=True)
    for i in range(len(nums)):
        if i!=len(nums)-1:
            print(nums[i],end=' ')
        else:
            print(nums[i],end='')
    print()
