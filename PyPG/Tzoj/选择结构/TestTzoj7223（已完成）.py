num=input()
f=0
for i in num:
    if i=='-':
        f+=1
if f%2==0:
    print('positive')
else:
    print('negative')