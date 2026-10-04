import math
import sys
for i in sys.stdin:
    b,P=map(int,i.split())

    found = False

# 方法1：循环少量x1（因为x1很大时N会远大于P，所以循环有上界）
# 提示：x1 从 -abs(P) 到 abs(P) 就足够了，想想为什么？
    for x1 in range(-abs(P), abs(P) + 1):
        N = 3 * x1 * x1 + 3 * x1 + 1 + b
        if N == P:  # 或者 if is_prime(N): （如果题目是任意质数）
            found = True
            break

# 方法2：用求根公式（更高效）
# 方程：3*x1^2 + 3*x1 + (1 + b - P) = 0
# 提示：计算判别式 delta，检查它是否是完全平方数
    # delta = 9 - 12 * (1 + b - P)
    # if delta >= 0:
    #     sqrt_delta = int(math.isqrt(delta))
    #     if sqrt_delta * sqrt_delta == delta:  # 是完全平方数
    #     # 提示：检查 (-3 + sqrt_delta) 是否能被 6 整除
    #         if (-3 + sqrt_delta) % 6 == 0:
    #             found = True

    print("Existent" if found else "Non-existent")
