#简单数学计算
import sys
for i in sys.stdin:
    v1,v2,d,s,m=map(float,i.split())
    v1=v1*10
    v2=v2*10
    d=d*10
    s=s*10
    t_1=d/(v1-v2)
    t_2=s/v2
    if t_1>t_2  or t_1>m:
        print("oh yeah!")
    else:
        print("oh no!")