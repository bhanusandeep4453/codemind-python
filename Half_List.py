n=int(input())
lt=list(map(int,input().split()))
x=lt[:n//2:]
y=lt[n//2::]
y.reverse()
for i in y+x:
    print(i,end=' ')