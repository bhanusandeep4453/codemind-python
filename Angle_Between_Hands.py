h,m=map(int,input().split(":"))
a=h*30
b=m/12
a+=b*6
b=m*6
x=abs(a-b)
y=360-x
if (x<y): print(x)
else: print(y)