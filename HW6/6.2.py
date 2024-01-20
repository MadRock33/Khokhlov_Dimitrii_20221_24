def count_and_get_subsets(elements: list) -> (int,list):
    n = len(elements)
    unique_subsets = set()

    for i in range(1,2**n):
        subset = [elements[j] for j in range(n) if (i & (1 << j)) > 0]
        if len(subset) == len(set(subset)):
            unique_subsets.add(tuple(sorted(subset)))

    return len(unique_subsets), list(map(set, unique_subsets))

if __name__ == '__main__':
    #list_input = [1,2,3,4]
    list_input = ['a', 'b', 'c', 'd', 'd']
    count, subsets = count_and_get_subsets(list_input)


    print(f"Подмножества: {subsets}")
    print(f"Количество подмножеств: {count}")
