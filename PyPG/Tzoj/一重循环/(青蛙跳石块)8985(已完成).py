n=int(input())
nums=list(map(int,input().split()))
max_len=0
now_len=0
for i in range(n-1):
    if nums[i]>=nums[i+1]:
        now_len+=1
    else:
        now_len=0
    max_len=max(max_len,now_len)
print(max_len)
