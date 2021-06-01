# Здравствуйте дорогая Мария!
import json

# Задание 1:
one_line = "your text"
file_text = []
print("Enter text line by line, after empty line enter, the text will be saved in ")
while one_line != '':
    one_line = input()
    file_text.append(one_line + '\n')

file = open("firsttext.txt", "w", encoding='utf-8')
file.writelines(file_text)
file.close()

# Задание 2:
file = open("text_problem2.txt", "r")
mega_string = file.readlines()
file.close()
print("File has " + str(len(mega_string)) + " lines")
line_counter = 0
for line in mega_string:
    line_counter += 1
    print("Line " + str(line_counter) + " contains " + str(line.count(' ') + 1) + " words.")

# Задание 3:
file = open("salaries.txt", "r")
list_string = file.readlines()
file.close()
salary_dict = {}
for line in list_string:
    salary_dict[line.split(" ")[0]] = int(line.split(" ")[1])

salary_sum = 0
for line in salary_dict:
    salary_sum += salary_dict.get(line)
    if salary_dict.get(line) < 20000:
        print(line)

print("Average salary is: " + str(salary_sum / len(salary_dict)))

# Задание 4:
file = open("englishcount.txt", "r")
russian_count_list = ["Один", "Два", "Три", "Четыре"]
list_string = file.readlines()
file.close()

for i in range(len(list_string)):
    line = list_string[i].split(" ")
    line[0] = russian_count_list[i]
    list_string[i] = line[0] + " " + line[1] + " " + line[2]

file = open("russiancount.txt", "w", encoding='utf-8')
file.writelines(list_string)
file.close()

# Задание 5:
file = open("numbers.txt", "w", encoding='utf-8')
file.writelines("1 7 15 20 37 38 50 57 80 76 88 0 95 114")
file.close()
file = open("numbers.txt", "r")
list_numbers = file.read().split(" ")
file.close()
sum_of_numbers = 0
for number in list_numbers:
    sum_of_numbers += int(number)
print("Sum of all numbers in the file is: " + str(sum_of_numbers))

# Задание 6:
file = open("lessons_for_lesson5.txt", "r")
string_list = file.readlines()
file.close()
discipline_list = []
hours_line = []
times_list = []
for line in string_list:
    discipline_list.append(line.split(":")[0])
    garbage_line = (line.split(":")[1])
    digits = " 0123456789"
    purified_line = ""
    for i in range(len(garbage_line)):
        if digits.count(garbage_line[i]) != 0:
            purified_line += garbage_line[i]
    hours_line.append(purified_line.split(" "))

for i in range(len(hours_line)):
    times_list.append(0)
    for j in range(len(hours_line[i])):
        if hours_line[i][j].isnumeric():
            times_list[i] += int(hours_line[i][j])

discipline_time_dict = {}
for i in range(len(discipline_list)):
    discipline_time_dict[discipline_list[i]] = times_list[i]

print(discipline_time_dict)

# Задание 7:
file = open("firms_and_profit.txt", "r")
string_list = file.readlines()
file.close()
firms_and_profits_dict = {}
for line in string_list:
    line_as_list = line.split(" ")
    firm_name = line_as_list[0]
    firm_results = int(line_as_list[2]) - int(line_as_list[3])
    firms_and_profits_dict[firm_name] = firm_results

profitable_result_counter = 0
profit_sum = 0
for result in firms_and_profits_dict:
    if firms_and_profits_dict[result] > 0:
        profit_sum += firms_and_profits_dict[result]
        profitable_result_counter += 1

average_profit = profit_sum / profitable_result_counter
average_profit_dict = {"average_profit": average_profit}
json_data = [firms_and_profits_dict, average_profit_dict]
print(json_data)

with open('firms_and_profit_rapport.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)
