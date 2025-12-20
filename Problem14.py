file = open('P13input.txt', 'r')
lines = file.read()
input = lines.split('\n')

total = 0

# def helpCount(listInput, setBeams):
#     count = 0
#     newBeams = setBeams.copy()
#     listBeams = list(setBeams)
#     for i in range(len(listBeams)):
#         if 0 <= listBeams[i] < len(listInput) and listInput[listBeams[i]] == '^':
#             count += 1
#             newBeams.remove(listBeams[i])
#             if listBeams[i] - 1 >= 0:
#                 newBeams.add(listBeams[i] - 1)
#             if listBeams[i] + 1 < len(listInput):
#                 newBeams.add(listBeams[i] + 1)
#     return count, newBeams

# for j in range(len(input)):
#     input[j] = list(input[j])

setBeams = set()
setBeams.add(input[0].index('S'))


def recurseBeams(inputLine, setBeams):
    if inputLine == len(input) - 1:
        return 0
    if "^" not in input[inputLine]:
        return recurseBeams(inputLine + 1, setBeams)
    
    newBeams = setBeams.copy()
    listBeams = list(setBeams)
    
    for i in range(len(listBeams)):
        if input[inputLine][listBeams[i]] == "^":
            leftBeam = set()
            leftBeam.add(listBeams[i] - 1)
            
            rightBeam = set()
            rightBeam.add(listBeams[i] + 1)
            
            return 2 + recurseBeams(inputLine + 1, leftBeam) + recurseBeams(inputLine + 1, rightBeam)
    return recurseBeams(inputLine + 1, setBeams)

print(recurseBeams(1, setBeams))