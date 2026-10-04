n=int(input())
ji_num=0
ou_num=0
for i in range(n):
    a=int(input())
    if a%2==0:
        ou_num+=1
    else:
        ji_num+=1
print(ji_num,ou_num)