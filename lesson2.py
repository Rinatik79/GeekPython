megalist = [7, "Good", 7.7, True, [True, False, None, 1], (19, [0, 4]), {"Mama": "Elvira", "Papa": "Rinat"}, None]
for one_member in megalist:
    print("'" + str(one_member) + "' has type: " + str(type(one_member)))

string_list = input("Enter string list, use ' ' - space as separator: ")
string_list = string_list.split(" ")
print(string_list)

for i in range(0, len(string_list), 2):
    if i != len(string_list) - 1:
        buffer = string_list[i]
        string_list[i] = string_list[i+1]
        string_list[i+1] = buffer
print("There's changed list: " + str(string_list))

months_list = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", 'fall', 'fall', 'fall', "winter"]
months_dict = {
    1: "winter",
    2: "winter",
    3: "spring",
    4: "spring",
    5: "spring",
    6: "summer",
    7: "summer",
    8: "summer",
    9: "fall",
    10: "fall",
    11: "fall",
    12: "winter"
}
choice = int(input("Enter number of month [1-12], please: "))
print("This season is printed by using a list: " + str(months_list[choice-1]))
print("This season is printed by using a dict: " + months_dict[choice])

string_list = input("Enter string list, use ' ' - space as separator: ")
string_list = string_list.split(" ")
i = 0
for word in string_list:
    i += 1
    if len(word) > 10:
        print(str(i) + ": " + word[:10])
    else:
        print(str(i) + ": " + word)

my_list = [7, 5, 3, 3, 2]
print("Base list is: " + str(my_list))
new_number = int(input("Enter new number please: "))
my_list.extend([new_number])
my_list.sort(reverse=True)
print("List with new member: " + str(my_list))

selector = ""
product_list = []

while selector != '0':
    print("\nTo add new product enter '1'")
    print("To display statistic enter '2'")
    print("To exit enter '0'")
    selector = input(": ")
    counter = 0;
    if selector == '1':
        name = input("\nEnter new product name please: ")
        price = float(input("Enter new product price please: "))
        quantity = int(input("Enter new product quantity please: "))
        unit = input("Enter new product units of measurement please: ")
        counter += 1
        product_list.append((counter, {"name": name, "price": price, "quantity": quantity, "unit": unit}))

    if selector == '2':
        names = []
        prices = []
        quantities = []
        units = []
        print("\nHere is your statistic:")
        for i in range (len(product_list)):
            names.append(product_list[i][1]["name"])
            prices.append(product_list[i][1]["price"])
            quantities.append(product_list[i][1]["quantity"])
            units.append(product_list[i][1]["unit"])

        statistic = {"name": names,
                     "price": prices,
                     "quantity": quantities,
                     "unit": units}
        print(statistic)
    if selector == '0':
        print("Chao!")
        exit(0)
    if selector != '1' and selector != '2' and selector != '0':
        print("\nWrong enter, try again")
