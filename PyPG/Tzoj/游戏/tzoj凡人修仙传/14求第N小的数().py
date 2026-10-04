# import sys
# def fang_shu(n=3*10**7):
#     fang_shu = [1]*(n+1)
#     for i in range(1, n+1):
#         if fang_shu[i]:
#             if i*i>n:
#                 break
#             fang_shu[i*i]=0
#     return ((j,k-) for j,k in enumerate(fang_shu) if k)

# nums = fang_shu()
# print(len(nums))
# for i in sys.stdin:
#     n=int(i)
#     result=[]
#     f=0
#     for i,j in nums:
#         if f==n:
#             break
#         result.append((i,j))
#         f+=1
#     result.sort()
#     print(result[n])