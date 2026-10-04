def kmp(s1,s2):
    next=build_next(s2)
    i=0
    j=0
    nums=[]
    while i<len(s1) and j<len(s2):
        if s1[i]==s2[j]:
            i+=1
            j+=1
        elif j>0:
            j=next[j-1]
        else:
            i+=1
        if j==len(s2):
            nums.append(i-j)
            j=next[j-1]
    return nums
def build_next(s2):
    next=[0]
    prefix_len=0
    i=1
    while i<len(s2):
        if s2[prefix_len]==s2[i]:
            prefix_len+=1
            next.append(prefix_len)
            i+=1
        elif prefix_len>0:
            prefix_len=next[prefix_len-1]
        else:
            next.append(0)
            i+=1
    return next
s1=input()
s2=input()
nums=kmp(s1,s2)
next=build_next(s2)
for i in range(len(nums)):
    print(nums[i]+1)

for j in range(len(next)):
    if j==len(next)-1:
        print(next[j],end='')
        continue
    else:
        print(next[j],end=' ')
        
