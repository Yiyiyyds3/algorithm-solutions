s=input()
sorted_s=sorted(s)
if sorted_s[0]==sorted_s[1] and sorted_s[1]!=sorted_s[2] and sorted_s[2]==sorted_s[3]:
    print("Yes")
else:
    print("No")