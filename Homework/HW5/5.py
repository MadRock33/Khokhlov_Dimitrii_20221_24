def maximize_money(banks:list[(str,int),...]) -> list[int,(str,int),...]:
    n = len(banks)
    result = [0, ("", 0)]

    if n == 0:
        return result

    money = {0: banks[0][1], 1: max(banks[0][1], 0)}

    for i in range(2, n):
        money[i] = max(money[i - 2] + banks[i][1], money[i - 1])

    idx = n - 1
    while idx >= 0:
        if idx == 0 or money[idx] != money[idx - 1]:
            result[0] += banks[idx][1]
            result.append((banks[idx][0], idx + 1))
            idx -= 2
        else:
            idx -= 1

    result.pop(1)
    return result



if __name__ == "__main__":

    n = int(input("Введите количество банков: "))
    banks = []

    for i in range(n):
        bank_name = input("Введите название банка: ")
        money = int(input("Введите сумму денег в сейфе (в миллионах рублей): "))
        banks.append((bank_name, money))
    print(banks)
    result = maximize_money(banks)
    print(result)
