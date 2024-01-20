def maximize_robbery(banks):
    if not banks:
        return 0, []

    prev_max_sum = 0
    curr_max_sum = banks[0][1]
    result_banks = [0]

    for i in range(1, len(banks)):
        if prev_max_sum + banks[i][1] > curr_max_sum:
            curr_max_sum, prev_max_sum = prev_max_sum + banks[i][1], curr_max_sum
            result_banks.append(i)

    return curr_max_sum, [(banks[i][0], i + 1) for i in result_banks]

# Пример использования
num_banks = int(input("Введите количество банков: "))
banks_data = [(input(f"Введите название банка {i + 1}: "), float(input(f"Введите сумму в сейфе банка {i + 1} (в миллионах рублей): "))) for i in range(num_banks)]

result_sum, result_banks = maximize_robbery(banks_data)
print(f"\nМаксимальная сумма денег, которую можно получить: {result_sum} млн рублей.")
print("Банки для ограбления в следующем порядке:")
for bank_name, bank_number in result_banks:
    print(f"{bank_name} (банк {bank_number})")
