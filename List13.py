n = int(input())
a = []
for i in range(n):
  a.append(i)
  i+=1
last = a[-1]
a.pop()
print(last,a)