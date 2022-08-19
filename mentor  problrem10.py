i=1
v=1
while i<=3:
    j=1
    while j<=3:
        if i==2 and j!=3:
            print(v+4,end=" ")
        elif (i==2 and j==3) or (i==3 and j==2):
            print(v-2,end=" ")
        elif i==3 and j==3:
            print(v-4,end=" ")
        else:
            print(v,end=" ")
        j=j+1
        v=v+1
    i=i+1
    print()