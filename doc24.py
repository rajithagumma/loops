a=100
b=500
sum_even=0
sum_odd=0
while a<=b:
    if a%2==0:
        sum_even=sum_even+a
    else:
        sum_odd=sum_odd+a
    a=a+1
print(sum_even)
print(sum_odd)