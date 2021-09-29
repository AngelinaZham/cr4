print('Введите величины катетов: ')
cat1, cat2 = map(int, input().split())
hyp = (cat1 ** 2 + cat2 ** 2) ** 0.5
print('Площадь: ', 0.5 * cat1 * cat2)
print('Периметр: ', cat1 + cat2 + hyp)