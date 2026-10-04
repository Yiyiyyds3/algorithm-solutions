mod=1000000007
def fc():
    x=int(input())
    ans=1
    for i in range(2,x+1):
        ans=(ans*i)%mod
    print(ans)

fc()

#单纯迭代累乘