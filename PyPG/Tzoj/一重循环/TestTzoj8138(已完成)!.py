import sys
#该题目输入遇到runtime error的问题，解决办法是
# 用sys来规避可能存在的空格，
# 输入行数不足，避免隐藏的多组数据，兼容性更强
def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    x, y, n = map(int, data[:3])

    for _ in range(n):
        if x >= y:
            g = x // 2
            x -= g
            y += g
        else:
            g = y // 2
            x += g
            y -= g

    print(x, y)

if __name__ == "__main__":
    main()