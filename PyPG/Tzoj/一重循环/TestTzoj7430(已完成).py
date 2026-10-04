#使用decimal 实现更高精度的四舍五入
from decimal import  Decimal,getcontext,ROUND_HALF_UP
# getcontext().prec=6  全局有效数字位
s=''
n=input().strip()
num=Decimal(n)
w=int(input())
for i in range(w):
    s+='0'
precision=Decimal(f"0.{s}")
num=num.quantize(precision,rounding=ROUND_HALF_UP)
print(num)
