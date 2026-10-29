n = int(input())
a = []
for i in range(1,n+1):
  a.append(i)
  i+=1
b = a[::2]
print(b,sum(b))