D5 = {}
n = int(input('enter no of students '))
for i in range(n):
 erno, phy, chem, maths = input('enter enrolment number and marks in phy chem and maths')
 D5.update({erno: (int(phy), int(chem), int(maths))})
print(D5)
#Suggest Changes
