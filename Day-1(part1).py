data = open("/Users/pranavkrishnan/desktop/adventofcode/input/input.txt")
lines = data.readlines()

count = 0

for x in range(len(lines)-1):
    if lines[x+1] > lines[x]:
        count += 1
print(count)

