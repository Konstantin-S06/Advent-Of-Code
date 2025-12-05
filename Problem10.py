file = open('P9input.txt', 'r')
lines = file.read()
input = lines.split()
idRange = []
total = 0
added = False

def check_overlap(given1):
    given = given1.copy()
    changed = False
    for i in range(len(given)):
        givei = given1[i]
        for j in range(i, len(given)):
            givej = given1[j]
            if i != j:
                if givei[0] <= givej[0]:
                    if givei[1] < givej[0]:
                        continue
                    if givei[1] <= givej[1]:
                        given[j] = (givei[0], givej[1])
                        given.remove(givei)
                        changed = True
                        break
                    if givei[1] > givej[1]:
                        given[j] = (givei[0], givei[1])
                        given.remove(givei)
                        changed = True
                        break
                elif givei[0] > givej[0]:
                    if givei[0] > givej[1]:
                        continue
                    if givei[1] <= givej[1]:
                        changed = True
                        given.remove(givei)
                        break
                    if givei[1] > givej[1]:
                        given[j] = (givej[0], givei[1])
                        given.remove(givei)
                        changed = True
                        break
    if changed:
        return check_overlap(given)
    else:
        return given


for i in input:
    if "-" in i:
        strings = i.split("-")
        parts= (int(strings[0]), int(strings[1]))
        if len(idRange) > 0:
            added = False
            for j in range(0, len(idRange)):
                ranges = idRange[j]
                if parts[0] <= ranges[0]:
                    if parts[1] < ranges[0]:
                        continue
                    if parts[1] <= ranges[1]:
                        idRange[j] = (parts[0], ranges[1])
                        added = True
                        idRange = check_overlap(idRange)
                        break
                    if parts[1] > ranges[1]:
                        idRange[j] = (parts[0], parts[1])
                        added = True
                        idRange = check_overlap(idRange)
                        break
                elif parts[0] > ranges[0]:
                    if parts[0] > ranges[1]:
                        continue
                    if parts[1] <= ranges[1]:
                        added = True
                        break
                    if parts[1] > ranges[1]:
                        idRange[j] = (ranges[0], parts[1])
                        added = True
                        idRange = check_overlap(idRange)
                        break
            if not added:
                idRange.append((int(parts[0]), int(parts[1])))
        else:
            idRange.append((int(parts[0]), int(parts[1])))


for range in idRange:
    total += range[1] - range[0] + 1

print(total)
