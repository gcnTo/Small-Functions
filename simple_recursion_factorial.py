def fact(n):
	if n==1:             # the base case 1! = 1
		return n 
	else:
		return n*fact(n-1) # * comes from the mathematical definition of factorial (n!), fact(n-1) is needed so that eventually we reach the base case

print(fact(5))
