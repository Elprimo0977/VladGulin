n = int(input())
a = []
b = []
for i in range(n+1):
  a.append(i)
sred = sum(a)/len(a)
for i in a:
  if i > sred:
    b.append(i)
print(b,sred)