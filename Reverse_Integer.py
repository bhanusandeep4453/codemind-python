n=int(input())
if n>0:
    t=n
    s=0
    while n!=0:
        r=n%10
        s=(s*10)+r
        n=n//10
    print(s)
else:
    n=-1*n
    t=n
    s=0
    while n!=0:
        r=n%10
        s=(s*10)+r
        n=n//10
    print(-s)