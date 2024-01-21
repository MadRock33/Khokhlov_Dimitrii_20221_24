def get_possible_pins(observed_pin:str) -> list[str,...]:
    adjacent_digits = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }


    result = ['']


    for digit in observed_pin:

        result = [prefix + neighbor for prefix in result for neighbor in adjacent_digits[digit]]

    return result

if __name__ == '__main__':
    pin = input("Enter a pin: ")
    result_variants = get_possible_pins(pin)
    print(result_variants)
