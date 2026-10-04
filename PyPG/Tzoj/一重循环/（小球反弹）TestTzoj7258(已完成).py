# from math import *
# w,h,n=map(int,input().split())

# for i in range(n):
#     s=input().split()
#     x=int(s[0])
#     y=int(s[1])
#     t=int(s[2])
#     c=s[3]
#     if c=='R':
#         n_x=x+t
#         if n_x<w:
#             print(n_x,y)
#         elif n_x==w:
#             print(w,y)
#         else:
#             collide=ceil(n_x/w)
#             if collide%2==0:
#                 print(n_x%w,y)
#             else:
#                 print(w-(n_x%w),y)
#     elif c=='L':
#         n_x=x-t
#         if n_x>0:
#             print(n_x,y)
#         elif n_x==0:
#             print(0,y)
#         else:
#             n_x=abs(n_x)
#             collide=ceil(n_x/w)
#             if collide%2==0:
#                 print(w-(n_x%w),y)
#             else:
#                 print(n_x%w,y)
#     elif c=='D':
#         n_y=y+t
#         if n_y<h:
#             print(x,n_y)
#         elif n_y==h:
#             print(x,h)
#         else:
#             collide=ceil(n_y/h)
#             if collide%2==0:
                
#                 print(x,n_y%h)
#             else:
#                 print(x,h-(n_y%h))

#     elif c=='U':
#         n_y=y-t
#         if n_y>0:
#             print(x,n_y)
#         elif n_y==0:
#             print(x,0)
#         elif n_y%h==0:
#             print(x,h)
#         else:
#             n_y=abs(n_y)
#             collide=ceil(n_y/h)
#             if collide%2==0:
#                 print(x,h-(n_y%h))
#             else:
#                 print(x,n_y%h)

#周期函数折叠来当模，把弹问题换成直线问题
w, h, n = map(int, input().split())

def bounce(p, d, size):
    p += d
    period = 2 * size
    mod = p % period
    return mod if mod <= size else period - mod

for _ in range(n):
    x, y, t, c = input().split()
    x, y, t = int(x), int(y), int(t)

    dx = dy = 0
    if c == 'R': dx = t
    if c == 'L': dx = -t
    if c == 'D': dy = t
    if c == 'U': dy = -t

    print(bounce(x, dx, w), bounce(y, dy, h))