def is_number(_str):
    try:
        int(_str)
        return _str
    except ValueError:
        return print(f'Вы ввели не число')