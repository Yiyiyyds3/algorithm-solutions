h1,m1,s1=map(int,input().split(':'))
h2,m2,s2=map(int,input().split(':'))
if h2<h1:
    h2+=24
if m2<m1:
    m2+=60
    h2-=1
if s2<s1:
    s2+=60
    m2-=1
print(f"{h2-h1:02d}:{m2-m1:02d}:{s2-s1:02d}")
print("Happy New Year!")