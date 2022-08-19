user=int(input("enter the number:"))
num=user
i=0
while user>0:
    a=user%10
    i=i*10+a
    user=user//10
if i==num:
    print("palindrome")
else:
    print("not")