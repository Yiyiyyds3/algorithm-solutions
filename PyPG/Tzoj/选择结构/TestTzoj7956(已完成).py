a,b,c=map(float,input().split())
lt=2.455
gt=1.26
if b==0:
    bz=a*lt
elif b==1:
    bz=a*gt
if bz <= c:
    print(f"{bz:.2f} ^_^")
else:
    print(f"{bz:.2f} T_T")

#洛希极限,要用到开三次方的函数
