# Count the Repeating words in string


import collections
input_string=input(str())
output=collections.Counter(input_string)
# ans=output.count(1)
# ans = max(zip(output.values(), output.keys()))[1]
# for i in len(output.keys):
#     if(output(i)==1):
#         count=count+1

values = output.values()
values_list = list(values)
ans=values_list.count(1)
print(ans)