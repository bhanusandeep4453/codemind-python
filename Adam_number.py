def rev(n):
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    return r
n=int(input())
sq=n*n
rev1=rev(n)
rev2=rev1*rev1
print(rev(rev2)==sq)