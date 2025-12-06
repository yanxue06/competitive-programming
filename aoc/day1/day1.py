
with open('./input.json') as f:
    instructions = f.read().strip().strip('"').split(',')

psw = 50
count = 0

for instruction in instructions:

    if instruction[0] == 'L':
        tmp = psw - int(instruction[1:])

        if tmp < 0:
            psw = tmp % 100
        else:
            psw = tmp
    else:

        tmp = psw + int(instruction[1:])

        if tmp > 99:
            psw = tmp % 100
        else:
            psw = tmp

    if psw == 0:
        count += 1

print(count)