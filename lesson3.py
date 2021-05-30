# Здравствуйте дорогая Мария!
# Вы просили в проверке 1-го урока номеровать задания.
# К сожалению 2-ой урок я уже запостил без нумерации.
# Но начиная с этого урока, торжественно обещаю все нумеровать.


# Задача № 1:
def mega(given_a, given_b):
    print(str(given_a) + " / " + str(given_b) + " = " + str(given_a / given_b))


a = 0
b = 0
while b == 0:
    a = float(input("Enter numerator please: "))
    b = float(input("Enter denominator please: "))
    if b == 0 or b == 0.:
        print("Denominator cannot be 0, retry please.")
mega(a, b)


# Задача № 2:
def to_string(firstname, secondname, year, town, email, phone):
    print(firstname + " " + secondname + ", " + year + ", " + town + ", " + email + ", " + phone)


to_string("Rinat", "Sabitov", "1979", "Montreal", "sabitovrinat@mama.ca", "555-432-1111")


# Задача № 3:
def my_func(given_a, given_b, given_c):
    if given_a <= given_b and given_a <= given_c:
        return given_b + given_c
    if given_b <= given_a and given_b <= given_c:
        return given_a + given_c
    return given_a + given_b


print(my_func(3, 13, 23))


# Задача № 4:
def my_func(x, y):
    # return x ** y
    module_y = -y
    result = 1
    for i in range(module_y):
        result *= x
    return 1 / result


print(my_func(8, -3))

# Задача № 5:
total_sum = 0


def adder(given_list):
    list_sum = 0
    for member in given_list:
        if member != '':
            list_sum += float(member)

    return list_sum


trigger = True
while trigger:
    string_list = input("Enter you number list, use ' ' - space as separator, type 'end' to exit: ")
    if string_list.find("end") != -1:
        string_list = string_list.split("end")[0]
        trigger = False
    current_list = string_list.split(" ")
    total_sum += adder(current_list)
    print("Total sum is: " + str(total_sum))
print("Bye!")


# Задача № 6:
def int_func(text_line):
    return text_line.title()


print(int_func("text"))
print(int_func("papa u vasi silen v matemetike,"))
print(int_func("uchitsa papa za vasyu ves god,"))
print(int_func("gde eto vidano, gde eto slyhano,"))
print(int_func("papa reshaet a vasia sdaet!"))
