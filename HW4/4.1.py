def flip_number(num:int) -> int:
    flipped_num = 0
    while num != 0:
        flipped_num = flipped_num * 10 + (num % 10)
        num //= 10
    return flipped_num

def isPalindrome(num:int, num2:int) -> bool :
    if num == num2:
        return True
    else:
        return False

if __name__ == "__main__":
    num = int(input("Введите число "))
    num2 = flip_number(abs(num))
    print(isPalindrome(abs(num),abs(num2)))

