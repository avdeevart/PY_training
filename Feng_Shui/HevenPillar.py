def get_symbol_element(year):
    cycle_year = (year - 1974) % 10
    symbol = 'Ян' if cycle_year in [0, 2, 4, 6, 8] else 'Инь'
    element = ['дерево', 'огонь', 'земля', 'металл', 'вода'][cycle_year // 2]
    return symbol, element

# Пример использования
year = int(input('Введите год: '))
symbol, element = get_symbol_element(year)
print(f'Для года {year} символ - {symbol}, элемент - {element}')
