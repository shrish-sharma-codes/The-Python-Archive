def area_cyclinder( h, d):
	area = 22/7*(d/2)*(d/2) + 2*22/7*(d/2)*h
	print(“Area of cylinder = {}”.format(area))

d  = float(input(“Enter the diameter of cylinder”))
h = float(input(“Enter the height of cylinder”))
area_cyclinder(h,d)
