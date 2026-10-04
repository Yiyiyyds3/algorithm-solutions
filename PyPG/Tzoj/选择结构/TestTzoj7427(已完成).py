n=input()
q=''
if len(n)<5:
    if len(n)==4 and n[-4]>='5':
        q+='1'
        print(q+'0'*4)
    else:
        print('0')
        
elif n[-4]>='5':
    num=int(n[0:-4])
    num+=1
    print(str(num)+'0'*4)
else:
    new_n=n[:-4]+'0'*4
    print(new_n)