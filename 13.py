def is_prime(a):
if a == 0 or a == 1:
return False
elif a == 2:
return True
else:
for i in range(2, int(a**0.5)+1):
if a % i == 0:
return False
return True
def all_prime(a, b):
for i in range(a, b):
if is_prime(i):
print(i, end=' ')
def main():
a, b = map(int, input().split())
all_prime(a, b)
