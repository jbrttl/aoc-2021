
with open('aoc_d11.txt') as f:
    lines = f.read().split('\n')

counter = 0
lines.pop()

for index,line in enumerate(lines):
    if index != 0:
        if int(line) > int(lines[index-1]):
            counter += 1

print('Final result:', counter)
