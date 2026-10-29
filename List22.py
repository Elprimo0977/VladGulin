n = int(input())
a = []
d = int(input())
s = 0
for i in range(n):
  if i == d:
    s +=1
  a.append(i*d)
print(a,s)