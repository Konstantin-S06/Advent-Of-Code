input = open('P7input.txt', 'r')
lines = input.read()
rolls = lines.split()
total = 0

for i in range(len(rolls)):
    for j in range(len(rolls[i])):
        count = 0
        if rolls[i][j] == ".":
            continue
        if j > 0 and rolls[i][j-1] == "@":
            count += 1
        if j < len(rolls[i])-1 and rolls[i][j+1] == "@":
            count += 1
        if i > 0 and rolls[i-1][j] == "@":
            count += 1
        if i < len(rolls)-1 and rolls[i+1][j] == "@":
            count += 1
        if i > 0 and j > 0 and rolls[i-1][j-1] == "@":
            count += 1
        if i > 0 and j < len(rolls[i])-1 and rolls[i-1][j+1] == "@":
            count += 1
        if i < len(rolls)-1 and j > 0 and rolls[i+1][j-1] == "@":
            count += 1
        if i < len(rolls)-1 and j < len(rolls[i])-1 and rolls[i+1][j+1] == "@":
            count += 1
        if count <= 3:
            total += 1


print(total)

