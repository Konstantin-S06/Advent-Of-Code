input = open('input.txt', 'r')
lines = input.read()
comb = lines.split()
current = 50
count = 0

for j in range(0, len(comb)):
    i = comb[j]
    value = int(i[1:])

    if i[0] == "L":
        current -= value
        while current < 0:
            current = 100 + current
    else:
        current += value
        while current >= 100:
            current = current - 100

    if current == 0:
        count += 1
print(count)