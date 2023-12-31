
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input("Введите длину первой стороны треугольника: "))
b = int(input("Введите длину второй стороны треугольника: "))
c = int(input("Введите длину третьей стороны треугольника: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c or a + c > b or b + c > a:
        if a == b == c:
            print("Треугольник равносторонний")
        elif a == b or a == c or b == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")

    else:
        print("Треугольника с такими сторонами не существует")
else:
    print("Длина стороны не может быть отрицательной или равняться 0")