n = 5
# Upper part of the pattern
for i in range(n-1,0,-1):
    print(" "* (n-i) + "*" *(2*i-1))
