
#秦九韶算法，通过累乘和累加来算
def pi(a,x):
    result=0
    for i in reversed(a):
        result=result*x+i
    return result

n,x=map(int,input().split())
a=list(map(int,input().split()))

print(pi(a,x)%1000000007)