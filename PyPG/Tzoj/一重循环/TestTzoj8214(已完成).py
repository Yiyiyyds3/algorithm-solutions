# 快速幂
def culmilate():
    a,b=map(int,input().split())
    c=1
    if a>1000000000:
        print("-1")
    while b:
        if b&1:
            c*=a
            if c>1000000000:
                print("-1")
                return
        a*=a
        b>>=1
    print(c)

culmilate()