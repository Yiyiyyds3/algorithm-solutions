import sys
from math import sqrt
# 填上你觉得需要的其他模块

def main():
    T = int(input())
    if T == 1:
        # 粘贴问题 1 的主函数代码
        print("I love Luogu!")
    elif T == 2:
        # 粘贴问题 2 的主函数代码
        print(2 + 4, 10 - 2 - 4)
    elif T == 3:
        print(14//4)
        print(12)
        print(14%4)
        # 请自行完成问题 3 的代码
        pass
    elif T == 4:
        print(f"{500/3:.3f}")
        # 请自行完成问题 4 的代码
        pass
    elif T == 5:
        print(480//32)
        # 请自行完成问题 5 的代码
        pass
    elif T == 6:
        print(f"{sqrt(9**2+6**2):.4f}")
        # 请自行完成问题 6 的代码
        pass
    elif T == 7:
        print(110)
        print(90)
        print(0)
        # 请自行完成问题 7 的代码
        pass
    elif T == 8:
        pi=3.141593
        r=5
        print(f"{2*pi*r:.4f}")
        print(f"{pi*r*r:.4f}")
        print(f"{pi*r*r*r*4/3:.3f}")
        # 请自行完成问题 8 的代码
        pass
    elif T == 9:
        print(22)
        # 请自行完成问题 9 的代码
        pass
    elif T == 10:
        print(9)
        # 请自行完成问题 10 的代码
        pass
    elif T == 11:
        print(f"{100/3:.4f}")
        # 请自行完成问题 11 的代码
        pass
    elif T == 12:
        print(13)
        print('R')
        # 请自行完成问题 12 的代码
        pass
    elif T == 13:
        pi=3.141593
        r1=4
        r2=10
        v=pi*(r1**3)*4/3+pi*(r2**3)*4/3
        i=2
        while i**3<=v:
            l=i
            i+=1
        print(f"{l:.0f}")
        # 请自行完成问题 13 的代码
        pass
    elif T == 14:
        print(50)
        # 请自行完成问题 14 的代码
        pass

if __name__ == "__main__":
    main()
