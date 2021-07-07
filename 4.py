D3 = {}
n = int(input('enter no of students '))
for i in range(n):
 erno, mob = input('enter enrolment number and Phone Number ').split()
 D3.update({erno: mob})
print(D3)
