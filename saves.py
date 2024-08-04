def str_to_bool(value_str):
    if value_str.lower() == 'true':
        return True
    elif value_str.lower() == 'false':
        return False
    else:
        raise ValueError(f"Некорректное значение: '{value_str}'. Ожидается 'true' или 'false'.")

with open('Saves.txt', 'r') as fp:
    first = fp.readlines()[0].strip()
    _fsmod = str_to_bool(first)

def fsmodeswap():
    global _fsmod
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
    _fsmod = str_to_bool(inverted_value)
    print(f"Значение полноэкранного режима Saves.txt изменено: {inverted_value}")
    return inverted_value

def fsmod():
    return _fsmod

# --------------------------------------------------------------------------


class Stats:
    Fortitude = 1
    Prudence = 1
    Justice = 1
    basehp = Fortitude*10
    basesp = Prudence*10
    basedmg = Justice*5
    hpdefence = 100
    spdefence = 100
    bothdefence = 100
    persdefence = 100

