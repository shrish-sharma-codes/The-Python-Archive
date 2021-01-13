# Program to sort a list
L = []

# Sorting List function
def sorting_list_num(L):
    L.sort()
    print(L)

def sorting_list_alpha(L):
    x = sorted(L)
    print(x)
    
# Type
t = int(input("Type 1 for Numerical List and 2 for Alphabetical list:"))

if t == 1:
    # Taking Size
    n = int(input('Enter the Size:'))

    # Inserting Elements
    i = 0
    while(i != n):
        e = int(input('Enter Element ' + str(i) + ":"))
        L.append(e)
        i = i + 1    

    sorting_list_num(L)
else:
    print("Enter elements and press x to stop:")
    ch = 'a'
    while(ch != 'x'):
        ch = input("Enter Element:")
        L.append(ch)
    sorting_list_alpha(L)
    
    
