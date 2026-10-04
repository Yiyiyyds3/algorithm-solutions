x,y=map(int,input().split())
#整数向上取整
k=(x*105+y-1)//y
#求折数
ans=k/10
if ans>10:
    print(10.0)
else:
    print(ans)