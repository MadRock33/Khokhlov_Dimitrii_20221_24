import time
from config import get_moves,get_data

def display_solutions(solutions: list, startTime) -> None:
    print(f"Всего решений:{len(solutions)}")

    with open("output.txt", "w") as output_file:
        if not solutions:
            output_file.write("no solutions")
        else:
            for solution in solutions:
                output_file.write(" ".join(map(str, solution)) + "\n")

    endTime = time.time()
    print(f"Время выполнения программы: {endTime - startTime}s")


#ограничиваем и добавляем элементы в нашу доску
def make_move(board, N: int, row: int, col: int, solutions: list) -> None:
    solutions.append((row, col))
    board[row] = board[row][:col] + "#" + board[row][col+1:]

    moves = get_moves(row,col)

    for row_index, col_index in moves:
        if 0 <= row_index < N and 0 <= col_index < N and board[row_index][col_index] != "#":
            board[row_index] = board[row_index][:col_index] + "*" + board[row_index][col_index+1:]



#ищем ходы
def find_solution(L: int, N: int, board: list, row: int, col: int, solutions: list, allSolutions: list) -> None:
    while True:
        col += 1

        if col >= N:
            col = 0
            row += 1

        if row >= N: break

        if board[row][col] != "0": continue

        now_board = list(board)
        now_solutions = list(solutions)

        make_move(now_board, N, row, col, now_solutions)

        if L - 1 == 0:
            allSolutions.append(now_solutions)
            if len(allSolutions) == 1:
                for i_row in now_board:
                    print(i_row)
            continue

        find_solution(L - 1, N, now_board, row, col, now_solutions, allSolutions)



#инициализируем данные
def init_data():
    startTime = time.time() #запуск таймера

    solutions = []
    allSolutions = []

    N,L,K,board = get_data(solutions, make_move)

    return startTime, board, solutions, allSolutions, N, L, K


if __name__ == "__main__":
    startTime, board, solutions, allSolutions, N, L, K = init_data()

    print(f"Размер доски: {N}x{N}\n"
          f"Фигур на доске: {K}\n"
          f"Требуется разместить: {L}")

    if L == 0:
        if not (len(solutions) == 0):
            allSolutions.append(solutions)
        for i_row in board:
            print(i_row)
        display_solutions(allSolutions, startTime)

    find_solution(L, N, board, 0, -1, solutions, allSolutions)
    display_solutions(allSolutions, startTime)