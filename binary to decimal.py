n=int(input("enter the number:"))
len=len(str(n))
i=0
k=0
while i<len:
    r=n%10
    k=k+r*2**i
    i=i+1
    n=n//10
print(k)