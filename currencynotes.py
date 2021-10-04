notes = (2000,500,200,100,50,20,10,5,2,1)

amount = int(input("Enter Amount to be paid : "))

for C in notes:
    count = amount//C
    print("Note Value : ", C,'\tnumber of notes ',count)
    amount = amount%C
