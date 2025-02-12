#reversing an integer

#taking user input 
n=int(input("enter a number to reverse:"))
t=n #initializing a temporary variable 
rev=0
#loop for iterations 
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10 
#printing the reversed digit 
print("The Reversed number is :",rev)
