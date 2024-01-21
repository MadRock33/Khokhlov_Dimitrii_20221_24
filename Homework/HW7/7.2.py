def roman2arabic(roman_num:str) -> int:
    roman_dict = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000
                  }
    result = 0

    for i in range(len(roman_num)):

        if i < len(roman_num) - 1 and roman_dict[roman_num[i]] < roman_dict[roman_num[i + 1]]:
            result -= roman_dict[roman_num[i]]
        else:
            result += roman_dict[roman_num[i]]

    return result

if __name__ == '__main__':
    roman_number = input('Enter a roman numeral: ')
    result = roman2arabic(roman_number)
    print(result)
