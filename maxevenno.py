# Python code to find the maximum EVEN number 

n = 0		# loop counter
num = 0		# to store the input
maxnum = 0	# to store maximum EVEN number

# loop to take input 10 number
while n<10:
    num = int(input("Enter your number: "))
    if num%2 == 0:
        if num > maxnum:
            maxnum = num
    n += 1

# printing the 	maximum even number
print("The maximum EVEN number :",maxnum)
