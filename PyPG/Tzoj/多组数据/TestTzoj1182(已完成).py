#多组输入，1行第一位为输入位数后续为输入的数字，可以用字符串的风格和列表来实现
result=[]
while True:
    sum=0
    parts=input().strip().split()
    k=int(parts[0])
    if k==0:
        break
    nums = list(map(int, parts[1:]))
    # print(nums)
    result.append(nums)
    for i in nums:
        sum+=i
    print(sum)