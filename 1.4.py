length = int(input('Введите длину шоколадки m: '))
width = int(input('Введите ширину шоколадки n: '))
count = int(input('Введите число долек k, которые можно отломить по условию: '))
result = True
if count % length == 0 or count % width == 0:
    print(result)
else:
    print(not result)
