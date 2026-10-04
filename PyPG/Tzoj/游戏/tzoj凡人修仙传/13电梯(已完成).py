import sys
for i in sys.stdin:
    s=list(map(int,i.split()))
    if s[0]==0:
        break
    N=s[0]
    now_floor=0
    all_time=0
    for j in range(1,len(s)):
        if s[j]>now_floor:
            all_time+=(s[j]-now_floor)*6+5
        elif s[j]<now_floor:
            all_time+=(now_floor-s[j])*4+5
        elif s[j]==now_floor:
            all_time+=5
        now_floor=s[j]
    print(all_time)