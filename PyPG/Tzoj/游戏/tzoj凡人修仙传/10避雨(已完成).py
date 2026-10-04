from math import *
#直线距离要用欧几里得距离来求，曼哈顿距离求的是折线距离
t=int(input())

for i in range(t):
    n,m=map(int,input().split())
    x=0
    y=0
    d_num=list()
    s_num=list()
    for j in range(n):
        s=input()
        if 'd' in s or 's' in s: 
            for k in range(len(s)):
                if 's' in s:
                    y=s.find('s')
                    s_num.append([x,y])
                    s=s.replace('s','.')
                elif 'd' in s:
                    y=s.find('d')
                    d_num.append([x,y])
                    s='.'*(y+1)+s[y+1::]        
                elif s.find('d')== -1:
                    break
            x+=1
        else:
            x+=1
    min_distance=float('inf')
    t_x=-1
    t_y=-1
    for j in range(len(d_num)):
            if sqrt((d_num[j][0]-s_num[0][0])**2+(d_num[j][1]-s_num[0][1])**2)<min_distance:
                min_distance=sqrt((d_num[j][0]-s_num[0][0])**2+(d_num[j][1]-s_num[0][1])**2)
                t_x=d_num[j][0]
                t_y=d_num[j][1]
            elif sqrt((d_num[j][0]-s_num[0][0])**2+(d_num[j][1]-s_num[0][1])**2)==min_distance and t_x>d_num[j][0]:
                t_x=d_num[j][0]
                t_y=d_num[j][1]
            elif sqrt((d_num[j][0]-s_num[0][0])**2+(d_num[j][1]-s_num[0][1])**2)==min_distance and t_x==d_num[j][0] and t_y>d_num[j][1]:
                t_y=d_num[j][1]

    print(f"({t_x},{t_y})")
