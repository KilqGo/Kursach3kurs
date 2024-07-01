with open('Saves.txt', 'r') as fp:
    first = fp.readlines()[0]
fsmod = first

def fsmodeswap():
    try:
        with open('Saves.txt', 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Файл не найден: Saves.txt")
        return

    if not lines:
        print(f"Файл Saves.txt пуст.")
        return

    first_line = lines[0].strip().lower()

    if first_line == 'true':
        inverted_value = 'false'
    elif first_line == 'false':
        inverted_value = 'true'
    else:
        print(f"Некорректное значение в первой строке: {first_line}")
        return

    try:
        with open('Saves.txt', 'w') as file:
            file.write(inverted_value + '\n')
            for line in lines[1:]:
                file.write(line)
    except IOError:
        print(f"Ошибка записи в файл: Saves.txt")
        return

    print(f"Значение в первой строке файла Saves.txt успешно инвертировано: {inverted_value}")
    return inverted_value

fsmodeswap()

