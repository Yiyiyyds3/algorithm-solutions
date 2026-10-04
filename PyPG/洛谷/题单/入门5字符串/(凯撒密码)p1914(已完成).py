
n=int(input())
s=input()
for i in range(len(s)):
    print(chr(97+(ord(s[i])-97+n)%26),end='')