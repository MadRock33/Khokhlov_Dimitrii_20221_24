import time




class Board:
    def __init__(self, N: int):
        self.N = N
        self.board = [["0"] * N for _ in range(N)]

    def clear(self):
        self.board = [["0"] * self.N for _ in range(self.N)]

    def __getitem__(self, pos):
        row, col = pos
        return self.board[row][col]

    def __setitem__(self, pos, value):
        row, col = pos
        self.board[row][col] = value

    def display(self):
        for row in self.board:
            print(" ".join(row))

class Figure:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.moves = [(row, col - 1), (row, col - 2),
                      (row, col + 1), (row, col + 2),
                      (row - 1, col), (row - 2, col),
                      (row + 1, col), (row + 2, col)]

    def make_move(self, board):
        board[self.row, self.col] = "#"
        for row_index, col_index in self.moves:
            if 0 <= row_index < board.N and 0 <= col_index < board.N and board[row_index, col_index] != "#":
                board[row_index, col_index] = "*"

class Files:
    def __init__(self, output_file_name="output.txt"):
        self.output_file_name = output_file_name
    def set_data(self, all_steps):
        with open(self.output_file_name, "w") as output_file:
            if not all_steps:
                output_file.write("no steps")
            else:
                for step in all_steps:
                    output_file.write(" ".join(map(str, step)) + "\n")



class Game:
    def __init__(self, console_display=False):
        self.files = Files()
        self.N = 0
        self.L = 0
        self.K = 0
        self.board = None
        self.steps_list = []
        self.all_steps = []
        self.console_display = console_display

    def initialize_game(self, N, L, K, figure_coordinates):
        self.N = N
        self.L = L
        self.K = K
        self.board = Board(N)
        self.board.clear()
        self.steps_list = figure_coordinates

        for row, col in figure_coordinates:
            figure = Figure(row, col)
            figure.make_move(self.board)

    def find_steps(self, L, board, steps, row=0, col=-1):
        if L == 0:
            self.all_steps.append(steps[:])
            return

        for i in range(row, board.N):
            for j in range(col + 1 if i == row else 0, board.N):
                if board[i, j] == "0":
                    new_board = Board(board.N)
                    new_board.board = [row[:] for row in board.board]
                    figure = Figure(i, j)
                    figure.make_move(new_board)
                    steps.append((i, j))
                    self.find_steps(L - 1, new_board, steps, i, j)
                    steps.pop()

    def get_all_steps(self):
        self.all_steps = []
        self.find_steps(self.L, self.board, self.steps_list[:])
        return self.all_steps

    def display_info(self, start_time):
        if self.console_display:
            print("#------Результат------#")
            print(f"Всего решений: {len(self.all_steps)}")
            end_time = time.time()
            print(f"Время выполнения программы: {round(end_time - start_time, 1)}s")

