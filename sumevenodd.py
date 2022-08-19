sum_even=0
sum_odd=0
i=1
while i<=100:
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
    i=i+1
print(sum_even)
print(sum_odd)
