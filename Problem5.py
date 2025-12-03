input = open('P5input.txt', 'r')
lines = input.read()
bats = lines.split()
total = 0

def findMax(a: str) -> (int, int):
    index = 0
    max = 0
    for i in range(0, len(a)):
        if int(a[i]) > max:
            max = int(a[i])
            index = i
    return (max, index)

for bat in bats:
    dig1 = findMax(bat)
    dig2 = findMax(bat[dig1[1] + 1:])
    if len(bat) > 1 and dig1[1] == len(bat)-1:
        dig1 = findMax(bat[0:len(bat)-1])
        dig2 = findMax(bat[dig1[1] + 1:])
    total += dig1[0] * 10
    total += dig2[0]
print(total)
