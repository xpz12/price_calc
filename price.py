# Вводится изначальная цена
a = int(input('Введите изначальную цену: '))
# Вводится колво покупок
l = int(input('Введите количество покупок: '))

# Формула финальной цены
def calculate_final_price(a, l):
    final_price = a
    for i in range(l):
        final_price += final_price * 0.11
    return final_price

# Расчет финальной цены
final_price = calculate_final_price(a, l)

# Формула округления числа
def format_number(final_price):
    # Округляем число
    rounded_number = round(final_price)
    # Форматируем число с разделением тысяч
    return f"{rounded_number:,}".replace(",", ".")

# Округление
final_price = format_number(final_price)

# Вывод результата
print(f'Вам нужно ${final_price} чтобы купить {l} раз')
