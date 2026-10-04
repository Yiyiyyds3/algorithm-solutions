
#递归
def hanoi(n, a, b, c):
    setps=0
    if n == 1:
        
        print( f'Move disk {n} from {a} to {c}')
    else:
        hanoi(n-1, a, c, b)
        print(f'Move disk {n} from {a} to {c}')
        hanoi(n-1, b, a, c)
n=int(input())  
hanoi(n,'A','B','C')