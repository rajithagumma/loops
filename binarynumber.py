num=int(input("enter the number:"))
b=0
p=1
n=num
while n>0:
    rem=n%2
    b+=rem*p
    p=p*10
    n=n/2
    print(b)