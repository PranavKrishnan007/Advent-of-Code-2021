data = open("/Users/pranavkrishnan/desktop/adventofcode/input/input.txt")
lines = data.readlines()

count = 0
prev = 0
for x in range(len(lines)-2) :
    a = int(lines[x])
    b = int(lines[x+1])
    c = int(lines[x+2])
    sum = a + b + c
    if sum > prev:
        count += 1
    prev = sum
print(count-1)
