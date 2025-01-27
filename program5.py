n=int(input("enter a number"))
##user input for an integer 
t=n
rev=0
while n!=0:
	r=n%10
	rev=rev*10+r
	n=n//10
print ("reverse of the number",t,"is",rev)
