r=7
c=6
i=1
while i<=r:
    j=1
    while j<=c:
        if (j==1) or (j==5 and i!=1 and i!=2 and i!=3 and i!=4) or (i==5 and j!=2 and j!=3)or (i==7 and j!=6) or i==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()
