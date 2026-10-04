
n=int(input())

for i in range(n):
    for j in range(2*n-2*i-2):
        print(" ",end="")
    for j in range((2*i+2)//2):
        if (2*i+2)//2==1:
            print(1,end="")
        else:
            print(j+1,end=" ")
    for j in range(1,(2*i+2)//2):
        if (2*i+2)//2-j==1:
            print((2*i+2)//2-j,end="")
        else:
            print((2*i+2)//2-j,end=" ")
    print()