def flip_string(input_str:str) -> str:
    string_words = input_str.split()
    result = []
    for word in reversed(string_words):
        result.append(word)
    return ' '.join(result).capitalize()

if __name__ == '__main__':
    input_str = input("Input a string: ")
    output_str = flip_string(input_str)
    print("Flip string:", output_str)