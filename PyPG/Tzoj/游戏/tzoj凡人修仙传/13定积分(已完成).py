
nums=[]
for i in range(int(input())):
    a,b= map(int,input().split())
    nums.append((a,b))
x1,x2= map(int,input().split())

def F(x):
    value=0.0
    for i,j in nums:
        coeff=i/(j+1)
        value+=coeff*(x**(j+1))
    return value
result=F(x1)-F(x2)
print(f"{result:.4f}")