
t=int(input())
for i in range(t):
    s_1=input().split()
    n_1=int(s_1[0])
    t_s=s_1[1]
    s_2=input().split()
    n_2=int(s_2[0])
    t_s_2=s_2[1]
    sums=0
    if n_1==n_2:
        for i in range(n_1):
            if t_s[i]==t_s_2[i]:
                sums+=1
        if sums/n_1>=0.700:
            print("Yes")
        else:
            print("No")
    else:
        print("No")