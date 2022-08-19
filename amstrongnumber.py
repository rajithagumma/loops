user=int(input("entre the number:"))
n=len(str(user))
i=user
sum=0
while user>0:
    a=user%10
    b=a**n
    sum=sum+b
    user=user//10
if sum==i:
    print("amstrong number")
else:
    print("not amstrong number")