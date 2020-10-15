def simple_interest(p,t, r):
	si = (p*r*t)/100
	print(“si = {}”.format(si))

p = float(input(“Enter the principal amount”))
r = float(input(“Enter the rate”))
t = int(input(“Enter the time”))
simple_interest(p,t,r)
