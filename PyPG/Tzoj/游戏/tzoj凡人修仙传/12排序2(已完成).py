# import sys

# for i in sys.stdin:
#     i=i.replace('5',' ')
#     s=list(map(int,i.split()))
#     s.sort()
#     for j in range(len(s)):
#         if j==len(s)-1:
#             print(s[j],end='')
#         else:
#             print(s[j],end=' ')
#     print()
import sys

for line in sys.stdin:
    nums = line.replace('5', ' ').split()
    if nums:
        nums = sorted(map(int, nums))
        print(' '.join(map(str, nums)))  # join 自动处理空格，自带换行
    else:
        print()