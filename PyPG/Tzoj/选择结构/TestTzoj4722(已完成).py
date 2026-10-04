from math import sqrt
x1,y1,x2,y2=map(int,input().split())
if sqrt((x1-x2)**2+(y1-y2)**2)>= 1 and sqrt((x1-x2)**2+(y1-y2)**2)<= sqrt(2)  :
    print("collision")
elif sqrt((x1-x2)**2+(y1-y2)**2)<= 1  :
    print("error")
else :
    print("normal") 