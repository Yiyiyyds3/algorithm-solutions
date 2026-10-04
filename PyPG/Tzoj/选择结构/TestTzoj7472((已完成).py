weight=int(input())
value=int(input())
if weight<=20:
    print("0")
else:
    yj=value*0.015*(weight-20)
    yj=round(yj)
    print(yj)