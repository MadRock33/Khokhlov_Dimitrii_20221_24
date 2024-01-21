def analysis_lists(list_input1:list, list_input2:list) -> int:
    common_elements = set(list_input1) & set(list_input2)
    unique_elements = set(list_input1) ^ set(list_input2)
    remaining_list1 = list(set(list_input1) - common_elements)
    remaining_list2 = list(set(list_input2) - common_elements)

    return len(common_elements), len(unique_elements), len(remaining_list1), len(remaining_list2)


if __name__ == '__main__':
    list_input1 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25]
    list_input2 = [1, 38, 48, 8, 41, 7, 12, 48, 16, 40, 20, 23, 25]

    common_count, unique_count, remaining_list1_count, remaining_list2_count = analysis_lists(list_input1, list_input2)

    print(f"1) {common_count} элемента")
    print(f"2) {unique_count} элементов")
    print(f"3) {remaining_list1_count} элементов")
    print(f"4) {remaining_list2_count} элементов")
