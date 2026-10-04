n=int(input())
s=input().split()
s1=0
s2=0
for i in s:
    if i=='0':
        s1+=1
    else:
        s2+=1
if s1>=s2:
    print("NO")
    print(s2,s1)
else:
    print("YES")
    print(s2,s1)