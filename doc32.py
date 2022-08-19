from re import I


n=int(input("enter the number:"))
sum_even=0
sum_odd=0
i=2
while i<=n:
    if i%2==0:
        a=i**2
        sum_even=sum_even+a
    else:
        b=i**2
        sum_odd=sum_odd+b
    i=i+1
print(1+sum_even-sum_odd)
