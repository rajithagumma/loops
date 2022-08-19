n=int(input("enter the nth term :"))
x=int(input("enter the valaue of x:"))
i=1
sum=0
f=1
while i<=n:
    f=f*i
    sum=sum+(x**i/f)
    i=i+1
    print(1+sum)