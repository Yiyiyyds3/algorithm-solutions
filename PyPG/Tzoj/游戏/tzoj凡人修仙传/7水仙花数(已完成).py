import sys
def s_nums(n):
    nums=int(n)
    t=int(n[0])
    h=int(n[1])
    s=int(n[2])
    if t**3+h**3+s**3==nums:
        return True
    else:
        return False

for i in sys.stdin:
    a,b=map(int,i.split())
    f=0
    for j in range(a,b+1):
        if s_nums(str(j)):
            if f==0:
                print(f"{j}",end='')
                f=1
            else:
                print(f" {j}",end='')
    if f==0:
        print('no',end='')
    print()
    
