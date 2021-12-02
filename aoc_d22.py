with open('aoc_d2.txt') as f:
    lines = f.read().split('\n')

# Remove last empty item in the list
lines.pop()

horizontal = 0
aim = 0
depth = 0

for line in lines:
    instruction = line.split(' ')
    if instruction[0] == 'forward':
        horizontal += int(instruction[1])
        depth += (int(instruction[1]) * aim)
    elif instruction[0] == 'up':
        aim -= int(instruction[1])
    elif instruction[0] == 'down':
        aim += int(instruction[1])

print(f'Result: {horizontal * depth}'')
