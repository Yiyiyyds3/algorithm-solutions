import sys

# 加入三个元素岛list，分别是编号、总价值、价值列表要用元组的形式来加入
for _ in sys.stdin:
    n=int(_)
    value=[]
    for i in range(1,n+1):
        s=list(map(int,input().split()))
        if s[0]==0:
            continue
        value_sum=sum(s[j] for j in range(1,len(s)))
        if value_sum==0:
            continue
        value.append((
            i,
            value_sum,
            [s[k] for k in range(1,len(s))]
            ))
            
    value.sort(key=lambda x:(-x[1],x[0]))
    for j in range(len(value)):
        # print(value[j][0],value[j][2])
        print(f"{value[j][0]}: {' '.join(str(value[j][2][k]) for k in range(len(value[j][2])))}")
    print()