from math import *  
def IsNum(a1):
    a=a1
    if a==1:
        return False
    if a<=3:
        return True
    else:
        a2=ceil(sqrt(a))+1
        for i in range(2,a2):
            if a%i==0:
                return False
        return True
nums=[]
n=int(input())
a=input().split()
for i in range(n):

    if IsNum(int(a[i]))==True:
        nums.append(a[i])
    else:
        continue
for i in range(len(nums)):
    if i==len(nums)-1:
        print(nums[i])
    else:print(nums[i],end=' ')