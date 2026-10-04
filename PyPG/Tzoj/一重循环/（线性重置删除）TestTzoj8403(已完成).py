#线性重置删除
# n=int(input())  
# nums=[]
# new_nums=[]
# count=0
# num=3
# a_day=0
# t_day=0
# for i in range(1,n+1):
#     nums.append(i)
# while 1:
#     a_day+=1
#     for i in range(len(nums)):
#         if i==0 and nums[i]==n:
#             t_day=a_day
#             continue
#         elif i==0:
#             continue
#         count+=1
#         if count!=num:
#             new_nums.append(nums[i])
#         elif count==num and nums[i]==n:
#             count=0
#             t_day=a_day
#             continue
#         elif count==num:
#             count=0
#             continue

#     count=0
#     if len(new_nums)==1 and new_nums[0]==n:
#         a_day+=1
#         t_day=a_day
#         break
#     elif len(new_nums)==1:
#         a_day+=1
#         break
#     else:
#         nums=new_nums
#         new_nums=[]
# print(a_day,t_day)

''''
超出内存限制原因：保存了完整的数组
如果n很大如10^9，数组长度为10^9，内存会超出限制
改进思路
直接计算总天数
不存储完整数组，仅仅记录目标位置
用整数除法表示向上取整ceil(x/y)=>(x+y-1)//y
用整数除法表示向下取整floor(x/y)=>x//y
'''
n=int(input())
a_day=0
t_day=0
temp=n
#算总数
while temp>0:
    a_day+=1
    temp=(2*temp)//3
#记录目标位置    
pos=n
while True:
    t_day+=1
    if pos%3==1:
        break
    else:
        pos=pos-(pos+2)//3
print(a_day,t_day)