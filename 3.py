D2 = {}
n = int(input('Enter no of students '))
for i in range(n):
 erno, city = input('Enter Enrolment number and city ')
 D2.update({erno: city})
print(D2)
