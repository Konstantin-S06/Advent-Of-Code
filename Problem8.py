input = open('P7input.txt', 'r')
lines = input.read()
beforeRolls = lines.split()

def count_neighbors(rolls, total):
    changed = False
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
                rolls[i] = rolls[i][:j] + "." + rolls[i][j+1:]
                changed = True
    if changed:
        return count_neighbors(rolls, total)
    return total


print(count_neighbors(beforeRolls, 0))

