n=int(input())
if n%4==0:
    print(n//4*2)
elif n%4==1:
    print((n-1)//4*2+1)
elif n%4==2:
    print((n-2)//4*2+2)
elif n%4==3:
    print((n-3)//4*2+1)