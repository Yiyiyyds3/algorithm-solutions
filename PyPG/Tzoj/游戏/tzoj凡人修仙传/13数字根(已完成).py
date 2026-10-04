
while True:
    n=input()
    if n=='0':
        break
    nums=0
    #加法结合律，分开求和全部加起来求是一样的
    for i in range(len(n)):
        nums+=int(n[i])
    while nums>=10:
        nums=sum(int(i) for i in str(nums))
    print(nums)