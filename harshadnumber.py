n=int(input("enter the number:"))
a=n
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=n//10
if a%sum==0:
    print("harshad number")
else:
    print("not a harshad number")