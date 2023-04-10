count = int(input('Введите число: '))
if count % 6 == 0:
    min_count = int(count / 6)
    print(f'Количество журавликов сделал Петя: {min_count}, Катя: {min_count*4}, Сережа: {min_count}')
else:
    print('Невозможно определить')
