a = input()
b = input()
try:
sum = int(a) + int(b)
diff = int(a) - int(b)
except ValueError:
if a.isnumeric() is False and b.isnumeric() is False:
sum = 0
diff = 0
elif a.isnumeric() is False:
sum = int(b)
diff = -int(b)
else:
sum = int(a)
diff = int(a)
try:
print(sum % diff)
except ZeroDivisionError:
print("Zero Division error occurred")
