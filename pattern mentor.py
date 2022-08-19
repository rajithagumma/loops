# n=int(input("enter number of rows:"))
# i=0
# num=1
# while i<n:
#     j=0
#     while j<=i:
#         print(num,end=" ")
#         j=j+1
#         num+=1
#     i+=1
#     print()
# n=int(input("enter number of rows:"))
# i=0
# num=1
# while i<n:
#     j=0
#     while j<=i:
#         print(num,end=" ")
#         j=j+1
#         num+=2
#     i+=1
#     print()
n=int(input("enter the number:"))
a=n
f=1
sum=0
while n>0:
    r=n%10
    i=1
    while i<=r:
        f=f*i
        i=i+1
    n=n//10
    sum=sum+f
if a==sum:
    print("strong number")
else:
    print("not")