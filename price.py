import main

def calculate_final_price(initial_price, num_pricing):
    final_price = 0
    current_price = initial_price
    
    for _ in range(num_pricing):
        current_price += current_price * 0.11  # Уменьшаем текущую цену на 11%
        final_price += current_price  # Складываем уменьшенную цену

    # Округляем конечную сумму и форматируем с разделением тысяч
    formatted_price = f"{round(final_price):,}".replace(",", ".")

    # Форматируем с единицами измерения (M, B, T, Qa, Qi)
    formatted_with_units = format_with_units(final_price)

    return f"{formatted_price} ({formatted_with_units})"   

def format_with_units(value):
    units = [("Oc", 1e27), ("Sp", 1e24), ("Sx", 1e21),("Qi", 1e18), ("Qa", 1e15), ("T", 1e12), ("B", 1e9), ("M", 1e6)]
    for unit, threshold in units:
        if value >= threshold:
            return f"{value / threshold:.2f} {unit}"
    
    return f"{value:.2f}"