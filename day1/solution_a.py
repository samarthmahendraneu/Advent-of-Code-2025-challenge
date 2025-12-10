



with open('day1/input.txt', 'r') as f:
    data = f.read()


inputs = data.split('\n')
password = 0

dial_position = 50

for input in inputs:
    direction = input[:1]
    ticks = int(input[1:])

    if direction == 'L':
        dial_position -= ticks
    else:
        dial_position += ticks
    if dial_position < 0:
        while dial_position < 0:
            dial_position = 100 + dial_position
    elif dial_position>99:
        while dial_position > 99:
            dial_position = dial_position-100

    if dial_position == 0:
        password += 1

print(password)







