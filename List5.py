n = int(input())
d = int(input())
a = []
for i in range(n):
  a.append(i)
  i+=1
a.append(d)
print(a, len(a))