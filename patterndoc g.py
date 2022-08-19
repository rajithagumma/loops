n=int(input("enter number of rows:"))
i=n
while i>0:
    j=n
    while j>=i:
        print(j,end="")
        j=j-1
    i=i-1
    print()