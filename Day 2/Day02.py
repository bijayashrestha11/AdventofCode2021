import csv

#Part 1 of the Day 2 of Advent of Coding
aim = position = depth = 0

with open('F:\Study Material\Extra\Advent of Code\Day 2\input.csv') as data:
    reader = csv.reader(data, delimiter=' ')
    
#     for line in reader:
#         command, n_s = line[0], line[1]
#         n = int(n_s)
#         if command == 'up':
#             depth -= n
#         elif command == 'down':
#             depth += n
#         elif command == 'forward':
#             position += n
#         else:
#             raise AssertionError(f'Unreachable {command} {n}')
        
# print("The final answer of the multiplication is ", position*depth)

#Part 2 of the Day 2 of Advent of Coding
    for line in reader:
        command, n_s = line[0], line[1]
        n = int(n_s)
        if command == 'up':
            aim -= n
        elif command == 'down':
            aim += n
        elif command == 'forward':
            position += n
            depth += aim *n
        else:
            raise AssertionError(f'Unreachable {command} {n}')
        
print("The final answer of the multiplication is ", position*depth)
    