
s_1=input()
s_2=input()
for i in s_2:
    if i in s_1:
        s_1=s_1.replace(i,'')

print(s_1)