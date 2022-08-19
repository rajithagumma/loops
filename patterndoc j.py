n=int(input("enter the number of rows:"))
i=0
while i<n:
    k=1
    while k<n-i:
        print(" ",end="")
        k=k+1
    j=0
    while j<=i:
        print(j+1,end="")
        j=j+1
    i=i+1
    print()
a=4512
b=str(a)
c=0
sum=0
while c<len(b):
    d=b[c]
    e=int(d)
    sum=sum+(e**2)
    print(sum)
    c=c+1
