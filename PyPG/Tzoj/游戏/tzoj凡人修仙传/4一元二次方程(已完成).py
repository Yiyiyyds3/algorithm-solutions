a,b,c=map(float,input().split())
if b**2-4*a*c>0:
    x1=(-b+(b**2-4*a*c)**0.5)/(2*a)+0.0
    x2=(-b-(b**2-4*a*c)**0.5)/(2*a)+0.0
    temp_max=max(x1,x2)
    temp_min=min(x1,x2)
    x1=temp_max
    x2=temp_min
    print(f"{x1:.2f} {x2:.2f}")
elif b**2-4*a*c==0:
    x1=-b/(2*a)+0.0
    x2=-b/(2*a)+0.0
    temp_max=max(x1,x2)
    temp_min=min(x1,x2)
    x1=temp_max
    x2=temp_min
    print(f"{x1:.2f} {x2:.2f}")
elif b**2-4*a*c<0:
    x1=-b/(2*a)+0.0
    x2=-b/(2*a)+0.0
    x3=0.0+abs((b**2-4*a*c)**0.5)/(2*a)
    x4=0.0-abs((b**2-4*a*c)**0.5)/(2*a)
    temp_max=max(x3,x4)
    temp_min=min(x3,x4)
    x3=temp_max
    x4=temp_min
    print(f"{x1:.2f}+{x3:.2f}i {x1:.2f}{x4:.2f}i")