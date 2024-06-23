import time
from config import get_moves, NAME_FIGURE, VERSION, OUTPUT_FILE_NAME, INPUT_FILE_NAME


def display_board(board: list, N: int) -> None:
    print(f"*------Доска:x{N}------*")
    for row in board:

        for i in row:
            print(i, end=" ")
        print()
    print()
    return

def display_info(steps_list: list, start_time: float) -> None:

    print("#------Результат------#")
    print(f"Всего решений: {len(steps_list)}")
    with open(OUTPUT_FILE_NAME, "w") as output_file:
        if not steps_list:
            output_file.write("no steps")
        else:
            for step in steps_list:
                output_file.write(" ".join(map(str, step)) + "\n")

    end_time = time.time()
    print(f"Время выполнения программы: {round(end_time - start_time,1)}s")


# Ограничиваем и добавляем элементы в нашу доску
def make_move(board, N: int, row: int, col: int, steps_list: list) -> None:
    steps_list.append((row, col))
    board[row] = board[row][:col] + "#" + board[row][col + 1:]

    moves = get_moves(row, col)

    for row_index, col_index in moves:
        if 0 <= row_index < N and 0 <= col_index < N and board[row_index][col_index] != "#":
            board[row_index] = board[row_index][:col_index] + "*" + board[row_index][col_index + 1:]


# Ищем ходы
def find_steps(L: int, N: int, board: list, row: int, col: int, steps_list: list, all_steps: list) -> None:
    while True:
        col += 1

        if col >= N:
            col = 0
            row += 1

        if row >= N: break

        if board[row][col] != "0": continue

        now_board = list(board)
        now_steps = list(steps_list)

        make_move(now_board, N, row, col, now_steps)

        if L - 1 == 0:
            all_steps.append(now_steps)
            if len(all_steps) == 1:
                 display_board(now_board, N)
            continue

        find_steps(L - 1, N, now_board, row, col, now_steps, all_steps)
def get_data(steps_list:list, make_move):
    with open(INPUT_FILE_NAME, "r") as input_file:
        N, L, K = map(int, input_file.readline().split())
        global board
        board = ["0" * N for _ in range(N)]

        for _ in range(K):
            row, col = map(int, input_file.readline().split())
            make_move(board, N, row, col, steps_list)
    return N,L,K,board

def main():
    start_time = time.time()  # Время начала выполнения программы
    steps_list = []
    all_steps = []
    N, L, K, board = get_data(steps_list, make_move)

    print(f"*-----Информация о программе-----*\n"
          f"Название фигуры: {NAME_FIGURE}\n"
          f"Версия программы: {VERSION}\n\n"
          f"*-----Параметры-----*\n"
          f"Размер доски: {N}x{N}\n"
          f"Количество фигур: {K}\n"
          f"Требуется разместить: {L}\n")
    if L == 0:
        if not steps_list:
            all_steps.append(steps_list)
        for i_row in board:
            print(i_row)
    find_steps(L, N, board, 0, -1, steps_list, all_steps)

    display_info(all_steps, start_time)


if __name__ == "__main__":
    main()
