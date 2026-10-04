from math import ceil
mile=float(input())
money=0
if mile <=4:
    money=2
elif mile <=12:#1：4
    money=2+ceil((mile-4)/4)
elif mile <=24:#1：6
    money=4+ceil((mile-12)/6)
elif mile >24:#1：8  maxmoney==8
    money=6+ceil((mile-24)/8)
if money>8:
    money=8
print(int(money))