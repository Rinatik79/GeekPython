# Hi dear Maria!

import time


# Problem 1:
class TrafficLight:
    __color = "red"

    def running(self):
        print(self.__color)
        time.sleep(7)
        self.__color = "yellow"
        print(self.__color)
        time.sleep(7)
        self.__color = "green"
        print(self.__color)
        time.sleep(7)
        print("Good bye!")

show_once = TrafficLight()
show_once.running()

# Problem 2:
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_asphalt_tonnage(self, one_cm_high_kilo, high_cm):
        x = (self._width * self._length * one_cm_high_kilo * high_cm) / 1000
        print ("You will need: " + str(x) + " tons of asphalt.")


tonnage = Road(20, 5000)
tonnage.get_asphalt_tonnage(25, 5)

# Problem 3:
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    pass

    def get_full_name(self):
        print("Full name is: " + self.name + " " + self.surname)

    def get_total_income(self):
        print("Total income is: " + str(self._income["wage"] + self._income["bonus"]))


vasia_pupkin = Position("Vasiliy", "Pupkin", "developer", {"wage": 2000, "bonus": 1000})
vasia_pupkin.get_full_name()
vasia_pupkin.get_total_income()
print(vasia_pupkin.position + "\n")

boria_vorotov = Position("Boris", "Vorotov", "derector", {"wage": 25000, "bonus": 15000})
boria_vorotov.get_full_name()
boria_vorotov.get_total_income()
print(boria_vorotov.position)

# Problem 4:
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("We are going.")

    def stop(self):
        print("We stopped\n")

    def turn(self, direction):
        print("We turn " + direction)

    def show_speed(self):
        print("Your speed is: " + str(self.speed))


class PoliceCar(Car):
    pass


class SportCar(Car):
    pass


class TownCar(Car):
    pass

    def show_speed(self):
        if self.speed > 60:
            print("Are you fool? Cops will catch you! Your current speed is: " + str(self.speed))
        else:
            print("Your speed is: " + str(self.speed))


class WorkCar(Car):
    pass

    def show_speed(self):
        if self.speed > 40:
            print("Are you fool? Boss knows your speed by GPS! Your current speed is: " + str(self.speed))
        else:
            print("Your speed is: " + str(self.speed))


crazy_police_car = PoliceCar(119, "blue-white", "Dodge", True)
crazy_police_car.go()
crazy_police_car.turn("left")
crazy_police_car.turn("right")
crazy_police_car.show_speed()
crazy_police_car.stop()

brave_sport_car = SportCar(170, "yellow-black", "Mustang", False)
brave_sport_car.go()
brave_sport_car.turn("right")
brave_sport_car.turn("left")
brave_sport_car.turn("right")
brave_sport_car.show_speed()
brave_sport_car.stop()

crazy_work_car = WorkCar(77, "white", "Gazel", False)
crazy_work_car.go()
crazy_work_car.turn("left")
crazy_work_car.turn("right")
crazy_work_car.show_speed()
crazy_work_car.stop()

just_town_car = TownCar(33, "rose", "WV", False)
just_town_car.go()
just_town_car.turn("right")
just_town_car.turn("left")
just_town_car.turn("right")
just_town_car.turn("left")
just_town_car.show_speed()
just_town_car.stop()

# Problem 5:
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Drawing started")


class Pen(Stationery):
    pass

    def draw(self):
        print("Penning started")


class Pencil(Stationery):
    pass

    def draw(self):
        print("Penciling started")


class Handle(Stationery):
    pass

    def draw(self):
        print("Handling started")


pen = Pen("just a pen")
pen.draw()

pencil = Pencil("just a pencil")
pencil.draw()

handle = Handle("Just a handle")
handle.draw()

draw = Stationery("Draw")
draw.draw()
