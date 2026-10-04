

result=[]
n,m=map(int,input().split())
for i in range(m):
    d=0
    s=input()
    s_nums=[]*m
    nums=[]
    s_nums.append(s)
    for j in s:
        if j=='A':
            nums.append(1)
        elif j=='C':
            nums.append(2)
        elif j=='G':
            nums.append(3)
        elif j=='T':
            nums.append(4)
    for j in range(len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[j]>nums[k]:
                d+=1
    result.append((d,i,s))

result.sort(key=lambda x:(x[0],x[1]))
for i in result:
    print(i[2])
# import sys

# def count_inversions(s):
#     """计算字符串 s 的逆序数（即前面字母大于后面字母的对数）"""
#     inv_count = 0
#     n = len(s)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if s[i] > s[j]:  # 因为 A<C<G<T，直接比较字符即可
#                 inv_count += 1
#     return inv_count

# def main():
#     # 读取所有输入
#     data = sys.stdin.read().strip().split()
#     if not data:
#         return
    
#     # 解析第一行
#     n = int(data[0])  # 字符串长度（本题中其实可以不用，直接用len就行）
#     m = int(data[1])  # 字符串数量
#     strings = data[2:2 + m]
    
#     # 构造一个列表，每个元素是一个元组：(逆序数, 原始下标, 字符串)
#     dna_list = []
#     for idx, s in enumerate(strings):
#         inv = count_inversions(s)
#         dna_list.append((inv, idx, s))
    
#     # 排序：先按逆序数升序，再按原始下标升序（保证稳定性）
#     dna_list.sort(key=lambda x: (x[0], x[1]))
    
#     # 按格式输出
#     for item in dna_list:
#         print(item[2])

# if __name__ == '__main__':
#     main()