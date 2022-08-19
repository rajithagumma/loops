n=int(input("enter number of rows:"))
i=1
while i<=n:
    k=n-1
    while k>=i:
        print(" ",end="")
        k=k-1
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    i=i+1
    print()

