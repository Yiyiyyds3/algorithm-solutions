
t=int(input())
for i in range(t):
    s=input()
    x1=int(s[1])
    y1=int(s[3])
    x2=int(s[7])
    y2=int(s[9])
    step=0
    if x1==x2 and y2>=y1:#避免后退，前进
        step=abs(int(y2)-int(y1))
        print(step)
    elif y2<y1:#避免向下移动
        print("Error!")
    elif x1==x2 and y1==y2:#原地不动
        print(0)
    elif (x1!=x2 and y2<5):#没过河，不能左右移动
        print("Error!")
    elif x1!=x2 and y2>=5:#已过河,左右上移动
        step=abs(int(x2)-int(x1))+abs(int(y2)-int(y1))
        print(step)
    

    