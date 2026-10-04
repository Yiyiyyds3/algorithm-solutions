#减法操作
import sys
def spf(n):
    if n%2==0:
        return 2
    i=3
    while i*i<=n:
        if n%i==0:
            return i
        i+=2
    return n

for i in sys.stdin:
    n=int(i)
    if n==0:
        break
    print((n-spf(n))//2+1)


