# Hi dear Maria!

# Problem 1:
from abc import ABC, abstractmethod


class Matrix:
    def __init__(self, list_of_lines):

        self.list_of_lines = list_of_lines

    def __str__(self):

        for line in self.list_of_lines:
            print(line)

        return "\n"

    def __add__(self, other):
        out_matrix_list = self.list_of_lines
        for i in range(len(self.list_of_lines)):
            for j in range(len(self.list_of_lines[i])):
                out_matrix_list[i][j] = self.list_of_lines[i][j] + other.list_of_lines[i][j]

        return out_matrix_list


matrixA = Matrix([[0, 1, 3], [2, 3, 4], [3, 4, 5]])
print(matrixA)

matrixB = Matrix([[1, 1, 1], [0, 0, 0], [-3, -4, -5]])
print(matrixB)

matrixC = Matrix(matrixA + matrixB)
print(matrixC)


# Problem 2:
class Clothes(ABC):

    def __init__(self, name, main_measure):
        self.name = name
        self.main_measure = main_measure

    @property
    def get_full_object_info(self):
        return "Name: " + str(self.name) + ", fabric_consumption: " + str(self.fabric_consumption())

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    pass

    def fabric_consumption(self):
        return self.main_measure / 6.5 + 0.5


class Suit(Clothes):
    pass

    def fabric_consumption(self):
        return 2 * self.main_measure + 0.3


old_coat = Coat("old coat", 48)
print(old_coat.fabric_consumption())
print(old_coat.get_full_object_info)

new_suit = Suit("new suit", 174)
print(new_suit.fabric_consumption())
print(new_suit.get_full_object_info)


# Problem 3:
class Cell:

    def __init__(self, starting_qty):
        self.starting_qty = starting_qty

    def make_order(self):
        multiplicator = self.starting_qty // 5
        tail = self.starting_qty % 5
        return (multiplicator * "*****\n") + (tail * "*") + "\n"

    def __add__(self, other):
        return self.starting_qty + other.starting_qty

    def __mul__(self, other):
        return self.starting_qty * other.starting_qty

    def __sub__(self, other):
        if self.starting_qty > other.starting_qty:
            return self.starting_qty - other.starting_qty

        return print("Impossible to do this subtraction!\n")

    def __truediv__(self, other):
        return self.starting_qty // other.starting_qty


a = Cell(4)
b = Cell(2)
ab = Cell(a * b)
print(ab.make_order())

c = Cell(10)
abc = Cell(ab + c)
print(abc.make_order())

d = Cell(abc - a)
print(d.make_order())

error = Cell(b - a)

e = Cell(abc / a)
print(e.make_order())
