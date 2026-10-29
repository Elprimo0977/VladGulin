n = int(input())
d = int(input()) 
a = []
for i in range(n):
  a.append(i)
  i+=1
c = 0
if d in a:
  c+=1
  print(a[d])
else:
  print(-1)
print(a,c)