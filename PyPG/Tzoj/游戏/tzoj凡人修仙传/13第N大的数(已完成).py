
#警惕split()的用法
for i in range(int(input())):
    s=input().split()
    n=int(s[0])
    nums=list(map(int,s[1:]))
    nums.sort()
    print(n,nums[-3])