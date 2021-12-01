
with open('aoc_d11.txt') as f:
    lines = f.read().split('\n')

counter = 0
lines.pop()

for index,line in enumerate(lines):
    if index > 2:

        sum2 = int(line) + int(lines[index-1]) + int(lines[index-2])
        sum1 = int(lines[index-1]) + int(lines[index-2]) + int(lines[index-3])
        print(int(lines[index-1]), int(lines[index-2]), int(lines[index-3]))
        
        if sum2 > sum1:
            counter += 1

print('Final result:', counter)
