try:
  a = int(input())
  b = int(input())
  print(f"{a / b:.2f}")
except (ValueError, ZeroDivisionError):
  print("Посчитать не удалось")