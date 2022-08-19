from re import I


n=int(input("enter the nth term:"))
f=1
i=1
sum=0
while i<=n:
    f=f*i
    sum=sum+(1/f)
    i=i+1
    print(sum)
