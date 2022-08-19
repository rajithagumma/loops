r=6
c=5
i=1
while i<=r:
    j=1
    while j<=c:
        if (i==1 and j==1) or (i==1 and j==5):
            print(" ",end=" ")
        elif i==4 or j==1 or j==5 or i==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    i=i+1
    print()