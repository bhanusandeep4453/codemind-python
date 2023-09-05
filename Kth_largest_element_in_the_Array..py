n=int(input())
l=list(map(int,input().split()))
a=int(input())
b=set(l)
c=list(b)
for _ in range(a-1):
    c.remove(max(c))
print(max(c))