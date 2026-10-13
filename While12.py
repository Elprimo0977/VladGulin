n = int(input())
s = 1
k = 1
while s < n:
  k += 1
  s = sum(range(1,k+1))
print(s,k)