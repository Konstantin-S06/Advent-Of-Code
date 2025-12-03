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
    temp = bat
    for i in range(11, -1, -1):
        dig = findMax(temp[0:len(temp)-i])
        total += dig[0] * (10 ** i)
        if(dig[0] * (10 ** i) > 999999999999):
            print(dig[0] * (10 ** i))
        temp = temp[dig[1] + 1:]
        
print(total)
