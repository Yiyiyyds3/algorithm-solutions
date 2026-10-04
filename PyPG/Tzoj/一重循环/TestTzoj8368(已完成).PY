n=int(input())
a=0
b=0
index=0
t=input().split()
for i in t:
    index+=1
    if i=='1' and index<=15:
        b+=1
    elif i=='0' and index>15:
        b+=1
    if b==16:
        print("Bob")
        break
    if i=='0' and index<=15:
        a+=1
    elif i=='1' and index>15:
        a+=1
    if a==16:
        print("Alice")
        break
else:
    print("Peace")