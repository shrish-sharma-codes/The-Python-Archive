# Program to sort a list
L = []

# Sorting List function
def sorting_list(L):
    L.sort()
    print(L)

# Taking Size
n = int(input('Enter the Size:'))

# Inserting Elements
i = 0
while(i != n):
    e = int(input('Enter Element ' + str(i) + ":"))
    L.append(e)
    i = i + 1    

sorting_list(L)
    
