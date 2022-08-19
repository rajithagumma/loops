r=7
c=5
i=1
while i<=r:
    j=0
    while j<=c:
        if (j==1) or (j==5 and i!=1 and i!=4 and i!=7) or (i==1 or i==4 or i==7) and (j>1 and j<5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i+=1
    print()