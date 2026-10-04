n=int(input())
n_y=0
n_m=0
n_o=0
for i in range(n):
    a,b=map(int,input().split())
    if b>=10 and b<=30:
        n_y+=a
    elif b>=31 and b<=50:
        n_m+=a
    elif b>=51 and b<=70:
        n_o+=a
n_a={"Young": n_y, "Middle": n_m, "Old": n_o}
n_a=sorted(n_a.items(), key=lambda x: x[1], reverse=True)
for x,y in n_a:
    print(f"{x}: {y}")
if n_y>n_m and n_y>n_o:
    print("Yes")
else:
    print("No")