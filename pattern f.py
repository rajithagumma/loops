r=6
c=4
i=1
while i<=r:
    j=1
    while j<=c:
        if i==1 or i==3 or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()