while True:
  try:
    age = int(input())
  except ValueError:
    print("Отклонено")
    continue
  if 1 <= age <= 120:
    break
  else:
    print("Возраст вне допустимого диапазона")
print(f"Принято: {age}")