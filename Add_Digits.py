n=int(input())
def add(n):
    s=0
    while(n!=0):
        r=n%10
        s=s+r
        n=n//10
    return s
while(1):
    r=add(n)
    if r<10:
        print(r)
        break
    else:
        n=r