import sys
#使用数组自带的求同分人数的函数
for i in sys.stdin:
    n=int(i)
    if n==0:
        break
    scores=list(map(int,input().split()))
    target=int(input())
    count=scores.count(target)
    print(count)

