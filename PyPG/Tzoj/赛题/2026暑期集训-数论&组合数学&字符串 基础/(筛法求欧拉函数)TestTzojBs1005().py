def Is_p(n):
    nums=bytearray(0)*(n+1)
    nums[0]=nums[1]=1
    for i in range(2,n+1):
        if nums[i]:
            for j in range(i,n+1,i):
                nums[j]+=1
n=int(input())
Is_p(10**6)