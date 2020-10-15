def compound_interest( p, t, r, n):
	Ci = p*pow((1+r/n),t*n)
	print(“compound interest = {}”.format(CI))

p = float(input(“Enter the principal amount”))
r = float(input(“Enter the rate”))
t = int(input(“Enter the time”))
n = int(input(‘Enter the number of times interest applied per time period’))
compound_interest(p,t,r,n)
