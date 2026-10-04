# n=int(input())
# num=0
# s=list(map(int,input().split()))
# if n<3:
#     print(0)
#     exit()
# min_s=min(s[:-2])
# max_s=max(s[1:])
# for i in s[1:-1]:
#     if i>min_s and i<max_s:
#         num+=1
# print(num)

#前缀和与后缀和的应用

n = int(input())
nums = list(map(int, input().split())) 

if n < 3:
    print(0)
    exit()

left_min = [10000] * n
for i in range(1, n):
    left_min[i] = min(left_min[i-1], nums[i-1])

right_max = [0] * n
for i in range(n-2, -1, -1):
    right_max[i] = max(right_max[i+1], nums[i+1])

result = 0
for i in range(1, n-1):
    if left_min[i] < nums[i] < right_max[i]:
        result += 1

print(result)