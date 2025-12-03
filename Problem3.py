input = open('P3input.txt', 'r')
ids = input.read()
lines = ids.split(",")
total = 0

for line in lines:
    split = line.split("-")
    first = split[0]
    last = split[1]
    for i in range(int(first), int(last) + 1):
        str = f"{i}"
        if str[0:len(str)//2] == (str[len(str)//2:]):
            total += i
        
print(total)
