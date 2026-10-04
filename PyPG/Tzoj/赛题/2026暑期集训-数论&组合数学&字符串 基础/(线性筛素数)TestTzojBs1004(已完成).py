from math import isqrt
from array import array
import sys
#判断素数  (欧拉筛)
def Is_p(n):
    nums=bytearray(b'\x01')*(n+1)
    nums[0]=nums[1]=False
    primes=array('I')
    for i in range(2,n+1):
        if nums[i]:
            primes.append(i)
        
        for p in primes:
            if p*i>n:
                break
            nums[p*i]=0
            if i%p==0:
                break
    return primes

n,q=map(int,input().split())
nums_p=Is_p(10**8)
# print(sys.getsizeof(nums_p)/1024**2)
for i in range(q):
    k=int(input())
    print(nums_p[k-1])

