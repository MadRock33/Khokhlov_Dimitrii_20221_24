
def get_moves(row: int, col: int) -> list[tuple[int, int]]:
    return [
        (row, col - 1), (row, col - 2),  # Влево
        (row, col + 1), (row, col + 2),  # Вправо
        (row - 1, col), (row - 2, col),  # Вверх
        (row + 1, col), (row + 2, col)  # Вниз
    ]

def get_data(solutions:list, make_move):
    with open("input.txt", "r") as input_file:
        N, L, K = map(int, input_file.readline().split())

        board = ["0" * N for _ in range(N)]

        for _ in range(K):
            row, col = map(int, input_file.readline().split())
            make_move(board, N, row, col, solutions)
    return N,L,K,board