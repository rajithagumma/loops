i=1
count=0
num=int(input("enter the numbefr:"))
while i<=num:
    i=i+1
    if num%i==0:
        count=count+1
if count==2:
    print("prime number")
else:
    print("not a prime number")
