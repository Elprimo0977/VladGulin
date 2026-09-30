n = int(input())
c = 1
for i in range(1,n+1):
  x = i*0.1 + 1
  c*=x
  print(x)
print(c)