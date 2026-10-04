#求32位机子的剩余前导零数量
n=int(input())
n_2=''
while n:
    n_2+=str(n%2)
    n//=2
print(32-len(n_2))
