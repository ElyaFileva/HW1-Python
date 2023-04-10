number = int(input('Введите шестизначное число: '))
sum1 = 0
sum2 = 0
result = True
half_of_number1 = int(number//1000)
half_of_number2 = int(number % 1000)
while half_of_number1 != 0 or half_of_number2 != 0:
    sum1 = sum1+half_of_number1 % 10
    half_of_number1 = half_of_number1//10
    sum2 = sum2+half_of_number2 % 10
    half_of_number2 = half_of_number2//10
if sum1 == sum2:
    print(result)
else:
    print(not result)
