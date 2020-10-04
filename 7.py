D6 = {}
n = int(input('enter no of students '))
for i in range(n):
 erno, email = input('enter enrolment number and email id ')
 D6.update({erno: email})
print(D6)
