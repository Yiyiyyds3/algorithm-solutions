from math import floor

L=int(input())
R=int(input())
A=int(input())
S=min(L,R)
D=abs(L-R)
if A>=D:
    RD=A-D
    print(2*(S+D)+2*(RD//2))
else:
    print(2*(S+A))

# 木桶原理