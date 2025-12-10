



with open('input.txt', 'r') as f:
    data = f.read()


inputs = data.split('\n')
password = 0
dial_position = 50

for input in inputs:
    direction = input[:1]
    ticks = int(input[1:])

    for _ in range(ticks):
        if direction == 'L':
            dial_position -= 1
        else:
            dial_position += 1

        if dial_position < 0:
            dial_position += 100
        elif dial_position > 99:
            dial_position -= 100

        if dial_position == 0:
            password += 1

print(password)







