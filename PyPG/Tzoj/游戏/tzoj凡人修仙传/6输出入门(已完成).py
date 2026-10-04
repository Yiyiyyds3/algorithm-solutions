import sys
a,b =map(int,input().split())
print(a+b)
for i in sys.stdin:
    a,b=map(int,i.split())
    if a==0 and b==0:
        break
    else:
        print(f"\n{a+b}")