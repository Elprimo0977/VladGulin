n = int(input())
k = int(input())
a = []
for i in range(n+1):
  a.append(i)
  i+=1
print(a[k], a[-1], k)