a,b,c=map(int,input().split())
s=a+b+c
u=s/3
vmin=(abs(a-u)+abs(b-u)+abs(c-u))/2
print(f"{vmin:.2f}")

# 倒水问题，求最少倒水量