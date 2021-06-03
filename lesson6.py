# Hi dear Maria!

import time


# Problem 1:
# class TrafficLight:
#     __color = "red"
#
#     def running(self):
#         print(self.__color)
#         time.sleep(7)
#         self.__color = "yellow"
#         print(self.__color)
#         time.sleep(7)
#         self.__color = "green"
#         print(self.__color)
#         time.sleep(7)
#         print("Good bye!")
#
# show_once = TrafficLight()
# show_once.running()

# Problem 2:
# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def get_asphalt_tonnage(self, one_cm_high_kilo, high_cm):
#         x = (self._width * self._length * one_cm_high_kilo * high_cm) / 1000
#         print ("You will need: " + str(x) + " tons of asphalt.")
#
#
# tonnage = Road(20, 5000)
# tonnage.get_asphalt_tonnage(25, 5)

# Problem 3:
# class Worker:
#     def __init__(self, name, surname, position, income):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = income
#
#
# class Position(Worker):
#     pass
#
#     def get_full_name(self):
#         print("Full name is: " + self.name + " " + self.surname)
#
#     def get_total_income(self):
#         print("Total income is: " + str(self._income["wage"] + self._income["bonus"]))
#
#
# vasia_pupkin = Position("Vasiliy", "Pupkin", "developer", {"wage": 2000, "bonus": 1000})
# vasia_pupkin.get_full_name()
# vasia_pupkin.get_total_income()
# print(vasia_pupkin.position + "\n")
#
# boria_vorotov = Position("Boris", "Vorotov", "derector", {"wage": 25000, "bonus": 15000})
# boria_vorotov.get_full_name()
# boria_vorotov.get_total_income()
# print(boria_vorotov.position)

# Problem 4:
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
