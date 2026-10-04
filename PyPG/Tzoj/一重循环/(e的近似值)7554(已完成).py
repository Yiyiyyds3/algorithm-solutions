#递推

def sum_factorial(n):
    total=1.0
    fact=1.0
    for i in range(1,n+1):
        fact*=i
        total+=1/fact
    return total

n=int(input())
print(f"{sum_factorial(n):.3f}")