a,b = map(int,input().split())
percent=b/a*100
if percent>=100:
    print("100.00%")
else:
    print(f"{percent:.2f}%")