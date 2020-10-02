D2 = {}
n = int(input('Enter no of students '))
for i in range(n):
 erno, city = input('Enter enrolment number and City ')
 D2.update({erno: city})
print(D2)
