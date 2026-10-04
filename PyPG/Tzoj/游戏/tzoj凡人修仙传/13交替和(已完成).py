import sys
for i in sys.stdin:
    a,b=map(int,i.split())
    f=0
    sum_ab=0
    for i in range(a,b+1):
        if f<=1:
            sum_ab+=i
            f+=1
        elif f%2==0:
            sum_ab-=i
            f+=1    
        elif f%2==1:
            sum_ab+=i
            f+=1
    print(sum_ab)