import sys
f=0
for i in sys.stdin:
    if f!=0:
        print()
    
    s=i.split()
    Char=s[0]
    if Char=='@':
            break
    n=int(s[1])
    for i in range(1,n+1):
        for j in range(1,n-i):
            print(' ',end='')
        for j in range(1,2*i):
            if j==1 or j==2*i-1 or i==n:
                print(Char,end='')
            else:
                print(' ',end='')
        print()
    f+=1    
    
# import sys

# first = True
# for line in sys.stdin:
#     line = line.strip()
#     if not line:
#         continue
    
#     parts = line.split()
#     ch = parts[0]
#     if ch == '@':
#         break
    
#     n = int(parts[1])
    
#     if not first:
#         print()
#     first = False
    
#     for i in range(1, n + 1):
#         print(' ' * (n - i), end='')
#         for j in range(1, 2 * i):
#             if j == 1 or j == 2 * i - 1 or i == n:
#                 print(ch, end='')
#             else:
#                 print(' ', end='')
#         print() 