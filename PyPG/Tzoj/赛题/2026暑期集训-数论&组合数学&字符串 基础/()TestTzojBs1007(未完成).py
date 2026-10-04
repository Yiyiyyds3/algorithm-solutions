def ojld(a,p):
    if a%p==1:
        return a-(p*(a+p-1)//p)  
    else:
        
        return ojld(a,p) 
n,p=int(input())
for i in range(n):
    lcm_i=p*i