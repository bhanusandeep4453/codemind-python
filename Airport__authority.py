n=int(input())
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
y=int(input())
c=0
for i in l:
    if i<=y:
        c+=1
    else:
        c+=2
print(c)