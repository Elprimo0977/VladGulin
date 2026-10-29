import random
z = random.randint(1,10)
b = []
for x in range(z):
  b.append(x)
  x+=1
n = random.randint(1,10)
a = []
for i in range(n):
  a.append(i)
  i+=1
m = random.randint(1,10)
c = []
for r in range(m):
  c.append(r)
  r+=1
if len(a)>len(b) and len(b)>len(c):
  print(len(a))
elif len(b)>len(a) and len(a)>len(c):
  print(len(b))
else:
  print(len(c))
print(len(a),len(b),len(c),)