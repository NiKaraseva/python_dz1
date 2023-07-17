
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке

COLOUMNS = 4
ROWS = 2

for i in range(ROWS):
    for j in range(2, 11):
        line = ""
        for k in range(COLOUMNS):
            table_num = k * ROWS + i + 2
            if table_num > 9:
                break
            line += f"{table_num} x {j} = {table_num * j}\t   "
        print(line)
    print("–––––––––––––––––––––––––––")

