a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=a+b
k=0
while c>0:
    r=c%2
    c=c//2
    k=k*10+r
i=0
while k>0:
    m=k%10
    i=i*10+m
    k=k//10



