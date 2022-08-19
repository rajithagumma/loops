n=int(input("enter the number of rows:"))
i=0
while i<n:
    j=n
    while j>i:
        print(j,end="")
        j=j-1
    i=i+1
    print()