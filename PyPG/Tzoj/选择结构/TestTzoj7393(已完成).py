a,b=input().split()
c=a+b
c=''.join(sorted(c))#sorted给字符串排序时候需要手动拼接
if c=="24": #风(0)、水(1)、雷(2)、冰(3)、火(4)、岩(5)、草(6)
    print(0) 
elif c=="23":
    print(1)
elif c=="12":
    print(2)
elif c=="14":
    print(3)
elif c=="34":
    print(4)
elif c=="13":
    print(5)
elif c=="01" or c=="02" or c=="03" or c=="04":
    print(6)
elif c=="15" or c=="25" or c=="35" or c=="45":
    print(7)
elif c=="46":
    print(8)

#超载(0)、超导(1)、感电(2)、蒸发(3)、融化(4)、冻结(5)、扩散(6)、结晶(7)、点燃(8)
#2 4 0/ 2 3 1/1 2 2/ 1 4 3/3 4 4/1 3 5/0 1234 6/5 1234 7/4 6 8

