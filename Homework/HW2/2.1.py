def longest_substring(input_string:str) -> str:
    max_length = 0
    current_substring = []

    for end in range(len(input_string)):
        if input_string[end] in current_substring:
            start = current_substring.index(input_string[end]) + 1
            current_substring = current_substring[start:]

        current_substring.append(input_string[end])
        current_length = len(current_substring)
        if current_length > max_length:
            max_length = current_length
            max_substring = ''.join(current_substring)

    return max_substring

if __name__ == '__main__':
    print(longest_substring(input('Input a string: ')))

