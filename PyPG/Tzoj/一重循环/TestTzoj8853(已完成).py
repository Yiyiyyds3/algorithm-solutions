n=int(input())
a=[]
num=0
s=input().split()
for i in range(n):
    a.append(int(s[i]))
for i in range(n):
    if a[i]%2!=0:
        num+=(a[i]+1)//2
    else:
        num+=a[i]//2
print(num)