#可以用正则表达式来尝试完成
import sys


n=input()
result = 0      
current_num = 0 
sign = 1       
    
for c in n:
        if c.isdigit():
            current_num = current_num * 10 + int(c)
        else:  

            result += sign * current_num
            # 更新符号：+→1，-→-1
            sign = 1 if c == '+' else -1

            current_num = 0
result += sign * current_num
print(result)