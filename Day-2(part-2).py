data = open("/Users/pranavkrishnan/desktop/adventofcode/input/day2.txt")
line = data.readlines()
aim = 0
f = 0
d = 0
for x in line:
    dir = x.split()
    print(dir[0],dir[1])
    if dir[0] == "forward":
        d = d + (aim * int(dir[1]))
        f = f + int(dir[1])
    else:
        if dir[0] == "down":
            aim = aim + int(dir[1])
        elif dir[0] == "up":
            aim = aim - int(dir[1])
    print(aim,d,f)
print(f*d)

