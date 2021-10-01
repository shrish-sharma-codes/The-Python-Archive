food = ["beans", "gazar-halwa", "roti", "sabzi", "achaar", "chhole", "bhature", "lox", "lemonade"]
fifth = []
for x in food:
try:
fifth.append(x[4])
except IndexError:
fifth.append('N')
print(fifth)
