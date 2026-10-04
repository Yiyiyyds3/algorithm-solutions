import sys
for i in sys.stdin:
    a,b=map(int,i.split())
    if a==0 and b==0:
        break
    t_s=''
    for j in range(a):
        s=input()
        t_s+=s
    print(sum(line.count('*') for line in t_s))