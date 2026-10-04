n=int(input())
list=[0]
num=0
for i in range(1,n-1):
    if(i<3):
        list.append(1)
    else:
        list.append(list[i-1]+list[i-2])
for i in range(1,n-1):
    num+=list[i]
print(num+1)


# 斐波那契数列 第三项开始，每一项等于前两项之和