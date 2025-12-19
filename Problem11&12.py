file = open('P11input.txt', 'r')
lines = file.read()
input = lines.split("\n")
input[0] = input[0].split()
input[1] = input[1].split()
input[2] = input[2].split()
input[3] = input[3].split()
input[4] = input[4].split()

total = 0

# input = [["11"], 
#          ["11"], 
#          ["111"], 
#          ["111"], 
#          ["*"]]

for i in range(len(input[0])):
    maxlen = max(len(input[0][i]), len(input[1][i]), len(input[2][i]), len(input[3][i]))
    multList = []
    prod = 0
    for j in range(maxlen):
        if input[4][i] == '+':
            temp = ""
            if j < len(input[0][i]):
                temp += input[0][i][len(input[0][i]) - j - 1]
            if j < len(input[1][i]):
                temp += input[1][i][len(input[1][i]) - j - 1]
            if j < len(input[2][i]):
                temp += input[2][i][len(input[2][i]) - j - 1]
            if j < len(input[3][i]):
                temp += input[3][i][len(input[3][i]) - j - 1]
            total += int(temp.strip())
        elif input[4][i] == '*':
            temp = ""
            if j < len(input[0][i]):
                temp += input[0][i][len(input[0][i]) - j - 1]
            if j < len(input[1][i]):
                temp += input[1][i][len(input[1][i]) - j - 1]
            if j < len(input[2][i]):
                temp += input[2][i][len(input[2][i]) - j - 1]
            if j < len(input[3][i]):
                temp += input[3][i][len(input[3][i]) - j - 1]
            multList.append(int(temp.strip()))
            prod = 1

    for k in multList:
        prod *= k
    total += prod

print(total)