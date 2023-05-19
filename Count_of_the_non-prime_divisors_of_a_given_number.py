def isprime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return True
    else:
        return False
n=int(input())
c=0
for j in range(1,n+1):
    if n%j==0:
        if isprime(j)!=True:
            c=c+1
print(c)