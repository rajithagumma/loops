a=int(input("enter the number:"))
b=int(input("enter the number:"))
sum=0
while a<=b:
    if a%2==0:
        sum=sum+a
    a+=1
print(sum)
