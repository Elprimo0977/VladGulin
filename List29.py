a = []
n = int(input())
k = int(input())
for i in range(n):
  a.append(i)
a.sort(reverse=1)
print(a[:k])