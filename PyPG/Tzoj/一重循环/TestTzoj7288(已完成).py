n,m,t=map(int,input().split())
for i in range(n):
    a=int(input())
    m+=a
if m>=t:
    print("Good Luck")
else:
    print("So Bad")