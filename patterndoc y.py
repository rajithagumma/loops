n=int(input("enter number of rows:"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end=" ")
        k=k+1
    j=i
    while j>=1:
        print("*",end=" ")
        j=j-1
    m=2
    while m<=i:
        print("*",end=" ")
        m=m+1
    i=i+1
    print()


