from math import floor
N=int(input())
x=0
y=floor(N/5)
num=0
while y>=0:
    if (N-5*y)%3==0:
        x=(N-5*y)//3
        num+=x+y
        print(num)
        break
    y-=1
else:
    print(-1)
#注意循环的漏洞，当允许取得y=0的条件下，while循环要写y>=0while: else:结构下只有在循环正常结束时候才会执行else下的内容