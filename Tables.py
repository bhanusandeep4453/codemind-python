a,b=map(int,input().split())
for i in range(1,b+1):
    if(i%2!=0):
        x=a*i
        print(f"{a} x {i} = {x}")