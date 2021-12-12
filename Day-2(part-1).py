data = open("/Users/pranavkrishnan/desktop/adventofcode/input/day2.txt")
line = data.readlines()
f = 0
d = 0
for x in line:
    dir = x.split()
    print(dir[0],dir[1])
    if dir[0] == "forward":
        f = f + int(dir[1])
    else:
        if dir[0] == "down":
            d = d + int(dir[1])
        elif dir[0] == "up":
            d = d - int(dir[1])
print(f*d)
