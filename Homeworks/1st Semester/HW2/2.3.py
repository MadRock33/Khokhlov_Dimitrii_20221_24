def isValid(input_str:str) -> bool | str:
    is_matching = {
        ')':'(',
        '}':'{',
        ']':'[',
    }
    stack = []
    max_length = 0
    length = 0
    longest_valid_substr = ""

    for i, char in enumerate(input_str):
        match char:
            case "(" | "{" | "[":
                stack.append((char,i))
            case ")" | "}" | "]":
                if stack and is_matching[char] == stack[-1][0]:
                    stack.pop()
                    if stack:
                        length = i - stack[-1][1]
                    else:
                        length = i + 1

                    if length > max_length:
                        max_length = length
                        longest_valid_substr = input_str[i - max_length + 1:i+1]
                else: stack.append((char,i))

    if not stack: return True
    elif longest_valid_substr: return longest_valid_substr
    else: return False

#old_variant
#def _is_matching(opening_char:str, closeing_char:str):
#    return (opening_char == "(" and closeing_char == ")") or
#           (opening_char == "[" and closeing_char == "]") or
#           (opening_char == "{" and closeing_char == "}")

if __name__ == "__main__":
    print(isValid("[(){}(]")) # Test 1
    print(isValid("[()[((]))]]"))  # Test 2
    print(isValid("[()(]]"))  # Test 3
    print(isValid("[()[((]))]([]())]"))  # Test 4

    input_str = input()
    print(isValid(input_str))