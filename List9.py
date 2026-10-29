n = int(input())
a = []
for i in range(n):
  a.append(i)
  i+=1
sred = sum(a)/n
z = []
for x in a:
  if x>sred:
    z.append(x)
print(z, len(z))