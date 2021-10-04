# input the number
P=int(input('Enter a number: '))

# converting to binary
s=int(bin(P)[2:])

# reversing the binary 
r=str(s)[::-1] 

# checking the palindrome
if int(r)==s:
    print("The binary representation of the number is a palindrome.")
else:
    print("The binary representation of the number is not a palindrome.")
