#用字符串比较大小时要小心，最好转换成整型在比较
n=int(input())
for i in range(n):
    parts=input().split()
    a=int(parts[0])
    b=int(parts[2])
    c=int(parts[4])
    if parts[1]!='+' or c<1 or c>7:
        print('NO!!!')
        continue
    
    print((a+b+c)%(c+1))