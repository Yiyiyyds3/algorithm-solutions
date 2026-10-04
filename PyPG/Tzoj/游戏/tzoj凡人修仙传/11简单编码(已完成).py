
nums=[9,8,7,6,5,4,3,2,1,0]
result=''
s=input()
for i in s:
    if i >='0' and i<='9':
        result+=str(nums[int(i)])
    elif i>='A' and i<='Z':
        result+=chr(ord(i)+32)
    elif i>='a' and i<='z':
        result+=chr(ord(i)-32)
    else:
        result+=i
result=result[::-1]
print(result)