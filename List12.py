n = int(input())
k = int(input()) #>0,<n
a = []
for i in range(n):
  a.append(i)
  i+=1
a.insert(k, 0)
print(a, len(a))