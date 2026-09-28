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
sila = health - (agility * endurance)

print()
print("Характеристики героя:")
print(f"Здоровье:        {health}")
print(f"Сила:            {strength}")
print(f"Ловкость:        {agility}")
print(f"Выносливость:    {endurance}")
print()
print(f"Урон героя:       {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил:        {sila}")
print()

print("Что делаешь?")
print("1 - осмотреться")
print("2 - идти вперёд")
print("3 - отдохнуть")
print("4 - прислушаться")
print("5 - включить фонарь")
print()
choice = int(input())
print(frame)