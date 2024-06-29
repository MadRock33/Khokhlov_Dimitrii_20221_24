import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QMessageBox
from PySide6.QtCore import Qt
from chess import *
class ParameterWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Параметры")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label_n = QLabel("Размер доски N:")
        self.edit_n = QLineEdit()
        self.label_l = QLabel("Количество фигур L:")
        self.edit_l = QLineEdit()
        self.label_k = QLabel("Фигур требуется поставить K:")
        self.edit_k = QLineEdit()

        self.button_next = QPushButton("Дальше")
        self.button_next.clicked.connect(self.open_coordinate_window)

        self.layout.addWidget(self.label_n)
        self.layout.addWidget(self.edit_n)
        self.layout.addWidget(self.label_l)
        self.layout.addWidget(self.edit_l)
        self.layout.addWidget(self.label_k)
        self.layout.addWidget(self.edit_k)

        self.layout.addWidget(self.button_next)

    def open_coordinate_window(self):
        try:
            N = int(self.edit_n.text())
            K = int(self.edit_k.text())
            L = int(self.edit_l.text())
            if N <= 0 or K < 0 or L < 0:
                raise ValueError("Invalid input: N must be positive, K and L must be non-negative")
        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", str(e))
            return

        self.coordinate_window = CoordinateWindow(N, K, L)
        self.coordinate_window.show()
        self.close()

class CoordinateWindow(QMainWindow):
    def __init__(self, N:int, K:int, L:int):
        super().__init__()
        self.setWindowTitle("Координаты фигур")
        self.setGeometry(100, 100, 400, 400)

        self.N = N
        self.L = L
        self.K = K

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.figure_inputs = []

        self.label_figures = QLabel("Введите координаты фигур (x y):")
        self.layout.addWidget(self.label_figures)

        for i in range(K):
            label = QLabel(f"Фигура {i + 1}:")
            edit = QLineEdit()
            self.figure_inputs.append(edit)
            self.layout.addWidget(label)
            self.layout.addWidget(edit)

        self.button_next = QPushButton("Дальше")
        self.button_next.clicked.connect(self.open_board_window)
        self.layout.addWidget(self.button_next)

    def open_board_window(self):
        self.figure_coordinates = []
        try:
            for edit in self.figure_inputs:
                x, y = map(int, edit.text().split())
                if not (0 <= x < self.N and 0 <= y < self.N):
                    raise ValueError(f"Coordinates ({x}, {y}) are out of board bounds")
                self.figure_coordinates.append((x, y))
        except ValueError as e:
            QMessageBox.critical(self, "Ошибка", str(e))
            return

        self.board_window = BoardWindow(self.N, self.K, self.L, self.figure_coordinates)
        self.board_window.show()
        self.close()

class BoardWindow(QMainWindow):
    def __init__(self, N:int, K:int, L:int, figure_coordinates):
        super().__init__()
        self.setWindowTitle("ChessMaster")
        self.setGeometry(100, 100, 600, 600)

        self.N = N
        self.K = K
        self.L = L
        self.figure_coordinates = figure_coordinates

        self.board = Board(N)
        self.board.clear()
        self.steps_list = []
        self.figure_moves = []

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.layout.addWidget(self.view)

        self.button_solve = QPushButton("Найти вариации ходов")
        self.button_solve.clicked.connect(self.solve)
        self.layout.addWidget(self.button_solve)

        self.button_save = QPushButton("Сохранить")
        self.button_save.clicked.connect(self.save_to_file)
        self.layout.addWidget(self.button_save)

        self.draw_board()

    def draw_board(self):
        cell_size = 50
        for row in range(self.N):
            for col in range(self.N):
                color = Qt.white if (row + col) % 2 == 0 else Qt.gray
                rect_item = QGraphicsRectItem(col * cell_size, row * cell_size, cell_size, cell_size)
                rect_item.setBrush(color)
                self.scene.addItem(rect_item)

        for x, y in self.figure_coordinates:
            figure = Figure(x, y)
            figure.make_move(self.board)
            rect_item = QGraphicsRectItem(y * cell_size, x * cell_size, cell_size, cell_size)
            rect_item.setBrush(Qt.blue)
            self.scene.addItem(rect_item)

        for row in range(self.N):
            for col in range(self.N):
                if self.board[row, col] == "*":
                    rect_item = QGraphicsRectItem(col * cell_size, row * cell_size, cell_size, cell_size)
                    rect_item.setBrush(Qt.green)
                    self.scene.addItem(rect_item)

    def solve(self):
        game = Game()
        game.initialize_game(self.N, self.L, self.K, self.figure_coordinates)
        self.all_steps = game.get_all_steps()

        if not self.all_steps:
            QMessageBox.information(self, "Без вариантов(", "Варианты не найдены")
        else:
            self.draw_solution(self.all_steps[0])

    def draw_solution(self, solution):
        cell_size = 50
        for x, y in solution:
            rect_item = QGraphicsRectItem(y * cell_size, x * cell_size, cell_size, cell_size)
            rect_item.setBrush(Qt.red)
            self.scene.addItem(rect_item)

    def save_to_file(self):
        if hasattr(self, 'all_steps'):
            files = Files()
            files.set_data(self.all_steps)
            QMessageBox.information(self, "Выполнено", "Успешно сохранено в output.txt")
        else:
            QMessageBox.warning(self, "Без вариантов(", "Нет вариантов для сохранения")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ParameterWindow()
    main_window.show()
    sys.exit(app.exec())
