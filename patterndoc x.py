n=int(input("enter number of rows:"))
i=0
k=ord("A")
while i<n:
    j=0
    while j<=i:
        print(chr(k),end=" ")
        j=j+1
    k=k+1
    i=i+1
    print()
