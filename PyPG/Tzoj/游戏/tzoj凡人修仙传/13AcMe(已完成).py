import sys
num_c={}

for i in sys.stdin:
    for c in range(97,123):
        num_c[chr(c)]=0
    for j in i:
        if j=='a':
            num_c[j]+=1
        elif j=='b':
            num_c[j]+=1
        elif j=='c':
            num_c[j]+=1
        elif j=='d':
            num_c[j]+=1
        elif j=='e':
            num_c[j]+=1
        elif j=='f':
            num_c[j]+=1
        elif j=='g':
            num_c[j]+=1
        elif j=='h':
            num_c[j]+=1
        elif j=='i':
            num_c[j]+=1
        elif j=='j':
            num_c[j]+=1
        elif j=='k':
            num_c[j]+=1
        elif j=='l':
            num_c[j]+=1
        elif j=='m':
            num_c[j]+=1
        elif j=='n':
            num_c[j]+=1
        elif j=='o':
            num_c[j]+=1
        elif j=='p':
            num_c[j]+=1
        elif j=='q':
            num_c[j]+=1
        elif j=='r':
            num_c[j]+=1
        elif j=='s':
            num_c[j]+=1
        elif j=='t':
            num_c[j]+=1
        elif j=='u':
            num_c[j]+=1
        elif j=='v':
            num_c[j]+=1
        elif j=='w':
            num_c[j]+=1
        elif j=='x':
            num_c[j]+=1
        elif j=='y':
            num_c[j]+=1
        elif j=='z':
            num_c[j]+=1
    for i in num_c:
        print(f"{i}:{num_c[i]}")
    print()