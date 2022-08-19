from re import M


n=int(input("enter the number:"))
k=0
while n>0:
    r=n%2
    n=n//2
    k=k*10+r
i=0
while k>0:
    m=k%10
    i=i*10+m
    k=k//10
print(i)


