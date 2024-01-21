def minus_or_plus(N:int, numbers:list[int,...], target:int, current_sum:int=0, expression:str='', index:int=0):
    if index == N:
        return expression if current_sum == target else None

    expression_plus = minus_or_plus(N, numbers, target, current_sum + numbers[index], expression + '+' + str(numbers[index]), index + 1)
    expression_minus = minus_or_plus(N, numbers, target, current_sum - numbers[index], expression + '-' + str(numbers[index]), index + 1)

    return expression_plus or expression_minus

def main():
    with open('input.txt', 'r') as file:
        N, *numbers, target = map(int, file.readline().split())

    expression = minus_or_plus(N, numbers, target)

    with open('output.txt', 'w') as file:
        file.write(expression + '=' + str(target) if expression else 'no solution')

if __name__ == "__main__":
    main()
