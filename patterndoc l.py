n=int(input("enter the number of rows:"))
i=0
num=1
while i<n:
    j=0
    while j<=i:
        print(num,end="")
        j=j+1
        num=num+1
    i=i+1
    print()
