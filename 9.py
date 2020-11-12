l1 = list(input().split())
l2 = list(input().split())
l3 = []
for i in range(max(len(l1), len(l2))):
try:
l3.append(int(l1[i]) + int(l2[i]))
except IndexError:
if i >= len(l1) and l2[i].isnumeric():
l3.append(int(l2[i]))
elif i >= len(l2) and l1[i].isnumeric():
l3.append(int(l1[i]))
else:
l3.append(0)
except ValueError:

if l1[i].isnumeric() is False and l2[i].isnumeric() is False:
l3.append(0)
elif l1[i].isnumeric() is False:
l3.append(int(l2[i]))
else:
l3.append(int(l1[i]))
print(l3)
