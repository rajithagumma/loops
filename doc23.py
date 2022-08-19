i=0
l=0
s=1000
while i<10:
    n=int(input("entre the number:"))
    if n>l:
        l=n
    elif n<s:
        s=n
    i=i+1
print('largest number is',l)
print('smallest number is',s)
