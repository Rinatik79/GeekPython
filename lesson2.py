# megalist = [7, "Good", 7.7, True, [True, False, None, 1], (19, [0, 4]), {"Mama": "Elvira", "Papa": "Rinat"}, None]
# for one_member in megalist:
#     print("'" + str(one_member) + "' has type: " + str(type(one_member)))

# string_list = input("Enter string list, use ' ' - space as separator: ")
# string_list = string_list.split(" ")
# print(string_list)
#
# for i in range(0, len(string_list), 2):
#     if i != len(string_list) - 1:
#         buffer = string_list[i]
#         string_list[i] = string_list[i+1]
#         string_list[i+1] = buffer
# print("There's changed list: " + str(string_list))

# months_list = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", 'fall', 'fall', 'fall', "winter"]
# months_dict = {
#     1: "winter",
#     2: "winter",
#     3: "spring",
#     4: "spring",
#     5: "spring",
#     6: "summer",
#     7: "summer",
#     8: "summer",
#     9: "fall",
#     10: "fall",
#     11: "fall",
#     12: "winter"
# }
# choice = int(input("Enter number of month [1-12], please: "))
# print("This season is printed by using a list: " + str(months_list[choice-1]))
# print("This season is printed by using a dict: " + months_dict[choice])

string_list = input("Enter string list, use ' ' - space as separator: ")
string_list = string_list.split(" ")
i = 0
for word in string_list:
    i += 1
    if len(word) > 10:
        print(str(i) + ": " + word[:10])
    else:
        print(str(i) + ": " + word)



