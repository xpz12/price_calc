# Вводится изначальная цена
initial_price = int(input('Введите изначальную цену: '))
# Вводится колво покупок
num_purchases = int(input('Введите количество покупок: '))

def calculate_final_price(initial_price, num_purchases):
    final_price = 0
    current_price = initial_price
    
    for _ in range(num_purchases):
        current_price -= current_price * 0.11  # Уменьшаем текущую цену на 11%
        final_price += current_price  # Складываем уменьшенную цену

    # Округляем конечную сумму и форматируем с разделением тысяч
    return f"{round(final_price):,}".replace(",", ".")

# Расчет финальной цены
final_price = calculate_final_price(initial_price, num_purchases)

# Формула округления числа
def format_number(final_price):
    # Округляем число
    rounded_number = round(final_price)
    # Форматируем число с разделением тысяч
    return f"{rounded_number:,}".replace(",", ".")

# Рассчитываем и выводим конечный результат
formatted_final_price = calculate_final_price(initial_price, num_purchases)
print(f"Конечная сумма после всех покупок: ${formatted_final_price}")