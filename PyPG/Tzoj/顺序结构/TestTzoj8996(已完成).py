from collections import deque

num=input().strip()
flag=0
q= deque()
q.extend(map(int, num.split()))
a=''
temp=0
while len(q) != 0:
    flag+=1
    if flag%2==1:
        a+=str(q.popleft())
        a+=' '
    else:
        q.append(q.popleft())
print(a)