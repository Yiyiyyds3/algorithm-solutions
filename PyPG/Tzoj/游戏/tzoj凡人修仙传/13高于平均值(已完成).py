
t=int(input())
for i in range(t):
    s=list(map(int,input().split()))
    n=s[0]
    score=0
    for j in range(1,n+1):
        score+=s[j]
    avg=score/n
    ab_avg=0
    for j in range(1,n+1):
        if s[j]>avg:
            ab_avg+=1
    print(f"{ab_avg/n*100:.3f}%")