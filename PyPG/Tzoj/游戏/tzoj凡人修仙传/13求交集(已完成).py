
t=int(input())
for i in range(t):
    n=int(input())
    nums=set(map(int,input().split()))
    n_2=int(input())
    nums_2=set(map(int,input().split()))
    set_join=nums&nums_2
    set_n=0
    for j in range(len(set_join)):
        set_n+=1
    print(set_n)