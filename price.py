# Вводится изначальная цена
initial_price = int(input('Введите изначальную цену: '))
# Вводится колво покупок
num_purchases = int(input('Введите количество покупок: '))

def calculate_final_price(initial_price, num_purchases):
    final_price = 0
    current_price = initial_price
    
    for _ in range(num_purchases):
        current_price += current_price * 0.11  # Уменьшаем текущую цену на 11%
        final_price += current_price  # Складываем уменьшенную цену

    # Округляем конечную сумму и форматируем с разделением тысяч
    formatted_price = f"{round(final_price):,}".replace(",", ".")

    # Форматируем с единицами измерения (M, B, T, Qa, Qi)
    formatted_with_units = format_with_units(final_price)

    return f"{formatted_price} ({formatted_with_units})"   

def format_with_units(value):
    units = [("Qi", 1e18), ("Qa", 1e15), ("T", 1e12), ("B", 1e9), ("M", 1e6)]
    
    for unit, threshold in units:
        if value >= threshold:
            return f"{value / threshold:.2f} {unit}"
    
    return f"{value:.2f}"

# Рассчитываем и выводим конечный результат
result = calculate_final_price(initial_price, num_purchases)
print(f"Конечная сумма после всех покупок: {result}")