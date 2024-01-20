
def string2zigzag(input_str:str, num_rows:int) -> str:
    if not isValidated(input_str,num_rows):
        return input_str

    result = ['' for _ in range(num_rows)]
    row, step = 0, 1

    for char in input_str:
        result[row] += char
        if row == 0:
            step = 1
        elif row == num_rows - 1:
            step = -1
        row += step

    return str(''.join(result))

def isValidated(input_str:str,num_rows:int) -> bool: #функция проверяет на валидность введенные значения
    if num_rows == 1 or num_rows >= len(input_str):
        return False
    else:
        return True

if __name__ == '__main__':
    input_str = str(input("Input a string:"))
    num_rows = int(input("Input the number of rows:"))
    print(string2zigzag(input_str, num_rows))

