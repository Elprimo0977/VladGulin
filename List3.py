n = int(input())
a = []
c = []
for i in range(1,n+1):
  a.append(i)
  i+=1
b = 1
c = a[::2]
for x in c:
  b *=x
print(sum(a), b)