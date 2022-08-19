n=int(input("entre the number:"))
sum=1
i=1
while i<=n:
    f=1
    b=1
    while b<=i:
        f=f*b
        sum=sum+(1/f)
        print(sum)
        b=b+1
    i=i+1
