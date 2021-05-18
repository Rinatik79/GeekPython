a = 7
b = 7.7
c = "Seventh son of the seventh son."
name = input("Enter your name please: ")
age = int(input("Enter your age please: "))
print("int a = " + str(a))
print("float b = " + str(b))
print("String c is '" + c + "'")
print("Your name is " + name)
print("Your age is " + str(age))

total_seconds = int(input("Enter time in seconds please: "))
hours = 0
minutes = 0
seconds = 0
if total_seconds >= 60 ** 2:
    hours = total_seconds // 60 ** 2
    total_seconds = total_seconds % 60 ** 2
if total_seconds >= 60:
    minutes = total_seconds // 60
    seconds = total_seconds % 60
if hours < 10:
    hours = "0" + str(hours)
else:
    hours = str(hours)
if minutes < 10:
    minutes = "0" + str(minutes)
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = "0" + str(seconds)
else:
    seconds = str(seconds)
print("You have entered time in seconds, counted as: " + hours + ":" + minutes + ":" + seconds)

basic_digit = input('Enter your digit: ')
second_number = int(basic_digit + basic_digit)
third_number = int(basic_digit + basic_digit + basic_digit)
basic_digit = int(basic_digit)
print("Sum:")
print((basic_digit + second_number + third_number))

number = input("Enter number please: ")
all_numbers = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "0"]
biggest_digit = "0"
i = 0
continue_search = True
while i < 10 and continue_search:
    if number.find(all_numbers[i]) != -1:
        biggest_digit = all_numbers[i]
        continue_search = False
    i += 1
print("The biggest digit in number '" + number + "' is: " + biggest_digit)

revenue = float(input("Enter your company's revenue please: "))
costs = float(input("Enter your company's costs please: "))
if revenue >= costs:
    print("Your company have profit: " + str(revenue - costs))
    personal = int(input("Enter your company's personal quantity: "))
    print("Your company have '" + str((revenue - costs) / personal) + "' to single person effectivity.")
else:
    print("Your company is loss-making.")

starting_mileage = float(input("Enter starting mileage please: "))
wanted_mileage = float(input("Enter desired mileage please: "))
current_mileage = starting_mileage
day = 1
print("day number " + str(day) + " result is " + str(current_mileage))
while current_mileage < wanted_mileage:
    current_mileage = current_mileage * 1.1
    day += 1
    print("day number " + str(day) + " result is " + str(current_mileage))

print("Desired mileage will be gained in '" + str(day) + "' day of training.")
