def spiral_matrix(matrix: list[list[int, ...], ...]) -> list:
    result_matrix = []

    while matrix:
        result_matrix += matrix.pop(0)
        if matrix and matrix[0]:
            result_matrix += [m.pop() for m in matrix]
        if matrix:
            result_matrix += matrix.pop()[::-1]
        if matrix and matrix[0]:
            result_matrix += [m.pop(0) for m in matrix[::-1]]

    return result_matrix # возвращаем результат

if __name__ == '__main__':
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]

    result_matrix = spiral_matrix(matrix)
    print(result_matrix)