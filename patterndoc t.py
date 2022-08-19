n=int(input("enter number of rows:"))
i=0
while i<n:
    k=0
    while k<n-i-1:
        print(" ",end="")
        k=k+1
    j=0
    while j<=i:
        print("*",end=" ")
        j=j+1
    i=i+1
    print()