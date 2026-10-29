try:
  a = input()
  b = int(input())
  print(a[b])
except IndexError:
  print("Нет такого символа")
except ValueError:
  print("Ошибка ввода")