# t=int(input())
# for i in range(t):
#     n=int(input())
#     nums=list(map(int,input().split()))
#     max_value=nums[0]
#     second_value=nums[0]
#     for num in nums:
#         if num>max_value:
#             second_value=max_value
#             max_value=num
#         elif num>second_value and num!=max_value:
#             second_value=num
#     if second_value==max_value:
#         print("None")
#     else:
#         print(second_value)

''''版本2'''
# import sys

# input = sys.stdin.readline

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     max_val = None
#     sec_val = None
#     # 直接遍历输入的每个数字，不额外存成大列表以节省内存
#     for num in map(int, input().split()):
#         if max_val is None or num > max_val:
#             sec_val = max_val
#             max_val = num
#         elif num < max_val and (sec_val is None or num > sec_val):
#             sec_val = num
    
#     if sec_val is None:
#         print("None")
#     else:
#         print(sec_val)

''''版本3不适用split()进行分割，手动进行潘东更快'''
import sys

input = sys.stdin.readline#数据量大用这个加快输入

t = int(input())
for _ in range(t):
    n = int(input())
    line = input()  # 读入整行字符串，不 split
    
    max_val = None
    sec_val = None
    num = 0
    sign = 1
    
    for ch in line:
        if ch == '-':
            sign = -1
        elif ch == ' ' or ch == '\n':
            # 一个完整的数字解析完毕，应用符号
            num *= sign
            # 更新最大值和第二大值
            if max_val is None or num > max_val:
                sec_val = max_val
                max_val = num
            elif num < max_val and (sec_val is None or num > sec_val):
                sec_val = num
            # 重置，准备解析下一个数
            num = 0
            sign = 1
        else:
            # 字符转数字（比 int(ch) 快）
            num = num * 10 + (ord(ch) - 48)
    
    if sec_val is None:
        print("None")
    else:
        print(sec_val)