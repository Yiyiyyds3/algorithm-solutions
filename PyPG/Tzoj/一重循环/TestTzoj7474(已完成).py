from math import sqrt
dian=input().split(",")
a=[]
xlen=0
for i in dian:
    a.append(int(i))
for i in range(0,len(a)-3,2):
    xlen+=sqrt((a[i+2]-a[i])**2+(a[i+3]-a[i+1])**2)
print(f"{xlen:.2f}")