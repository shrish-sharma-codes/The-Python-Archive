def fnc(s):
ans = ''
VowelsSpaces = ['a', 'e', 'i', 'o', 'u', ' ']
for i in s:
if i not in VowelsSpaces:
ans += i + 'o' + i
else:
ans += i
return ans
print(fnc(input()))
