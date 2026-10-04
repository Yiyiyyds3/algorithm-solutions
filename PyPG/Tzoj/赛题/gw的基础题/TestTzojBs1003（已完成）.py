from collections import deque
s=input().split()
pwd=''
flag=0
while len(s)>0:
    temp=''
    flag+=1
    if flag%2==1:
        pwd+=s[0]
        s=s[1:]
    else:
        temp+=s[0]
        s=s[1:]
        s+=temp
for i in pwd:
    print(i,end=' ')
