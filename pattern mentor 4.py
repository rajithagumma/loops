from re import I


n=int(input("enter number of rows:"))
i=0
while i<n:
    j=i
    while j>=0:
        print(j,end=" ")
        j=j-1
    i=i+1
    print()