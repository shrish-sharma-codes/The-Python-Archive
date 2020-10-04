D2 = {}
n = int(input('Enter no of students '))
for i in range(n):
 erno, city = input('Enter the Enrollment Number and City:')
 D2.update({erno: city})
print(D2)

D = {}
n = int(input('enter no of students '))
for i in range(n):
 erno, name, email = input('enter enrolment number ,name, email')
 D.update({erno: (name, email)})
en_no = input('enter the enrolment number ')
print(D.get(en_no))

