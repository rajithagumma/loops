n=int(input("enter number of rows:"))
i=1
while i<=n:
    k=n
    while k<n:
        print(" ",end=" ")
        k=k+1
    j=1
    while j<=i+2:
        print("*",end=" ")
        j=j+1
    i=i+1
    print()