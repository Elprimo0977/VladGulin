n = int(input())
a = []
for i in range(-5,n+1):
  a.append(i)
  if i<0:
    a.remove(i)
print(a, len(a))