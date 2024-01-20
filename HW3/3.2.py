def rotate_matrix(matrix:list[list[int, ...], ...]) -> list[list[int, ...], ...]:
    m, n = len(matrix), len(matrix[0])


    transposed_matrix = [[matrix[row][col] for row in range(m)] for col in range(n)]
    #print(transposed_matrix)
    rotated_matrix = vertical_flip(transposed_matrix)
    #print(rotated_matrix)
    return rotated_matrix
def vertical_flip(matrix:list[list[int, ...], ...]) -> list[list[int, ...], ...]:
     return [list(reversed(row)) for row in matrix]



if __name__ == '__main__':
    matrix = [[1, 2, 3,4],
              [5, 6, 7, 8],
              [9,10,11,12]]
    rotated_matrix = rotate_matrix(matrix)
    #print(rotated_matrix)
    for i in range(len(rotated_matrix)):
        print(rotated_matrix[i],end='\n')