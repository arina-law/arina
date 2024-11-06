result = []

def divider(a, b):
    if a < b:
        raise ValueError("Первый аргумент должен быть больше или равен второму")
    if b > 100:
        raise IndexError("Второй аргумент должен быть меньше или равен 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 6: 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (TypeError, ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Ошибка: {e}")

print(result)