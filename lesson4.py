# Hi dear Maria!
# Terminal doesn't want to work with russian text

from functools import reduce

# Problem 1:
from sys import argv
working_time, working_rate, bonus = map(float, argv[1:])
print("Your pay is: " + str(working_time * working_rate + bonus))

# Problem 2:
int_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [int_list[i] for i in range(1, len(int_list)) if int_list[i] > int_list[i-1]]
print(result_list)

# Problem 3:
print([i for i in range(20, 241) if i % 20 == 0 or i % 21 == 0])

# Problem 4:
int_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
single_list = [int_list[i] for i in range(len(int_list)) if int_list.count(int_list[i]) == 1]
print(single_list)

# Problem 5:
product = reduce((lambda x, y: x * y), [i for i in range(100, 1001) if i % 2 == 0])
print(product)
