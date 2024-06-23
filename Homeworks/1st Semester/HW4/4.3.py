def sorting_words_into_group(words:list[str,...]) -> list[list[str,...],...]:
    result = []
    seen = set()

    for word in words:
        sorted_word = tuple(sorted(word))
        key = (sorted_word, len(word))

        if key not in seen:
            seen.add(key)
            result.append([word])
        else:
            for group in result:
                if sorted_word == group[0]:
                    group.append(word)
                    break

    return result

if __name__ == '__main__':
    input_list = ["a","a",""]
    output = sorting_words_into_group(input_list)
    print(output)