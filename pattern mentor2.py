n=int(input("enter number of rows:"))
i=1
while i<=n:
    j=1
    k=ord("A")
    while j<=i:
        if i%2==0:
            print(chr(k),end=" ")
        else:
            print(j,end=" ")
        j=j+1
        k+=1
    i=i+1
    print()