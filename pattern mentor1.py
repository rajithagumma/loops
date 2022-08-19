n=int(input("enter the number of rows:"))
i=1
while i<=n:
    k=1
    while k<=n-i:
        print(" ",end="")
        k=k+1
    j=i
    while j>=1:
        print(j,end="")
        j=j-1
    m=2
    while m<=i:
        print(m,end="")
        m=m+1
    i=i+1
    print()
# num=int(input("enter number:"))
# i=0
# sum=0
# while i<num:
#     user=int(input("enter user:"))
#     sum=sum+user
#     i=i+1
# print(sum)
# k=0
# while sum>0:
#     r=sum%10
#     k=k+r
#     sum=sum//10
# print(k)
# if k%2==0:
#     print("perfect even number")
# else:
#     print("odd number")
# n=int(input("enter the number:"))
# i=0
# c=0
# a=str(n)

# while i<len(a):
#     if (a[0])=="1":
#         c=c+1
# print(c)

