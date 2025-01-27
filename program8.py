n=int(input("enter a number"))
##user input for an integer 
print("the value of n",n)
t=n
rev=0
while n!=0:
	r=n%10
	print("value of r is ",r)
	rev=rev*10+r
	print("value of rev is",rev)
	n=n//10
	print("value of n is ",n)
print ("reverse of the number",t,"is",rev)
