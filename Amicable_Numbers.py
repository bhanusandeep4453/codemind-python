def div(n):
    s=0
    for i in range(1,1+int(n/2)):
        if n%i==0:
            s+=i
    return s
n=int(input())
m=int(input())
if div(n)==m and div(m)==n:
    print("Amicable")
else:
    print("Not Amicable")