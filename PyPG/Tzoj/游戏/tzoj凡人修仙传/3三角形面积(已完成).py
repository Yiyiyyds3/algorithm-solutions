import math
a=float(input())
b=float(input())
c=float(input())
l=(a+b+c)/2
#海伦公式
print("%.3f"%(math.sqrt(l*(l-a)*(l-b)*(l-c))))
