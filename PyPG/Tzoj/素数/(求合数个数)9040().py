# from math import sqrt,floor
# def euler_sieve(n):
#     primes=bytearray([1])*(n+1)
#     primes[0]=primes[1]=0
#     prime=[]
#     for i in range(2,n+1):
#             if primes[i]:
#                 prime.append(i)
#             for j in prime:
#                 if i*j>n:
#                     break
#                 primes[i*j]=0
#                 if i%j==0:
#                     break
#     return primes


# n=int(input())
# primes=euler_sieve(int(floor(sqrt(n))))
# print(primes)


