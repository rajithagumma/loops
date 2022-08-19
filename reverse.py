user=int(input("entre the number:"))
i=0
while user>0:
    r=user%10
    i=i*10+r
    user=user//10
print("reverse number is",i)
