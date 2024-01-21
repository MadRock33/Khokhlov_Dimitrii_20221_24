def flip_number(num:int) -> int:
    isNegative = False
    flipped_num = 0

    if num < 0:
        isNegative = True
        num *= -1

    while num != 0:
        flipped_num = flipped_num * 10 + (num % 10)
        num //= 10

    if isNegative: flipped_num *= -1

    return flipped_num

def isEightBit(num:int) -> bool:
    if num < (2**7)-1 and num > -(2**7):
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input("Введите число "))
    num = flip_number(num)
    if not isEightBit(num):
        print("Not solution")
    else:
        print(num)


