
n=input().split()
n=n[1::]
m=int(input())
n=n[-m::]+n[:-m:]
for i in range(len(n)):
    if i==len(n)-1:
        print(n[i],end='')
    else:
        print(n[i],end=' ')
