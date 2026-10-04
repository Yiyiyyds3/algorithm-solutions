#多组输入使用sys的sys.stdin来实现
import sys
for line in sys.stdin:
    t=int(line)
    print(f"{t//3600:02}:{t%3600//60:02}:{t%60:02}")