D5 = {}
n = int(input('enter no of students '))
for i in range(n):
 erno, phy, chem, maths = input('enter enrolment number and marks in phy chem and maths ATRE MADARCHOD')
 D5.update({erno: (int(phy), int(chem), int(maths))})
print(D5)

details = [False, False, False, False]
r = input("which information do you want to print\nname? 'y' or 'n'")
if r == 'y':
 details[0] = True
r = input("city? 'y' or 'n'")
if r == 'y':
 details[1] = True
r = input("state? 'y' or 'n'")
if r == 'y':
 details[2] = True
r = input("phone number? 'y' or 'n'")
if r == 'y':
 details[3] = True
n = int(input('enter no. of students'))
D = {}
for i in range(n):
 name, city, state, phone = input('enter name, city, state, phone number separated by comma
').split(',')
 D.update({name: (name, city, state, phone)})
n = input('enter name ')
for i in range(4):
 if details[i]:
 print(D.get(n)[i], end=' ')

