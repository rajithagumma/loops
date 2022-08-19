n=int(input("enter no.of rows:"))
i=1
num=1
while i<=n:
	j=1
	while j<=n:
		print(num,end="")
		j=j+1
		num=num+1
	num=num-2	
	i=i+1
	print()
