b=input().split()
r=input().split()
bnum=0
rnum=0
for i in b:
    bnum+=int(i)
for i in r:
    rnum+=int(i)
if bnum-rnum>=1:
    print("Blue")
else:
    print("Red")