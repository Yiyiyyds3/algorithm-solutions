a=''
num = input()
num = num[::-1]
flag = 1
for i in num:
    if flag ==1 and i == '0':
        continue
    else:
        a+=i
        flag+=1
print(a)