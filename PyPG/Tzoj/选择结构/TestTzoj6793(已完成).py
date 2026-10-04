a=float(input())
b=float(input())
c=float(input())
if a+b<c or a+c<b or b+c<a:
    print("Not triangle")
else:
    p=(a+b+c)/2
    print(f"{(p*(p-a)*(p-b)*(p-c))**0.5:.3f}")




