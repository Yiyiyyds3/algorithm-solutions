import sys
for i in sys.stdin:
    result=0
    a,n=map(int,i.strip().split())
    s=str(a)
    for i in range(n):    
        result+=int(s)
        s+=str(a)
    print(result)