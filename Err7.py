while True:
  try:
    a = int(input())
  except ValueError:
    print("Это не число. Поробуй еще")
    continue
  break
print(a)