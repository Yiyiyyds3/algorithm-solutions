import sys
for i in sys.stdin:
    a,b=map(int,i.split())
    if a > b:
        a, b = b, a
    count_o=0
    count_j=0
    for j in range(a,b+1):
        if j%2==0:
            count_o+=j*j
        else:
            count_j+=j*j*j
    print(count_o,count_j)