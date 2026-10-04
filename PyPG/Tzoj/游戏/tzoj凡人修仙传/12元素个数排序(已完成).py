import sys

n=[]
for i in sys.stdin:
    if i=='EOF\n':
        break
    n.append(i)
n.sort(key=lambda x:len(x.split()))
for i in n:
    print(i,end='')


    