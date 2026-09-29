title = 'ТЕМНЫЙ КВАРТАЛ'
frame = '=' * 20
print(frame)
print('   ' + title + '   ')
print(frame)
print("Как зовут героя?")
hero_name = input()
print(f'Добро пожловать, {hero_name}!')
print("Ты зашел в темный квартал. Здесь темно и тихо.")
print()

print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")
health = int(input())
strength = int(input())
agility = int(input())
endurance = int(input())
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = (health//2 + agility + endurance) // 2

print()
print("Характеристики героя:")
print(f"Здоровье:        {health}")
print(f"Сила:            {strength}")
print(f"Ловкость:        {agility}")
print(f"Выносливость:    {endurance}")
print()
print(f"Урон героя:       {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил:        {stamina}")
print()

print("Что делаешь?")
print("1 - осмотреться")
print("2 - идти вперёд")
print("3 - отдохнуть")
print("4 - прислушаться")
print("5 - включить фонарь")
print()
choice = input()
match choice:
  case "1":
    print("Вы осмотрелись. Кругом темнота")
  case "2":
    stamina = stamina - 8
    print("Вы осторожно идёте вперёд. Ботинки стучат по плитке.")
  case "3":
    stamina = stamina + 6
    print("Вы отдохнули.")
  case "4":
    print("Вы услышали стук капель дождя по крышам домов")
  case "5":
    stamina = stamina -1
    print("Фонарь оказался нерабочим.")
  case _:
    print("Такого действия нет.")
print()
print(f"Здоровье: {health} Запас сил: {stamina}")
print(frame)