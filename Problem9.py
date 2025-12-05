file = open('P9input.txt', 'r')
lines = file.read()
input = lines.split()
idRange = []
ids = []

for i in input:
    if "-" in i:
        parts = i.split("-")
        idRange.append((int(parts[0]), int(parts[1])))
    else:
        ids.append(int(i))
total = 0
for i in ids:
    for range in idRange:
        if i >= range[0] and i <= range[1]:
            total += 1
            break
print(total)
