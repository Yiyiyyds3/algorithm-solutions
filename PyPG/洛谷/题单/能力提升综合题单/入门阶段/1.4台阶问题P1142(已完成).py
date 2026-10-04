#递归太慢了，还是得用递推来做
# def step(n,k):
#     if (n==1 and k>=1) or n==0:
#         return 1
#     return  sum(step(n-i,k) for i in range(1,n+1))

# n,k=map(int,input().split())
# for i in range(n):

#传统递推（还是太慢了）
# ans=100003
# n,k=map(int,input().split())
# f=[0]*(n+1)
# f[0]=1
# for i in range(1,n+1):
#     for j in range(1,k+1):
#         if i-j>=0:
#             f[i]=(f[i]+f[i-j]) % ans
# print(f[n])

#使用滑动窗口来优化

ans=100003
dp=[0]*(100001)
n,k=map(int,input().split())
dp[0]=1
windows_sum=1
for i in range(1,n+1):
    dp[i]=windows_sum%ans
    windows_sum=(windows_sum+dp[i])%ans
    if i>=k: #当i>=k时，窗口大小为k，需要减去最左边的值，因为windows_sum里还有dp[0]，所以要减去dp[i-k]
        windows_sum=(windows_sum-dp[i-k])%ans
    
print(dp[n])