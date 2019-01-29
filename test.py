result = []
line = input()
while line != 'end':
    result.append([int(i) for i in line.split()])
    line = input()

new_result = [[0 for _ in range(len(el))] for el in result]
for i in range(len(result)):
    for j in range(len(result[i])):
        new_result[i][j] = result[(i - 1) % len(result)][j] \
                         + result[(i + 1) % len(result)][j] \
                         + result[i][(j - 1) % len(result[i])] \
                         + result[i][(j + 1) % len(result[i])]
for row in new_result:
    print(*row)