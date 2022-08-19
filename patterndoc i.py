n=int(input("enter the number of rows:"))
i=0
while i<n:
    k=1
    while k<5-i:
        print(" ",end='')
        k=k+1
    j=0
    while j<=i:
        print(i+1,end="")
        j=j+1
    i=i+1
    print()
