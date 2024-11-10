
def calcualte(initial, commands):
    left_order = ['N', 'W', 'S', 'E']
    right_order = ['N', 'E', 'S', 'W']

    res_list = []

    res_list.append(initial)

    for each in commands:
        prev_x, prev_y, prev_direction = res_list[-1]
        if each == 'L':
            index = left_order.index(prev_direction)
            if index < 3:
                next_direction = left_order[index + 1]
            else:
                next_direction = left_order[0]

            next_x, next_y = prev_x, prev_y
            

        elif each == 'R':
            index = right_order.index(prev_direction)
            if index < 3:
                next_direction = right_order[index + 1]
            else:
                next_direction = right_order[0]

            next_x, next_y = prev_x, prev_y

        
        elif each == 'M':
            if prev_direction == 'N':
                next_y = prev_y + 1
                next_x = prev_x

            if prev_direction == 'E':
                next_x = prev_x + 1
                next_y = prev_y

            if prev_direction == 'S':
                next_y = prev_y - 1
                next_x = prev_x

            if prev_direction == 'W':
                next_x = prev_x - 1
                next_y = prev_y

            next_direction = prev_direction
        res_list.append((next_x, next_y, next_direction))

    return res_list[-1]


initial = (3, 3, 'E')
commands = ['M', 'M', 'R', 'M', 'M','R','M','R','R','M']
print(calcualte(initial, commands))
