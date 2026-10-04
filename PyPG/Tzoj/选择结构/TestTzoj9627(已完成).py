a,b,c=map(int,input().split())

if (c*b)%a!=0:
    print("Error")
else:
    print((c*b)//a)