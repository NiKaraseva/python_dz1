
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print


number = int(input("Введите число: "))

message = ""

MIN_VALUE = 1
MAX_VALUE = 999
ONE_DIGIT = 10
TWO_DIGIT = 100

if MIN_VALUE <= number <= MAX_VALUE:
    if number < ONE_DIGIT:
        result = number ** 2
        message = f"Квадрат цифры {number} = {result}"
    elif number < TWO_DIGIT:
        first_digit = number // 10
        second_digit = number % 10
        result = first_digit * second_digit
        message = f"Произведение двузначного числа {number} = {result}"
    else:
        # result = int(str(number)[::-1])
        first_digit = number // 100
        second_digit = (number // 10) % 10
        third_digit = number % 10
        message = f"Зеркальное отображение трёхзначного числа {number} = {third_digit, second_digit, first_digit}"
else:
    message = f"Введено некоректное значение, введите число от 1 до 999"

print(message)
