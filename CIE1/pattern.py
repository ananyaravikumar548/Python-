#printing a specific pattern 
#taking user input 
n=int(input("enter number of lines:"))
#loops for iterations 
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
        
    print()#printing the sequence 
