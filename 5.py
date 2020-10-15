D4 = {}
n = int(input('enter no of students '))
for i in range(n):
 erno, state = input('enter enrolment number and state ').split()
 D4.update({erno: state})
print(D4)

