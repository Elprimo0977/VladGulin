import math
def triangle_ps(a):
  p = a*3
  s = (a**2)*math.sqrt(3/4)
  print(p,s)
for i in range(1,4):
  triangle_ps(i)