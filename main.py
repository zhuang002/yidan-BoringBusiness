layout = [[0]*401 for j in range(201)]

current = [-5, -1]


def setLayout(row: int, col: int) -> bool:
    r = -row
    c = col + 200
    if r<0 or r>200 or c<0 or c>400:
        return False
    if layout[r][c] == 1:
        return False
    layout[r][c] = 1
    return True


for i in range(-1,-4,-1):
    setLayout(i, 0)

for i in range(1,4,1):
    setLayout(-3, i)

for i in range(-4, -6, -1):
    setLayout(i, 3)

for i in range(4, 6, 1):
    setLayout(-5, i)

for i in range(-4, -2, 1):
    setLayout(i, 5)

for i in range(6, 8, 1):
    setLayout(-3, i)

for i in range(-4, -8, -1):
    setLayout(i, 7)

for i in range(6, -2, -1):
    setLayout(-7, i)

for i in range(-6, -4, 1):
    setLayout(i, -1)


line = input().split(' ')
direction = line[0]
steps = int(line[1])


def move(direction: str, steps: int) -> bool:
    if direction == 'l':
        for i in range(steps):
            if not setLayout(current[0], current[1] - (i+1)):
                current[1] -= steps
                return False
        current[1] -= steps
        return True
    elif direction == 'r':
        for i in range(steps):
            if not setLayout(current[0], current[1] + (i+1)):
                current[1] += steps
                return False
        current[1] += steps
        return True
    elif direction == 'u':
        for i in range(steps):
            if not setLayout(current[0] + (i+1), current[1]):
                current[0] += steps
                return False
        current[0] += steps
        return True
    elif direction == 'd':
        for i in range(steps):
            if not setLayout(current[0] - (i + 1), current[1]):
                current[0] -= steps
                return False
        current[0] -= steps
        return True
    else:
        return False


while direction != 'q':
    if move(direction, steps):
        print(str(current[1]) + ' ' + str(current[0]) + ' safe')
    else:
        print(str(current[1]) + ' ' + str(current[0]) + ' DANGER')
        break
    line = input().split(' ')
    direction = line[0]
    steps = int(line[1])

