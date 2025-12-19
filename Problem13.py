file = open('P13input.txt', 'r')
lines = file.read()
input = lines.split('\n')

total = 0

def helpCount(listInput, setBeams):
    count = 0
    newBeams = setBeams.copy()
    listBeams = list(setBeams)
    for i in range(len(listBeams)):
        if 0 <= listBeams[i] < len(listInput) and listInput[listBeams[i]] == '^':
            count += 1
            newBeams.remove(listBeams[i])
            if listBeams[i] - 1 >= 0:
                newBeams.add(listBeams[i] - 1)
            if listBeams[i] + 1 < len(listInput):
                newBeams.add(listBeams[i] + 1)
    return count, newBeams

for j in range(len(input)):
    input[j] = list(input[j])

setBeams = set()
setBeams.add(input[0].index('S'))

for k in range(len(input)):
    count, setBeams = helpCount(input[k], setBeams)
    total += count

print(total)
            
    