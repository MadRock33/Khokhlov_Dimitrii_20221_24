def isValid(input_string:str) -> bool | int:
    a = ''
    stack = []
    mapping ={
        ')':'(',
        '}':'{',
        ']':'['
    }
    max_length = 0
    c = 0
    f=-1
    for i in input_string:
        match i:
            case '(' | '{' | '[':
                a += i
                c+=1
                if max_length < c: max_length = c

            case ')' | '}' | ']':
                if a != '' and mapping[i] == a[-1]:
                    a = a[:-1]
                    c+=1
                    if max_length < c: max_length = c

            case _:
                    f +=1
                    stack.append(a)
                    a = ''
                    c = 0

        if f == -1:
            return True
        else:
            return stack[f]

if __name__ == '__main__':
    print(isValid(input('Enter a string ({[]}): ')))