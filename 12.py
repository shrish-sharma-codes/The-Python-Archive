def count_a(s):
if s=='':
return 0
return (s[0]=='a')+count_a(s[1:])
print(count_a(input('enter string ')))
