def generate_all_permutations(input_list:list) -> list[list[int,...],...]:
    result = [[]]

    for num in input_list:
        new_permutations = []
        for perm in result:
            for i in range(len(perm) + 1):
                new_permutations.append(perm[:i] + [num] + perm[i:])
        result = new_permutations

    return result[::-1]


input_list = [1, 2, 3, 4]
result = generate_all_permutations(input_list)
for i in range(len(result)):
    print(f"{i+1}. {result[i]}")

#print(result)
