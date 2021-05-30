from itertools import count, cycle
from sys import argv

# Problem 6:
# Run script with 3 arguments: starting int, finishing int, list printing repeating int
# For example: python lesson4_6.py 2 9 18

iterator = (count(start=int(argv[1]), step=1))
generated_list = list(next(iterator) for _ in range(int(argv[1]), int(argv[2])))

print ("Generated list:")
print (generated_list)

c = 0
for i in cycle(generated_list):
    print(i)
    c += 1
    if c == int(argv[3]):
        break
