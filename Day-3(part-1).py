data = open("/Users/pranavkrishnan/desktop/adventofcode/input/day3.txt")
line = data.readlines()
counta = 0
countb = 0
countc = 0
countd = 0
counte = 0
countf = 0
countg = 0
counth = 0
counti = 0
countj = 0
countk = 0
countl = 0
for x in line:
    val = x.strip()
    if val[0] == '1':
        counta += 1
    if val[1] == '1':
        countb += 1
    if val[2] == '1':
        countc += 1
    if val[3] == '1':
        countd += 1
    if val[4] == '1':
        counte += 1
    if val[5] == '1':
        countf += 1
    if val[6] == '1':
        countg += 1
    if val[7] == '1':
        counth += 1
    if val[8] == '1':
        counti += 1
    if val[9] == '1':
        countj += 1
    if val[10] == '1':
        countk += 1
    if val[11] == '1':
        countl += 1
print(counta, countb, countc, countd, counte, countf, countg, counth, counti, countj, countk, countl)
gamma = []
if counta > 1000- int(counta):
    gamma.append(1)
else:
    gamma.append(0)
if countb > 1000 - int(countb):
    gamma.append(1)
else:
    gamma.append(0)
if countc > 1000 - int(countc):
    gamma.append(1)
else:
    gamma.append(0)
if countd > 1000 - int(countd):
    gamma.append(1)
else:
    gamma.append(0)
if counte> 1000 - int(counte):
    gamma.append(1)
else:
    gamma.append(0)
if countf> 1000 - int(countf):
    gamma.append(1)
else:
    gamma.append(0)
if countg> 1000 - int(countg):
    gamma.append(1)
else:
    gamma.append(0)
if counth> 1000 - int(counth):
    gamma.append(1)
else:
    gamma.append(0)
if counti> 1000 - int(counti):
    gamma.append(1)
else:
    gamma.append(0)
if countj> 1000 - int(countj):
    gamma.append(1)
else:
    gamma.append(0)
if countk> 1000 - int(countk):
    gamma.append(1)
else:
    gamma.append(0)
if countl> 1000 - int(countl):
    gamma.append(1)
else:
    gamma.append(0)
print(*gamma)
epsilon = []
for x in gamma:
    if x == 1:
        epsilon.append(0)
    else:
        epsilon.append(1)
print(*epsilon)
bit = [2048,1024,512,256,128,64,32,16,8,4,2,1]
gammarate = 0
for x in range(12):
    gammarate = gammarate + (gamma[x]*bit[x])
print(gammarate)
epsilonrate = 0
for x  in range(12):
    epsilonrate = epsilonrate + (epsilon[x]*bit[x])
print(epsilonrate)
print(epsilonrate*gammarate)
