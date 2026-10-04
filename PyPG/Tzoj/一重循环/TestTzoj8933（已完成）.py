n = int(input())
num=0
x=0
cha=1073741825
c=0
while 1:
    if cha<abs(n-c) and x!=0:
        print(pow(2,x-2))
        break
    c=pow(2,x)
    if cha==abs(n-c) and x!=0:
        print(c)
        break
    cha=min(abs(n-c),cha)
    x+=1
