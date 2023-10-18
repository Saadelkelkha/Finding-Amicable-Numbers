n=int(input("Type the first number"))
m=int(input("Type the second number"))
f=0
d=0
for i in range (2,n) :
    if n%i==0 :
        d=d+i
for i in range (2,m) :
    if m%i==0 :
        f=f+i
if d==m and f==n :
    print("The two numbers are friends")
else :
    print("The two numbers are not friends")