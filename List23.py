n = int(input())
a = []
for i in range(-2,n):
  a.append(i)
print(sorted(a, key=abs, reverse=1))