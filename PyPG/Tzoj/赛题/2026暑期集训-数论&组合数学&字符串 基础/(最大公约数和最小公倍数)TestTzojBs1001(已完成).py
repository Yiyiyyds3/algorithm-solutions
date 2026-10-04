def gdc(n,m):
    if m==0:
        return n
    else:
        return gdc(m,n%m)
    
n,m=map(int,input().split())
gcd_num=gdc(n,m)
lcm=n*m//gcd_num
print(lcm,gcd_num)