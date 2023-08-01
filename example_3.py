dict = dict(axe = 10, sleepbag = 40, termos = 5, cup = 15, lasso = 13, light = 7, firecheck = 4, books = 2, knife = 2,)
bag = int(input('Введите грузоподъемность Вашего рюкзака: '))
total = 0
for keys,values in dict.items():
    if values <= (bag - total):
        total += values
        print(f'Упаковываем в рюкзак: {keys}, весом {values} кг. Осталось свободного места {bag - total}')
    else:
        continue