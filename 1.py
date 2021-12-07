print('Введите имя, фмилию и год рождения:')
name, surname, birth = map(str, input().split())
print(f'{name}_{surname}_{birth}')
name, surname = surname, name
birth = int(birth) + 60
print(f'{name}_{surname}_{birth}')
