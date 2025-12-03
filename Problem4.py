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
            equal = True
            if int(len(comb)//k * k) != len(comb):
                    equal = False
                    continue
            for m in range (0, len(comb), k):
                if comb[m:m+k] != comb[0:k]:
                    equal = False
                    break
            if equal:
                total += i
                break
            
                
print(total)
