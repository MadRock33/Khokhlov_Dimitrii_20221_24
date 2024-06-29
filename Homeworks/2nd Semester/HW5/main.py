import random

class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._x = x
        self._y = y
        self._length = length
        self._tp = tp
        self._is_move = True
        self._cells = [1] * length

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            if self._tp == 1:  # Horizontal
                self._x += go
            else:  # Vertical
                self._y += go

    def is_collide(self, other):
        ship1_coords = [(self._x + i, self._y) if self._tp == 1 else (self._x, self._y + i) for i in range(self._length)]
        ship2_coords = [(other._x + i, other._y) if other._tp == 1 else (other._x, other._y + i) for i in range(other._length)]
        for x1, y1 in ship1_coords:
            for x2, y2 in ship2_coords:
                if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
                    return True
        return False

    def is_out_pole(self, size):
        if self._tp == 1:  # Horizontal
            return not (0 <= self._x < size and 0 <= self._x + self._length - 1 < size and 0 <= self._y < size)
        else:  # Vertical
            return not (0 <= self._y < size and 0 <= self._y + self._length - 1 < size and 0 <= self._x < size)

    def __getitem__(self, indx):
        return self._cells[indx]

    def __setitem__(self, indx, value):
        self._cells[indx] = value
        if value == 2:
            self._is_move = False

class GamePole:
    def __init__(self, size=10):
        self.size = size
        self._ships = []
        self.init()

    def init(self):
        ship_types = [(4, 1), (3, 2), (2, 3), (1, 4)]
        for length, count in ship_types:
            for _ in range(count):
                while True:
                    tp = random.randint(1, 2)
                    x = random.randint(0, self.size - 1)
                    y = random.randint(0, self.size - 1)
                    ship = Ship(length, tp, x, y)
                    if not ship.is_out_pole(self.size) and not any(ship.is_collide(other) for other in self._ships):
                        self._ships.append(ship)
                        break

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            if ship._is_move:
                go = random.choice([1, -1])
                original_x, original_y = ship.get_start_coords()
                ship.move(go)
                if ship.is_out_pole(self.size) or any(ship.is_collide(other) for other in self._ships if other != ship):
                    ship.set_start_coords(original_x, original_y)

    def show(self):
        pole = [[0] * self.size for _ in range(self.size)]
        for ship in self._ships:
            for i in range(ship._length):
                x, y = ship._x + (i if ship._tp == 1 else 0), ship._y + (0 if ship._tp == 1 else i)
                pole[y][x] = ship._cells[i]
        for row in pole:
            print(' '.join(map(str, row)))

    def get_pole(self):
        pole = [[0] * self.size for _ in range(self.size)]
        for ship in self._ships:
            for i in range(ship._length):
                x, y = ship._x + (i if ship._tp == 1 else 0), ship._y + (0 if ship._tp == 1 else i)
                pole[y][x] = ship._cells[i]
        return tuple(map(tuple, pole))

# Тесты
ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)
assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"
ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"
ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"
s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"
s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"
s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"
s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"
p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"
        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()

gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"
pole_size_8 = GamePole(8)
pole_size_8.init()
print("\nPassed all tests!")
