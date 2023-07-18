n=int(input())
s1=str(n)
sq=n*n
s2=str(sq)
s3=s2[len(s2)//2::]
if s1==s3:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")