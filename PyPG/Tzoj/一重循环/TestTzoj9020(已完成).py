n=int(input())
x = 0
y = 0
z = 0
for i in range(1,n+1):
    x,y,z=map(float,input().split())
    if 3*y+z>=x:
        print("nb666")
    else:
        print("dou duo yu le")