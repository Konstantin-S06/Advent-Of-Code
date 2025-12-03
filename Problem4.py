input = open('P3input.txt', 'r')
ids = input.read()
lines = ids.split(",")
total = 0
equal = True

for line in lines:
    split = line.split("-")
    first = split[0]
    last = split[1]
    for i in range(int(first), int(last) + 1):
        comb = f"{i}"
        for k in range(1, len(comb)//2 + 1):
            if comb[0:k]*(len(comb)//(k)) == comb:
                total += i
                break
            
                
print(total)
