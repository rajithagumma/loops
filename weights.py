i=1
sum=0
while i<=11:
    weight=int(input("enter weight:"))
    i=i+1
    sum=weight+sum
print(sum/11)
if (sum/11)%5==0:
    print("divisible by 5")
else:
     print("not divisible by 5")




