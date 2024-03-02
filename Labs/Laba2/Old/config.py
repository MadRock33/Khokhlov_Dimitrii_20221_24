#---Настраиваемые параметры---#
NAME_FIGURE = "Визирь"
VERSION = "0.0.2"
INPUT_FILE_NAME = "input.txt"
OUTPUT_FILE_NAME = "output.txt"

def get_moves(row: int, col: int) -> list[tuple[int, int]]:
    return [
        (row, col - 1), (row, col - 2),  # Влево
        (row, col + 1), (row, col + 2),  # Вправо
        (row - 1, col), (row - 2, col),  # Вверх
        (row + 1, col), (row + 2, col)  # Вниз
    ]

