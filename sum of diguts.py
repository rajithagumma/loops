user=int(input("enter the number:"))
i=0
sum=0
while user%10!=0:
    r=user%10
    i=i*10+r
    sum=sum+r
    user=user//10
    print(sum)