import sys
n=int(input())
for i in range(n):
    s=input()
    f=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            f+=1
        elif s[i]!=s[i+1] :
            if f==1:
                print(s[i],end='')
            else:
                print(f"{f}{s[i]}",end='')
                f=1
        if i==len(s)-2:
            if f==1:
                print(s[i+1],end='')
            else:
                print(f"{f}{s[i+1]}",end='')
                f=1
    print()