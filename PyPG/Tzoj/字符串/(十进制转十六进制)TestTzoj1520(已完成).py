import sys
for i in sys.stdin:
    if i.strip() == '0':
        break
    else:
        print(hex(int(i.strip()))[2:].upper())