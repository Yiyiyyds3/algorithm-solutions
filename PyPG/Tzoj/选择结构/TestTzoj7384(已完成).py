c=input()
o=ord(c)
h=hex(o)
h=h+''
h=h[::-1]
len_h=len(h)
h=h[0:len_h-2]
print(h)