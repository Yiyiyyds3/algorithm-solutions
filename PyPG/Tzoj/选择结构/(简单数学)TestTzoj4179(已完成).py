a,b,c=map(int,input().split())
max_abc=max(abs(a-b),abs(c-b))
print(max_abc-1)
