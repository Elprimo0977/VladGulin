n = int(input())
if n%2 ==0:
  l = 2
else:
  l = 1
k = 1
while n>=l:
  k *=n
  n -=2
print(k)